# 🏦 BankSphere Intelligence — Banking Performance & Transaction Analytics

A SQL, Excel, and Power BI portfolio project analyzing loan portfolio performance and credit/debit transaction activity for a simulated retail bank, with an emphasis on KPI governance and data quality.

---

## 📋 Project Overview

BankSphere Intelligence is a banking analytics case study built around two operational areas: **loan portfolio performance** (client activity, funding, recovery, delinquency/default, branch and product performance) and **transaction monitoring** (credit/debit flow, bank/branch activity, transaction methods, time trends, and high-value review flags).

The project is deliberately positioned as a **Data Analyst / BI Analyst** portfolio piece rather than a fraud-detection or credit-scoring system. The core workflow moves from Excel source review, through SQL data-quality checks and KPI analysis, into Power BI dashboards, and finishes with documented business findings and recommendations.

What sets this project apart from a typical practice dataset is the data-quality work: several KPI definitions conflicted across the source Excel workbooks and the original Power BI dashboards (e.g., two different "default rate" definitions, an invalid ratio metric). These conflicts were identified, quantified in SQL, and resolved with governed, documented KPI definitions — the kind of reconciliation work a working BI/Data Analyst is actually asked to do.

**Skill focus:** SQL 40% · Power BI 40% · Excel 20%

---

## 🎯 Business Problem

A retail bank needs a consistent management view across lending operations and transaction activity, but existing reports use KPI definitions and labels that aren't standardized across tools. Management needs reliable answers to questions like:

- How large is the loan portfolio, and how many unique clients does it represent?
- What are the actual default, delinquency, and on-time repayment rates?
- Which branches, regions, and products deserve deeper review?
- How are credit/debit flows and transaction volumes trending?
- Which transactions exceed the high-value review threshold, and where are they concentrated?

---

## ✅ Objectives

- Validate and reconcile loan and transaction source data across Excel, SQL, and Power BI
- Define and document a governed KPI dictionary for both modules
- Analyze loan portfolio performance: recovery, default, delinquency, retention, branch/product concentration
- Analyze transaction activity: credit/debit flow, high-value review workload, monthly trends
- Identify and quantify conflicts in the source data rather than silently picking one number
- Build Power BI dashboards that reflect the corrected, governed KPI definitions
- Translate findings into specific, evidence-backed business recommendations

---

## 🗂️ Dataset

| Detail | Loan Portfolio | Transactions |
|---|---|---|
| **File** | `final_fact_cleaned.csv` | `credit_debit_bank.csv` |
| **Records** | 2,000 loan records | 100,000 transaction records |
| **Unique clients / accounts** | 870 unique clients | 100,000 unique customers / accounts |
| **Key fields** | loan amount, funded amount, disbursement date, loan status, credit score, branch, region, repayment behavior, default/delinquency flags | credit/debit amount, transaction date, bank, branch, transaction method, customer ID, account number |
| **Time period** | 2015–2023 (loan disbursements) | Rolling monthly data through Dec 2024 (Dec has 1 day only) |

The data is simulated: amounts are uniformly distributed, credit and debit totals differ by only 0.25%, and standard risk fields (credit score, grade, employment type) show no statistical relationship with default outcomes. This is disclosed openly in the project rather than glossed over — the project demonstrates analytical *method*, not real-world credit or fraud conclusions.

---

## 🛠️ Tools & Technologies

