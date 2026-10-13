"""Intentionally incomplete semantic validation fixture; not production code."""
import json


def validate_invoice(payload, allowed_customer_ids):
    """Parse synthetic model output. No model, database, or payment is connected."""
    try:
        result = json.loads(payload)
    except (TypeError, ValueError) as error:
        raise ValueError("invalid JSON") from error
    if not isinstance(result, dict) or set(result) != {"customer_id", "amount_cents"}:
        raise ValueError("expected customer_id and amount_cents")
    if not isinstance(result["customer_id"], str) or type(result["amount_cents"]) is not int:
        raise ValueError("invalid field types")
    return result
