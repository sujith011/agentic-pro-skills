"""Intentionally defective synchronous evaluation fixture; not production code."""


def run_job(job_id, amount_cents, ledger):
    """Append a credit to this caller-owned in-memory ledger."""
    if not isinstance(job_id, str) or not job_id:
        raise ValueError("job_id must be a nonempty string")
    if type(amount_cents) is not int or amount_cents <= 0:
        raise ValueError("amount_cents must be a positive integer")
    credit = {"job_id": job_id, "amount_cents": amount_cents}
    ledger.append(credit)
    return credit
