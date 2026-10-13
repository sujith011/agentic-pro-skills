import unittest
from output import validate_invoice


class OutputBaseline(unittest.TestCase):
    def test_valid_invoice(self):
        result = validate_invoice('{"customer_id":"customer-1","amount_cents":500}', {"customer-1"})
        self.assertEqual({"customer_id": "customer-1", "amount_cents": 500}, result)


if __name__ == "__main__":
    unittest.main()
