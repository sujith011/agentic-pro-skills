"""Copy selected skills to a Claude Code or Codex directory.
Dry-run by default; refuse existing content differences. Python 3.10+.
"""
import argparse
import re
import shutil
import sys
from pathlib import Path

CORE = ["understand-first", "proof-first-testing", "root-cause-debug",
        "five-axis-gate", "real-browser-check", "threat-surface"]
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


def snapshot(folder):
    if folder.is_symlink() or not folder.is_dir():
        raise ValueError(f"Expected a regular directory: {folder}")
    result = {}
    for entry in sorted(folder.rglob("*")):
        if entry.is_symlink():
            raise ValueError(f"Refusing symlink resource: {entry}")
        result[entry.relative_to(folder).as_posix()] = None if entry.is_dir() else entry.read_bytes()
    return result


def install(source, destination, selected, *, apply=False):
    source = Path(source).resolve()
    destination = Path(destination)
    if destination.is_symlink():
        raise ValueError(f"Refusing symlink destination: {destination}")
    destination = destination.resolve()
    if destination == source or source in destination.parents:
        raise ValueError("Destination cannot be inside the source skills directory")
    plans = []
    for name in dict.fromkeys(selected):
        if not NAME.fullmatch(name):
            raise ValueError(f"Invalid skill name: {name}")
        folder = source / name
        if not (folder / "SKILL.md").is_file():
            raise ValueError(f"Unknown or incomplete skill: {name}")
        source_content = snapshot(folder)
        target = destination / name
        exists = target.exists() or target.is_symlink()
        if exists and snapshot(target) != source_content:
            raise ValueError(f"Existing content differs; nothing overwritten: {target}")
        plans.append((folder, target, exists))
    # Preflight every selection before making the first copy.
    for folder, target, exists in plans:
        print(f"{'SKIP identical' if exists else 'COPY' if apply else 'WOULD COPY'} {folder.name} -> {target}")
        if apply and not exists:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(folder, target)
    return plans


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent", choices=["claude", "codex"], required=True)
    parser.add_argument("--scope", choices=["user", "project"], default="user")
    parser.add_argument("--project-root", type=Path)
    parser.add_argument("--skills", nargs="+", default=CORE,
                        help="Skill names, or 'all'; defaults to six core workflows")
    parser.add_argument("--apply", action="store_true", help="Perform the printed copies")
    args = parser.parse_args()
    if args.scope == "project" and args.project_root is None:
        parser.error("--project-root is required for project scope")
    if args.scope == "user" and args.project_root is not None:
        parser.error("--project-root applies only to project scope")
    source = Path(__file__).resolve().parents[1] / "skills"
    if "all" in args.skills and args.skills != ["all"]:
        parser.error("'all' must be the only --skills value")
    selected = sorted(path.name for path in source.iterdir() if path.is_dir()) if args.skills == ["all"] else args.skills
    base = Path.home() if args.scope == "user" else args.project_root
    destination = base / (".claude" if args.agent == "claude" else ".agents") / "skills"
    try:
        install(source, destination, selected, apply=args.apply)
    except (ValueError, OSError) as error:
        print(str(error), file=sys.stderr)
        return 1
    if not args.apply:
        print("Dry run only. Repeat with --apply to install.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
