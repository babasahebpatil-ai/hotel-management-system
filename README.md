# 🏦 BankSphere Intelligence
## Banking Performance & Transaction Analytics

> An end-to-end banking analytics project using **PostgreSQL, Excel, and Power BI** to analyze loan portfolio performance, validate KPI definitions, monitor credit/debit transactions, and build management-ready reporting.

**Author:** Babasaheb Patil  
**Role Focus:** Data Analyst | BI Analyst  
**Domain:** Banking & Financial Services  
**Tech Stack:** PostgreSQL | SQL | Excel | Power BI | DAX

---

## 📌 Project Overview

BankSphere Intelligence is a banking analytics case study designed to analyze lending performance and transaction activity within a retail banking environment.

The project works with:

- **2,000 loan records**
- **870 unique clients**
- **100,000 banking transactions**

The main focus is not only dashboard creation, but also **data validation, KPI reconciliation, SQL analysis, business reporting, and identifying inconsistencies in banking data**.

This project is positioned as a **Data Analyst / BI Analyst portfolio project**, not as a fraud-detection or credit-scoring system.

---

## 📊 Key Results at a Glance

| KPI | Result |
|---|---:|
| Loan Records | 2,000 |
| Unique Clients | 870 |
| Total Loan Amount | ₹52.36M |
| Average Loan Amount | ₹26.18K |
| Status-Based Default Rate | 10.30% |
| Legacy Default Flag Rate | 5.00% |
| Transaction Records | 100,000 |
| Total Credit Amount | ₹127.60M |
| Total Debit Amount | ₹127.29M |
| Net Transaction Flow | ₹0.32M |
| High-Value Transactions | 10,428 |
| High-Value Review Rate | 10.43% |

---

## Business Problem

A retail bank needs a consistent management view across lending operations and transaction activity.

However, different source fields produce different results for important business metrics such as loan default and delinquency.

This creates several reporting challenges:

- inconsistent default-rate definitions;
- disagreement between delinquency and repayment information;
- difficulty reconciling KPIs across different tools;
- limited visibility into branch and geographic performance;
- inconsistent interpretation of high-value transactions.

The goal of this project is to create a reliable analytical workflow that converts raw banking data into consistent and explainable management information.

---

## 🔄 Analytics Workflow

![BankSphere Analytics Workflow](images/project_workflow.png)

```text
Raw Banking Data
        ↓
Data Validation
        ↓
SQL Analysis
        ↓
KPI Definition
        ↓
Data Reconciliation
        ↓
Excel Validation
        ↓
Power BI + DAX
        ↓
Interactive Dashboards
        ↓
Business Insights
```

---

## 🛠️ Technology Stack

| Technology | Project Usage | Focus |
|---|---|---:|
| PostgreSQL | Data validation, SQL analysis, KPI calculation, reconciliation | 40% |
| Power BI | DAX, dashboards, visualization, management reporting | 40% |
| Excel | PivotTables, validation, ad-hoc reconciliation | 20% |
| Git & GitHub | Version control and documentation | Supporting |

### Intentionally Out of Scope

- Python
- Machine Learning
- Tableau
- Fraud Prediction
- Credit Scoring

The goal is to demonstrate a focused **SQL + Excel + Power BI analytics workflow**.

---

# SQL Analysis

PostgreSQL is used as the primary analytical layer.

The SQL workflow covers:

- missing-value checks;
- duplicate validation;
- loan portfolio aggregation;
- unique-client analysis;
- loan default calculations;
- default-definition reconciliation;
- delinquency validation;
- branch-level analysis;
- geographic analysis;
- transaction aggregation;
- high-value transaction analysis;
- CTEs;
- subqueries;
- CASE statements;
- window functions;
- KPI consistency checks;
- Power BI reporting views.

### Business Questions Answered

```text
What is the total loan portfolio value?

How many unique banking clients exist?

What percentage of loans are classified as defaulted?

Why do different default fields produce different results?

Which regions show higher observed default rates?

What is the total credit and debit transaction activity?

How many transactions exceed the review threshold?

Are business KPIs consistent across reporting layers?
```

