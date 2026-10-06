import argparse

from .scanner import (
    load_transactions,
    find_recurring,
    calculate_savings,
)


def main():
    parser = argparse.ArgumentParser(
        description="Find recurring subscriptions in a bank statement."
    )

    parser.add_argument(
        "command",
        choices=["scan"],
        help="Command to execute",
    )

    parser.add_argument(
        "file",
        help="Path to a CSV bank statement",
    )

    args = parser.parse_args()

    if args.command == "scan":
        try:
            transactions = load_transactions(args.file)
            recurring = find_recurring(transactions)
            savings = calculate_savings(recurring)

        except (OSError, ValueError) as error:
            print(f"Error: {error}")
            return 1

        print()
        print(f"💸 Found {len(recurring)} recurring charges")
        print()

        for item in recurring:
            print(
                f"🔄 {item['merchant']:<25} "
                f"${item['amount']:.2f}/mo"
            )

        print()
        print(f"💰 Potential monthly savings: ${savings['monthly']:.2f}")
        print(f"💰 Potential yearly savings:  ${savings['yearly']:.2f}")
        print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())