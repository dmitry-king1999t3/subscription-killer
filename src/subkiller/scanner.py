import csv
from collections import defaultdict
from datetime import datetime


def load_transactions(filename):
    transactions = []

    with open(filename, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames:
            raise ValueError("CSV file has no headers.")

        fields = {field.lower().strip(): field for field in reader.fieldnames}

        date_field = fields.get("date")
        merchant_field = fields.get("merchant") or fields.get("description")
        amount_field = fields.get("amount")

        if not date_field or not merchant_field or not amount_field:
            raise ValueError(
                "CSV must contain date, merchant/description and amount columns."
            )

        for row in reader:
            try:
                date = datetime.fromisoformat(
                    row[date_field].strip()
                )
                merchant = row[merchant_field].strip()
                amount = abs(float(row[amount_field].replace("$", "").replace(",", "")))

                transactions.append({
                    "date": date,
                    "merchant": merchant,
                    "amount": amount,
                })

            except (ValueError, TypeError):
                continue

    return transactions


def find_recurring(transactions):
    grouped = defaultdict(list)

    for transaction in transactions:
        key = (
            transaction["merchant"].lower(),
            round(transaction["amount"], 2),
        )
        grouped[key].append(transaction)

    recurring = []

    for (merchant, amount), items in grouped.items():
        if len(items) < 2:
            continue

        items.sort(key=lambda x: x["date"])

        intervals = []

        for previous, current in zip(items, items[1:]):
            days = (current["date"] - previous["date"]).days
            intervals.append(days)

        average_interval = sum(intervals) / len(intervals)

        if 20 <= average_interval <= 40:
            recurring.append({
                "merchant": items[0]["merchant"],
                "amount": amount,
                "count": len(items),
                "interval": round(average_interval),
            })

    return recurring


def calculate_savings(recurring):
    monthly = sum(item["amount"] for item in recurring)

    return {
        "monthly": round(monthly, 2),
        "yearly": round(monthly * 12, 2),
    }