### SQL Preview

![SQL Analysis](images/sql_analysis.png)

---

# Excel Analysis

Excel is used as an additional reconciliation and validation layer.

The Excel workbooks are used for:

- PivotTable analysis;
- portfolio summaries;
- transaction summaries;
- SQL-result validation;
- KPI reconciliation;
- quick management analysis.

### Excel Preview

![Excel Analysis](images/excel_analysis.png)

---

# 📈 Power BI Dashboard

Power BI converts the validated analytical outputs into management-level dashboards.

## Loan Portfolio Overview

The loan portfolio dashboard includes:

- total loan amount;
- average loan amount;
- total loan records;
- unique clients;
- status-based default rate;
- portfolio status;
- branch-level performance;
- geographic distribution.

![Loan Portfolio Dashboard](images/loan_portfolio_overview_legacy.png)

---

## Branch Performance

The branch analysis compares lending activity and observed default patterns across locations.

![Branch Performance Dashboard](images/branch_performance_legacy.png)

---

## Transaction Overview

The transaction dashboard tracks:

- total credit value;
- total debit value;
- net transaction flow;
- transaction volume;
- high-value transaction count;
- high-value review rate.

![Transaction Overview](images/transaction_overview_legacy.png)

---

## Transaction Drilldown

The drilldown page provides transaction-level investigation and detailed segment analysis.

![Transaction Drilldown](images/transaction_drilldown_legacy.png)

> **Dashboard Note:** Current screenshots were captured before the final report-layout corrections and are therefore treated as legacy screenshots. Final screenshots should replace them after Power BI Desktop verification.

---

# 🔍 Key Findings

## 1. Two Different Default Definitions Exist

The source data contains two conflicting default definitions.

| Default Definition | Result |
|---|---:|
| Status-Based Default Rate | 10.30% |
| Legacy Default Flag Rate | 5.00% |
| Loans Matching Both | 10 |

This means the same portfolio can produce significantly different reported default rates depending on which field is used.

For this project:

**Primary KPI:** Status-Based Default Rate — **10.30%**

**Legacy Reconciliation KPI:** Default Flag Rate — **5.00%**

This highlights the importance of proper KPI governance.

---

## 2. Delinquency Does Not Fully Match Repayment Behavior

Some records show disagreement between delinquency indicators and recorded repayment behavior.

This means delinquency should not automatically be treated as a reliable management KPI without further source-data validation.

---

## 3. Credit Score Shows Weak Relationship With Default

Credit score shows approximately:

```text
Correlation with Default ≈ 0.03
```

Other traditional risk-related fields also show limited separation between defaulted and non-defaulted records.

This is consistent with the simulated nature of the underlying dataset.

---

## 4. Geographic Patterns Need Further Investigation

Bihar / Patna and Odisha / Bhubaneswar show higher observed default rates.

However, these findings are based on relatively small samples.

They should therefore be treated as **investigation signals rather than conclusions about regional credit risk**.

---

## 5. Credit and Debit Activity Is Closely Balanced

Across **100,000 transactions**:

| Metric | Amount |
|---|---:|
| Total Credits | ₹127.60M |
| Total Debits | ₹127.29M |
| Net Flow | ₹0.32M |

The relatively small net flow indicates closely balanced credit and debit activity within the dataset.

---

## 6. High-Value Transaction Review

A transaction-review threshold was defined as:

```text
Transaction Amount > ₹4,500
```

This identifies:

| KPI | Result |
|---|---:|
| High-Value Transactions | 10,428 |
| Review Rate | 10.43% |

These transactions are classified only for **high-value review**.

They are **not classified as fraudulent or suspicious transactions**.

---

## 7. Customer Behavior Analysis Is Limited

Every customer/account appears only once in the transaction dataset.

Therefore, the available data cannot reliably support:

- repeat-purchase behavior;
- transaction-frequency analysis;
- customer retention;
- customer lifecycle analysis;
- longitudinal behavioral segmentation.

---

# 💡 Business Recommendations

Based on the analysis:

