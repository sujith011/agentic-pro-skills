import unittest
from jobs import run_job


class JobBaseline(unittest.TestCase):
    def test_new_job(self):
        ledger = []
        result = run_job("job-1", 500, ledger)
        self.assertEqual({"job_id": "job-1", "amount_cents": 500}, result)
        self.assertEqual([result], ledger)


if __name__ == "__main__":
    unittest.main()
