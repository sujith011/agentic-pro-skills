import unittest
from store import read_invoice


class StoreTests(unittest.TestCase):
    def test_own_invoice(self):
        self.assertEqual(100, read_invoice("a", "invoice-a")["total"])


if __name__ == "__main__":
    unittest.main()
