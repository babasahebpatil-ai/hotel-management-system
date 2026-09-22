# BankSphere Intelligence — Banking Performance & Transaction Analytics

End-to-end analytics on a simulated retail bank: a **loan portfolio** and a **transaction activity** dataset, analyzed with PostgreSQL, Excel, and Power BI — with an emphasis on KPI governance, not just dashboards.

![SQL](https://img.shields.io/badge/SQL-PostgreSQL_16-336791)
![Power BI](https://img.shields.io/badge/BI-Power_BI-F2C811)
![Excel](https://img.shields.io/badge/Excel-workbooks-217346)

## Table of Contents
- [Overview](#overview)
- [Key Findings](#key-findings)
- [Repository Structure](#repository-structure)
- [Architecture](#architecture)
- [Quick Start](#quick-start)
- [Run Order](#run-order)
- [Dashboards](#dashboards)
- [Documentation](#documentation)
- [Data Notes & Limitations](#data-notes--limitations)
- [Verification](#verification)
- [License](#license)

## Overview
Two independent modules, analyzed separately:
- **Loans** — 2,000 records, 870 unique clients, ₹52.4M disbursed
- **Transactions** — 100,000 records, ₹255M in credit + debit flow

The core contribution is **metric governance**: exposing where the source data gives conflicting definitions (e.g. two different "default rates") and giving every KPI one documented meaning across SQL, Excel, and Power BI.

## Key Findings
- Status-based default is **10.3%**, flag-based default is **5.0%** — barely overlap
- Bihar/Patna and Odisha/Bhubaneswar run ~2x the average default rate (small samples)
- Credit score, grade, and income show almost no relation to default
- Only **24.5%** of 2020 borrowers returned to borrow again in 2021
- Credit and debit flows balance almost exactly (net ₹0.32M)
- High-value review (>₹4,500) flags **10.43%** of transactions, uniformly across branches
- Every customer has exactly one transaction, so customer-level trend analysis isn't possible

Full detail: [`reports/key_findings.md`](reports/key_findings.md) · [`reports/executive_summary.md`](reports/executive_summary.md)

## Repository Structure
```text
data/       Source CSVs + Excel-to-CSV export script
docs/       Architecture, SQL catalog, Power BI & Excel audit notes
excel/      Loan portfolio & transaction Excel workbooks
images/     Legacy dashboard screenshots
powerbi/    Three .pbix dashboards + DAX measure reference
reports/    Business problem, findings, KPIs, recommendations
sql/        PostgreSQL scripts (data quality, KPIs, views, checks)
verification/  Reproducible headline metrics (JSON)
```

## Architecture
```text
Excel workbooks
      │
      ▼
PostgreSQL tables (final_fact_cleaned / credit_debit_bank)
      │
      ├── Data quality checks
      ├── KPI / business analysis
      ├── BI-ready views
      └── Reconciliation checks
      │
      ▼
Power BI dashboards → Findings & recommendations
```
Focus split: **SQL 40% · Power BI 40% · Excel 20%**. Loan and transaction modules are kept separate — this isn't modeled as one relational schema.

## Quick Start
Run from the project root (`BankSphere_Intelligence_SQL_Excel_PowerBI/`) so relative CSV paths resolve:

```bash
# regenerate CSVs from the Excel workbooks, if data/csv/ is empty
python data/export_excel_to_csv.py

createdb banksphere_db
psql -d banksphere_db -f sql/postgres/00_setup.sql
psql -d banksphere_db -f sql/postgres/00b_load_data_psql.sql
```

Requires **PostgreSQL 13+** (tested on 16) and, for the export script, `pandas` + `openpyxl`.

## Run Order
| Step | Script | Purpose |
|---|---|---|
| 1 | `01_loan_data_quality.sql` | NULLs, duplicates, invalid values |
| 2 | `02_loan_kpi_analysis.sql` | Loan KPIs, retention, branch/product breakdown |
| 3 | `03_transaction_data_quality.sql` | Transaction validation, month completeness |
| 4 | `04_transaction_kpi_analysis.sql` | Transaction KPIs, trends, rankings |
| 5 | `05_powerbi_views.sql` | BI-ready views for Power BI |
| 6 | `06_reconciliation_queries.sql` | One-row checks matching Excel/Power BI cards |
| 7 | `07_consistency_checks.sql` | Source-data conflicts (default, delinquency, thresholds) |

All scripts live in `sql/postgres/`; see [`sql/postgres/README.md`](sql/postgres/README.md) for the pgAdmin walkthrough and a full MySQL-to-PostgreSQL syntax cheat sheet.

## Dashboards
- `BankSphere_Loan_Portfolio_Dashboard_1.pbix` — portfolio overview
- `BankSphere_Loan_Portfolio_Dashboard_2.pbix` — branch & segment drilldown
- `BankSphere_Transaction_Intelligence_Dashboard.pbix` — transaction overview & high-value review

Open with Power BI Desktop, or connect it directly to the `banksphere` schema (Get Data → PostgreSQL) to read the `vw_*` views. Measure logic: [`powerbi/DAX_Measures.md`](powerbi/DAX_Measures.md).

## Documentation
| File | Covers |
|---|---|
| `reports/business_problem.md` | Scenario and management questions |
| `reports/kpi_dictionary.md` | One definition per KPI |
| `reports/data_quality_report.md` | Data issues found and how they were handled |
| `reports/recommendations.md` | What to act on vs. what needs more review |
| `docs/sql_query_catalog.md` | What each SQL script answers |
| `docs/powerbi_dashboard_audit.md` | Corrections applied to the PBIX files |
| `docs/excel_workbook_audit.md` | Workbook structure and known issues |

## Data Notes & Limitations
- The dataset appears simulated — standard risk fields show almost no relationship with default
- Findings should **not** drive fraud, credit-risk, or profitability decisions
- One transaction per customer removes any customer-level retention analysis
- No 2024 loan data; December 2024 transactions cover a single day only

## Verification
`verification/verified_metrics.json` holds the reproducible headline numbers (loan count, default rates, transaction totals) that the SQL, Excel, and Power BI outputs are checked against, so the three stay consistent.

## License
No license file is included yet. Add one (MIT is a common default for portfolio projects) before sharing this publicly if you want to state usage terms explicitly.
