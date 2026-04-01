# SQL1_Repository
A SQL Project to show skill and knowledge in SQL. <br>
I am analyzing a data set provide by ITAAI. You can find the dataset [**here**](https://www.itaai.com/financial-dataset). The goal is a PNL Analysis with real business data.

This is what the Excel file looks like:

| Table | Meaning | Explaining |
| :--- | :--- | :--- |
| GL | General Ledger | Core transaction data |
| COA | Chart of Accounts | Maps account codes to categories |
| Calendar | Date dimension | Enables time-series analysis |
| Territory | Geographic/Sales regions | Enables segmented P&L by region |
| Cashflow | Cash flow statement | Complements P&L with liquidity view |
| SoCE_St | Statement of Changes in Equity | Equity movements |


**Time period**: 2018–2020 (3 full fiscal years)
**Regions**: North America, Europe, Oceania
**Countries**: USA, Canada, UK, Germany, France, Australia, New Zealand 

## Methodology
**1. Data Ingestion**
All 6 Excel sheets were loaded into a local SQLite database using pandas and sqlite3. Database indexes were created on all JOIN keys to ensure query performance.
<br>
**2. Exploratory Data Analysis**
Each table was profiled for structure, data quality (nulls, duplicates), and referential integrity. All 3 JOIN relationships were verified — GL → COA, GL → Calendar, GL → Territory - with zero unmatched rows across all joins.
<br>
**3. P&L Modelling**
The P&L was constructed by joining the GL to the COA hierarchy (Report → Class → SubClass → Account) and aggregating by year.
<br>
**4. Visualization**
Four interactive Plotly charts were produced:

- Waterfall chart — full P&L build for 2020
- Line chart — Revenue vs Net Profit trend (2018–2020)
- Bar chart — Net Profit breakdown by region and year
- Heatmap — average monthly expenses by category
<br>
<br>

# Key Results:

**P&L Summary**
<br>
<img width="507" height="133" alt="grafik" src="https://github.com/user-attachments/assets/f28c6c56-74cd-45b8-8088-891647187449" />
<br>
<br>