- establish one governed definition of loan default;
- maintain a centralized KPI dictionary;
- validate the legacy default flag before continued operational use;
- investigate delinquency and repayment inconsistencies;
- interpret high regional default rates carefully when sample sizes are small;
- use the ₹4,500 threshold as a review metric rather than a fraud label;
- collect multi-transaction customer histories for behavioral analytics;
- introduce automated KPI reconciliation across SQL and BI reporting.

---

# ⚠️ Data Quality & Project Limitations

## Simulated Dataset

The data shows characteristics associated with simulated datasets, including:

- relatively uniform transaction distributions;
- similar review rates across several segments;
- weak relationships between traditional credit-risk variables and default.

The project therefore demonstrates **analytical methodology and BI implementation**, not production banking risk behavior.

---

## Conflicting KPI Definitions

The two default indicators produce materially different results.

Rather than hiding this discrepancy, the project reports both definitions separately.

---

## Transaction-Level Limitation

Each customer/account contains only one transaction record.

This prevents meaningful repeated-customer behavioral analysis.

---

## Power BI Verification

Dashboard layout corrections were made, but the final reports have not yet been completely verified by reopening them in Power BI Desktop.

A final Desktop validation should be completed before a live interview demonstration.

---

## Legacy Dashboard Screenshots

Existing images were captured before the final dashboard corrections.

They are retained as legacy screenshots until new verified screenshots are generated.

---

## Excel Presentation

Some Excel sheets retain generic names.

Sheet naming and workbook presentation should be refined before a live walkthrough.

---

# 📁 Project Structure

```text
banksphere-banking-performance-analytics/
│
├── data/
│   └── csv/
│       ├── credit_debit_bank.csv
│       └── final_fact_cleaned.csv
│
├── sql/
│   └── postgres/
│       ├── 00_setup.sql
│       ├── 00b_load_data_psql.sql
│       ├── 01_loan_data_quality.sql
│       ├── 02_loan_kpi_analysis.sql
│       ├── 03_transaction_data_quality.sql
│       ├── 04_transaction_kpi_analysis.sql
│       ├── 05_powerbi_views.sql
│       ├── 06_reconciliation_queries.sql
│       └── 07_consistency_checks.sql
│
├── excel/
│   ├── BankSphere_Loan_Portfolio_Analysis.xlsx
│   └── BankSphere_Transaction_Analysis.xlsx
│
├── powerbi/
│   ├── BankSphere_Loan_Portfolio_Dashboard_1.pbix
│   ├── BankSphere_Loan_Portfolio_Dashboard_2.pbix
│   ├── BankSphere_Transaction_Intelligence_Dashboard.pbix
│   └── DAX_Measures.md
│
├── reports/
│   ├── business_problem.md
│   ├── data_quality_report.md
│   ├── executive_summary.md
│   ├── key_findings.md
│   ├── kpi_dictionary.md
│   ├── recommendations.md
│   └── stakeholder_requirements.md
│
├── docs/
│   ├── project_architecture.md
│   ├── sql_query_catalog.md
│   ├── powerbi_dashboard_audit.md
│   ├── excel_workbook_audit.md
│   └── interview_guide.md
│
├── verification/
│   ├── verified_metrics.json
│   └── pbix_package_checks.json
│
├── images/
│   ├── project_workflow.png
│   ├── sql_analysis.png
│   ├── excel_analysis.png
│   ├── loan_portfolio_overview_legacy.png
│   ├── branch_performance_legacy.png
│   ├── transaction_overview_legacy.png
│   └── transaction_drilldown_legacy.png
│
├── README.md
└── .gitignore
```

---

# How to Run the Project

## Requirements

```text
PostgreSQL 13+
psql / pgAdmin
Microsoft Excel
Microsoft Power BI Desktop
Git
```

### 1. Clone Repository

```bash
git clone https://github.com/<your-username>/banksphere-banking-performance-analytics.git
cd banksphere-banking-performance-analytics
```

### 2. Create PostgreSQL Database

```bash
createdb banksphere_db
```

### 3. Create Tables

```bash
psql -d banksphere_db -f sql/postgres/00_setup.sql
```

