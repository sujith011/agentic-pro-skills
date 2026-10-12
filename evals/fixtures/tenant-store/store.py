"""Deliberately incomplete fixture for the cross-tenant repair evaluation."""
INVOICES = {
    "invoice-a": {"tenant": "a", "total": 100},
    "invoice-b": {"tenant": "b", "total": 200},
}


def read_invoice(tenant, invoice_id):
    return INVOICES[invoice_id]
