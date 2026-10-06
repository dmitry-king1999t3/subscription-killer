\# 🔪 subscription-killer



> Finds forgotten subscriptions in your bank statement and shows how to cancel them. Runs locally.



\## Why



People lose \*\*$30–50 per month\*\* on subscriptions they forgot about:

free trials that auto-renewed, duplicate services, unnoticed price hikes.



\## How



1\. Feed it a bank statement (CSV)

2\. Detects recurring charges by merchant, amount, and period

3\. Flags abandoned, duplicates, and price hikes

4\. Shows how to cancel + how much you'll save



\## Pros



\- 🔒 \*\*100% local\*\* — no servers, no telemetry

\- 💸 \*\*Real savings\*\* — typically $30–50/mo

\- ⚡ \*\*One command\*\* — `subkiller scan statement.csv`

\- 🌍 \*\*Multi-bank\*\* — Chase, BoA, Wells Fargo, generic CSV

\- 🧩 \*\*Extensible\*\* — add your bank in a single file



\## Quick start



```bash

pip install subkiller

subkiller scan \~/Downloads/statement.csv

```



\## Example output



```

💸 Found 7 recurring charges totalling $47/mo



🔴 Abandoned:  Hulu            $17.99/mo (unused 4 months)

🟡 Duplicate:  iCloud + Google One → keep one, save $2.99/mo

🟠 Price hike: Spotify $10.99 → $11.99/mo



💰 Potential savings: $23/mo = $276/year

```



\## License



MIT