- **SQL** — PostgreSQL 13+ and MySQL 8 (both included), covering `GROUP BY`/`HAVING`/`CASE`, CTEs, subqueries, window functions (`LAG`, `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `NTILE`), rolling averages, and reconciliation queries
- **Power BI** — three `.pbix` dashboards with DAX measures, drill-downs, filters/slicers, and management-facing views
- **Excel** — two workbooks with PivotTables, PivotCharts, and formula-based reconciliation checks
- **Python** — used only for a CSV export utility (`data/export_excel_to_csv.py`); not used for analysis

---

## 🔄 Project Workflow

```text
Excel Source Review
      ↓
SQL Data Quality Checks
      ↓
SQL KPI / Trend / Segment Analysis
      ↓
Power BI Modeling & Dashboards
      ↓
Business Findings
      ↓
Recommendations & Monitoring
```

---

## 🧹 Data Cleaning & Preparation

- Standardized the loan client-ID column name (`client_id`) across all SQL scripts
- Separated **Loan Records** (2,000 rows) from **Unique Clients** (870), which had been mislabeled as the same thing
- Reconciled two conflicting funded-amount fields (`Funded_Amount` vs `Funded_Amount_Inv`)
- Flagged and excluded incomplete calendar periods (December 2024 has only 1 day of data) from trend conclusions
- Identified payment-integrity issues: 185 loans with recovered principal exceeding total payment, and 991 loans (49.6%) with funded amount above loan amount
- Checked NULLs, duplicates, invalid monetary values, and category consistency across both source tables

---

## 🗃️ SQL Analysis

SQL work is organized into eight scripts (mirrored for PostgreSQL and MySQL):

- **Data quality** (`01`, `03`) — NULL checks, duplicate detection with `ROW_NUMBER()`, invalid amounts, category and range validation, period-completeness checks
- **KPI analysis** (`02`, `04`) — loan/transaction KPIs, cohort-based retention, branch and product scorecards, rolling trends, `NTILE()`-based activity segmentation
- **Power BI-ready views** (`05`) — pre-aggregated views feeding the dashboards
- **Reconciliation** (`06`) — cross-checks between SQL, Excel, and Power BI outputs
- **Consistency checks** (`07`) — quantifies the source-data conflicts described below (default definitions, delinquency vs. repayment behavior, duplicate high-value thresholds)

---

## 📊 Power BI / Dashboards

Three dashboards: two for loan portfolio, one for transaction intelligence. As part of this project's correction pass, several dashboard labels were fixed to match governed KPI definitions rather than misleading legacy labels:

- `Total Clients` → **Loan Records** (this card was counting rows, not clients)
- `Default Rate` (5%) → **Default Flag Rate**, clearly distinguished from the primary **Status Default Rate** (10.30%)
- Invalid `Account Activity Ratio` (`COUNT(*) / SUM(Balance)`) → replaced with **Transaction Count**
- `Suspicious Transaction Count` → **High-Value Review Count**, using the governed `Amount > 4,500` rule instead of the legacy `≥ 4,000` workbook flag
- `Product Profitability` → **Product Interest Contribution** (no cost data exists to support a true profitability metric)

Legacy pre-correction screenshots are kept in `images/` for reference; see `docs/powerbi_dashboard_audit.md` for the full correction log.

---

## 📌 Key KPIs

**Loan Portfolio**

| KPI | Value |
|---|---:|
| Loan Records | 2,000 |
| Unique Clients | 870 |
| Active Clients | 324 |
| Total Loan Amount | ₹52.36M |
| Average Loan Amount | ₹26.18K |
| Principal Recovery Rate (as recorded) | 99.05% |
| Status Default Rate (primary) | 10.30% |
| Default Flag Rate (legacy) | 5.00% |
| Delinquency Rate | 10.35% |
| On-Time Repayment Rate | 71.05% |
| Client Retention (2020 → 2021) | 24.5% |

**Transactions**

| KPI | Value |
|---|---:|
| Transaction Count | 100,000 |
| Total Credit | ₹127.60M |
| Total Debit | ₹127.29M |
| Net Flow | ₹0.32M |
| Average Transaction Amount | ₹2,549 |
| High-Value Review Count (> ₹4,500) | 10,428 (10.43%) |
| Legacy Source Flag Count (≥ ₹4,000, reconciliation only) | 20,426 |

---

## 💡 Key Insights

- **Default rate depends entirely on definition.** Status-based default is 10.30% vs. a flag-based 5.00%, and only 10 loans satisfy both — a headline "5% default" figure describes almost none of the loans whose status actually says Default.
- **Standard risk indicators carry no signal on this data.** Credit score correlates at ~0.03 with default; default rate by credit-score band ranges 9.5–14.0%, with the *highest* rate in the 800+ band — supporting the conclusion that the dataset is simulated.
- **Two regions stand out for review.** Bihar/Patna (19.6% default on 92 loans) and Odisha/Bhubaneswar (23.3% on 30 loans) sit well above the 10.3% portfolio average, though sample sizes are small.
- **Portfolio concentration is real.** The top five branches hold 40.4% of loan value; Services-purpose loans are 56.9% of records and 57.7% of recorded interest income.
- **Client retention is low.** Only 24.5% of 2020 borrowers returned to borrow again in 2021.
- **Transaction flows are balanced.** ₹127.60M credit vs. ₹127.29M debit (ratio 1.0025), with a governed high-value review workload of 10.43% of all transactions.
- **Review rates don't differentiate.** High-value share is uniform (10.0–10.8%) across every branch, bank, and transaction method — a flat amount threshold alone can't prioritize review effort.
- **Monthly "trends" are partly a calendar artifact.** Raw monthly transaction counts vary mainly with month length; transactions per active day are stable at 292–301, and December 2024 (1 day of data) is excluded from trend conclusions.

---

## 📈 Business Recommendations

1. **Resolve the default/delinquency definition conflict** with the data owner before either rate is used in a management report; report both, labeled, until resolved.
2. **Prioritize collections/underwriting review** in Bihar/Patna and Odisha/Bhubaneswar, re-testing as more loans accumulate.
3. **Don't use credit score, grade, or employment type for risk decisions** on this dataset — validate these fields against real outcomes first.
4. **Investigate low repeat-borrowing** (24.5% retention) and consider retention offers for clients with strong repayment records.
5. **Monitor purpose and branch concentration** (Services: 56.9% of loans; top 5 branches: 40.4% of value) and set exposure limits.
6. **Standardize on one high-value threshold** (₹4,500, governed) and move to risk-based sampling rather than a flat cut-off, since review rates don't vary meaningfully by segment.
7. **Compare transaction months on a per-active-day basis** and exclude partial periods like December 2024.
8. **Capture multi-transaction history per account** — the current one-transaction-per-customer grain blocks any real retention or behavioral analysis.

---

## 📁 Project Structure

```text
BankSphere_Intelligence_SQL_Excel_PowerBI/
├── README.md
├── CHANGELOG.md
├── data/
│   ├── export_excel_to_csv.py
│   └── csv/
│       ├── final_fact_cleaned.csv
│       └── credit_debit_bank.csv
├── sql/
│   ├── 00_setup.sql … 07_consistency_checks.sql
│   └── postgres/            # PostgreSQL port of all scripts
├── excel/
│   ├── BankSphere_Loan_Portfolio_Analysis.xlsx
│   └── BankSphere_Transaction_Analysis.xlsx
├── powerbi/
│   ├── DAX_Measures.md
│   ├── BankSphere_Loan_Portfolio_Dashboard_1.pbix
│   ├── BankSphere_Loan_Portfolio_Dashboard_2.pbix
│   └── BankSphere_Transaction_Intelligence_Dashboard.pbix
├── reports/
│   ├── business_problem.md
│   ├── stakeholder_requirements.md
│   ├── kpi_dictionary.md
│   ├── data_quality_report.md
│   ├── key_findings.md
│   └── recommendations.md
├── docs/
│   ├── project_architecture.md
│   ├── sql_query_catalog.md
│   ├── excel_workbook_audit.md
│   ├── powerbi_dashboard_audit.md
│   ├── job_description_coverage.md
│   └── interview_guide.md
├── verification/
│   ├── verified_metrics.json
│   └── pbix_package_checks.json
└── images/
    └── *_legacy.png          # pre-correction dashboard screenshots
```

---

## 🚀 How to Run This Project

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/banksphere-intelligence-banking-analytics.git
cd banksphere-intelligence-banking-analytics

# 2. Load the data (PostgreSQL example)
psql -f sql/postgres/00_setup.sql
psql -f sql/postgres/00b_load_data_psql.sql

# 3. Run the analysis scripts in order
psql -f sql/postgres/01_loan_data_quality.sql
psql -f sql/postgres/02_loan_kpi_analysis.sql
psql -f sql/postgres/03_transaction_data_quality.sql
psql -f sql/postgres/04_transaction_kpi_analysis.sql
psql -f sql/postgres/05_powerbi_views.sql
psql -f sql/postgres/06_reconciliation_queries.sql
psql -f sql/postgres/07_consistency_checks.sql

# 4. Open the dashboards
# Open the .pbix files in powerbi/ using Power BI Desktop
```

MySQL 8 scripts are available directly under `sql/` if PostgreSQL isn't available.

---

## 🧠 Key Skills Demonstrated

- SQL: joins, CTEs, subqueries, window functions, KPI logic, data-quality auditing
- Data reconciliation across SQL, Excel, and Power BI
- KPI definition and governance
- Power BI dashboard development and DAX measures
- Excel PivotTable analysis and validation
- Evidence-based business insight and recommendation writing
- Honest handling of conflicting/ambiguous source data

---

## 📝 Conclusion

BankSphere Intelligence takes two banking datasets with genuinely conflicting KPI definitions and turns them into a governed, reconciled analytics layer across SQL, Excel, and Power BI. Rather than picking whichever number matched the existing dashboard, the project surfaces and documents every conflict (default rate, delinquency flag, high-value threshold), states clearly what the data can and can't support, and ends with specific, evidence-backed recommendations for lending operations and transaction review teams.

---

### Portfolio Positioning

**Resume title:** BankSphere Intelligence — Transaction Monitoring & Banking Performance Analytics
**Suggested repo name:** `banksphere-intelligence-banking-analytics`
**One-line description:** SQL, Excel, and Power BI banking analytics project covering loan portfolio performance, transaction monitoring, KPI governance, and data-quality reconciliation.