### 4. Load Banking Data

```bash
psql -d banksphere_db -f sql/postgres/00b_load_data_psql.sql
```

### 5. Run Data Quality Checks

```bash
psql -d banksphere_db -f sql/postgres/01_loan_data_quality.sql
psql -d banksphere_db -f sql/postgres/03_transaction_data_quality.sql
```

### 6. Run KPI Analysis

```bash
psql -d banksphere_db -f sql/postgres/02_loan_kpi_analysis.sql
psql -d banksphere_db -f sql/postgres/04_transaction_kpi_analysis.sql
```

### 7. Create Power BI Views

```bash
psql -d banksphere_db -f sql/postgres/05_powerbi_views.sql
```

### 8. Run Reconciliation Checks

```bash
psql -d banksphere_db -f sql/postgres/06_reconciliation_queries.sql
psql -d banksphere_db -f sql/postgres/07_consistency_checks.sql
```

### 9. Open Power BI Reports

Open the `.pbix` files available inside:

```text
powerbi/
```

Refresh the corresponding data source if required.

---

# Skills Demonstrated

This project demonstrates practical experience in:

**SQL & Database**
- PostgreSQL
- CTEs
- Subqueries
- CASE expressions
- Window functions
- Data aggregation

**Data Analytics**
- Data Cleaning
- Data Validation
- Data Reconciliation
- KPI Analysis
- Exploratory Analysis
- Root Cause Investigation

**Business Intelligence**
- Power BI
- DAX
- Data Modeling
- Dashboard Development
- KPI Reporting
- Data Visualization

**Excel**
- PivotTables
- Data Validation
- Reconciliation
- Ad-hoc Analysis

**Business Skills**
- Banking Analytics
- Loan Portfolio Analysis
- Transaction Monitoring
- KPI Governance
- Business Reporting
- Insight Generation

---

# 💼 Portfolio Positioning

This project demonstrates more than dashboard development.

It follows a complete Data Analyst workflow:

```text
Business Problem
      ↓
Data Validation
      ↓
SQL Analysis
      ↓
KPI Governance
      ↓
Data Reconciliation
      ↓
Power BI Reporting
      ↓
Business Insights
```

### Suitable Roles

- Data Analyst
- BI Analyst
- Power BI Analyst
- SQL Analyst
- Junior Business Intelligence Analyst

---

# Resume Description

### BankSphere Intelligence — Banking Performance & Transaction Analytics
**PostgreSQL | Excel | Power BI | DAX**

- Analyzed **2,000 loan records and 100,000 banking transactions** to evaluate portfolio performance, transaction activity, branch-level patterns, and high-value transaction reviews.
- Developed SQL-based KPI validation and reconciliation workflows across **870 unique clients**, identifying differences between a **10.30% status-based default rate** and a **5.00% legacy default rate**.
- Built Power BI dashboards and DAX measures to monitor **₹52.36M loan exposure, ₹127.60M credits, ₹127.29M debits**, and **10,428 high-value transactions** for management reporting.

---

# Repository Name

```text
banksphere-banking-performance-analytics
```

### GitHub Description

> Banking analytics project using PostgreSQL, Excel, and Power BI for loan portfolio analysis, KPI reconciliation, data-quality validation, and transaction monitoring.

---

# 👤 Author

**Babasaheb Patil**

B.Tech — Computer Science Engineering  
Data Analytics | Business Intelligence | SQL | Power BI

GitHub: [babasahebpatil-ai](https://github.com/babasahebpatil-ai)

---

## Project Takeaway

> **Data → Validation → SQL Analysis → KPI Governance → Power BI → Business Insights**

BankSphere Intelligence demonstrates how a Data Analyst can move beyond basic dashboard creation by validating source data, questioning inconsistent KPIs, reconciling reporting definitions, and transforming banking data into reliable management information.

---

*This project uses simulated banking data and is intended for educational and portfolio purposes. The results demonstrate analytical methodology, SQL analysis, KPI governance, reconciliation, Excel validation, and Power BI reporting rather than real-world credit-risk or fraud assessment.*
