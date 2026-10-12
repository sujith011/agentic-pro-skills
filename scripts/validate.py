"""Validate this repository's portable skill format and local Markdown links.
Uses Python 3.10+ standard library. External URLs are not fetched.
Frontmatter intentionally supports only name and JSON-quoted description scalars.
"""
import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
LINK = re.compile(r"!?\[[^\]\n]*\]\(([^)\s]+)\)")


def prose(text):
    """Exclude fenced examples before checking links and headings."""
    return re.sub(r"(?ms)^([\x60~]{3,})[^\n]*\n.*?^\1\s*$", "", text)


def anchors(text):
    result = set()
    counts = {}
    for heading in re.findall(r"(?m)^#{1,6}\s+(.+?)\s*#*\s*$", prose(text)):
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        result.add(slug if not count else f"{slug}-{count}")
    return result


def frontmatter(text, path):
    errors = []
    fields = {}
    lines = text.splitlines()
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        return {}, [f"{path}: missing or unterminated frontmatter"]
    end = lines.index("---", 1)
    for line in lines[1:end]:
        if not line.strip():
            continue
        key, separator, raw = line.partition(":")
        key, raw = key.strip(), raw.strip()
        if not separator or key not in {"name", "description"}:
            errors.append(f"{path}: unsupported frontmatter line: {line}")
            continue
        if key in fields:
            errors.append(f"{path}: duplicate frontmatter key {key}")
        if key == "description":
            try:
                value = json.loads(raw)
                if not isinstance(value, str) or not value.strip() or len(value) > 1024:
                    raise ValueError("description must be a nonempty string of at most 1024 characters")
                fields[key] = value
            except (ValueError, json.JSONDecodeError):
                errors.append(f"{path}: description must be a valid JSON-quoted string")
        else:
            fields[key] = raw
    for key in ("name", "description"):
        if key not in fields:
            errors.append(f"{path}: missing {key}")
    if not "\n".join(lines[end + 1:]).strip():
        errors.append(f"{path}: empty skill body")
    return fields, errors


def validate_repository(root):
    root = Path(root).resolve()
    errors = []
    skill_root = root / "skills"
    names = set()
    if not skill_root.is_dir():
        errors.append("skills/: missing skills directory")
    else:
        for folder in sorted(skill_root.iterdir()):
            if folder.is_symlink():
                errors.append(f"{folder.name}: symlink skill is not supported")
                continue
            if not folder.is_dir():
                errors.append(f"skills/{folder.name}: expected a skill directory")
                continue
            entry = folder / "SKILL.md"
            if not entry.is_file() or entry.is_symlink():
                errors.append(f"skills/{folder.name}: missing regular SKILL.md entrypoint")
                continue
            text = entry.read_text(encoding="utf-8")
            fields, issues = frontmatter(text, entry.relative_to(root))
            errors.extend(issues)
            name = fields.get("name", "")
            if not NAME.fullmatch(name) or len(name) > 64:
                errors.append(f"{entry.relative_to(root)}: invalid name")
            if name != folder.name:
                errors.append(f"{entry.relative_to(root)}: name must match folder")
            if name in names:
                errors.append(f"{entry.relative_to(root)}: duplicate skill name {name}")
            names.add(name)

    readme = root / "README.md"
    if not readme.is_file():
        errors.append("README.md: missing catalog")
    else:
        text = readme.read_text(encoding="utf-8")
        count = re.search(r"\*\*(\d+) engineering skills?\*\*", text)
        if count is None or int(count.group(1)) != len(names):
            errors.append("README.md: declared skill count does not match discovered skills")
        catalog = set(re.findall(r"\]\(skills/([^/]+)/SKILL\.md\)", prose(text)))
        if catalog != names:
            errors.append("README.md: catalog does not match skill directories")

    for document in sorted(root.rglob("*.md")):
        if document.is_symlink():
            errors.append(f"{document.relative_to(root)}: symlink document is not supported")
            continue
        text = document.read_text(encoding="utf-8")
        for target in LINK.findall(prose(text)):
            url = urlsplit(target)
            if url.scheme or url.netloc:
                continue
            resolved = (document.parent / unquote(url.path)).resolve() if url.path else document
            try:
                resolved.relative_to(root)
            except ValueError:
                errors.append(f"{document.relative_to(root)}: link escapes repository: {target}")
                continue
            if not resolved.exists():
                errors.append(f"{document.relative_to(root)}: missing link target {target}")
            elif url.fragment and resolved.suffix == ".md":
                if unquote(url.fragment) not in anchors(resolved.read_text(encoding="utf-8")):
                    errors.append(f"{document.relative_to(root)}: missing anchor in {target}")
    version_path = root / "VERSION"
    if version_path.exists():
        version = version_path.read_text(encoding="utf-8").strip()
        changelog = root / "CHANGELOG.md"
        if not re.fullmatch(r"\d+\.\d+\.\d+", version):
            errors.append("VERSION: expected major.minor.patch")
        if not readme.exists() or f"Version: **{version}**" not in readme.read_text(encoding="utf-8"):
            errors.append("README.md: release version does not match VERSION")
        if not changelog.exists() or not re.search(rf"(?m)^## {re.escape(version)} - \d{{4}}-\d{{2}}-\d{{2}}$", changelog.read_text(encoding="utf-8")):
            errors.append("CHANGELOG.md: missing current release entry")
    scenarios_path = root / "evals" / "scenarios.json"
    if scenarios_path.exists():
        try:
            scenarios = json.loads(scenarios_path.read_text(encoding="utf-8"))
            if not isinstance(scenarios, list) or not scenarios:
                raise ValueError("expected a nonempty list")
            ids = set()
            for case in scenarios:
                if not isinstance(case, dict):
                    raise ValueError("each scenario must be an object")
                case_id = case.get("id")
                if not isinstance(case_id, str) or not NAME.fullmatch(case_id) or case_id in ids:
                    raise ValueError("scenario IDs must be unique valid names")
                ids.add(case_id)
                for key in ("prompt", "setup"):
                    if not isinstance(case.get(key), str) or not case[key].strip():
                        raise ValueError(f"{case_id}: missing {key}")
                for key in ("skills", "checks", "hard_fail"):
                    value = case.get(key)
                    if not isinstance(value, list) or not value or not all(isinstance(item, str) and item.strip() for item in value):
                        raise ValueError(f"{case_id}: {key} must be a nonempty string list")
                if set(case["skills"]) - names:
                    raise ValueError(f"{case_id}: unknown evaluation skill")
        except (ValueError, json.JSONDecodeError) as error:
            errors.append(f"evals/scenarios.json: {error}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        errors = validate_repository(args.root)
    except (OSError, UnicodeError) as error:
        print(f"Validation could not complete: {error}", file=sys.stderr)
        return 1
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("PASS: metadata, catalog/count, release version, evaluation schema, and local links")
    print("External URLs and agent behavior were not evaluated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
