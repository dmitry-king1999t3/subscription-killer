import unittest
from datetime import datetime

from src.subkiller.scanner import find_recurring, calculate_savings


class TestScanner(unittest.TestCase):

    def test_find_recurring(self):
        transactions = [
            {
                "date": datetime(2026, 1, 1),
                "merchant": "Netflix",
                "amount": 9.99,
            },
            {
                "date": datetime(2026, 2, 1),
                "merchant": "Netflix",
                "amount": 9.99,
            },
            {
                "date": datetime(2026, 3, 1),
                "merchant": "Netflix",
                "amount": 9.99,
            },
        ]

        result = find_recurring(transactions)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["merchant"], "Netflix")
        self.assertEqual(result[0]["amount"], 9.99)

    def test_ignore_non_recurring(self):
        transactions = [
            {
                "date": datetime(2026, 1, 1),
                "merchant": "Amazon",
                "amount": 50.00,
            },
            {
                "date": datetime(2026, 3, 20),
                "merchant": "Amazon",
                "amount": 50.00,
            },
        ]

        result = find_recurring(transactions)

        self.assertEqual(len(result), 0)

    def test_calculate_savings(self):
        recurring = [
            {
                "merchant": "Netflix",
                "amount": 9.99,
                "count": 3,
                "interval": 30,
            },
            {
                "merchant": "Spotify",
                "amount": 10.99,
                "count": 3,
                "interval": 30,
            },
        ]

        result = calculate_savings(recurring)

        self.assertEqual(result["monthly"], 20.98)
        self.assertEqual(result["yearly"], 251.76)


if __name__ == "__main__":
    unittest.main()