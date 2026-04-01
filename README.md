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


**Time period**: 2018–2020 (3 full fiscal years) <br>
**Regions**: North America, Europe, Oceania <br>
**Countries**: USA, Canada, UK, Germany, France, Australia, New Zealand <br>

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

- Waterfall chart - full P&L build for 2020
- Line chart - Revenue vs Net Profit trend (2018–2020)
- Bar chart - Net Profit breakdown by region and year
- Heatmap - average monthly expenses by category
<br>
<br>

# Key Results:

**P&L Summary**
<br>
<img width="507" height="133" alt="grafik" src="https://github.com/user-attachments/assets/f28c6c56-74cd-45b8-8088-891647187449" />
<br>
<br>
**Margin Analysis**
<br>
<img width="573" height="144" alt="grafik" src="https://github.com/user-attachments/assets/589d487a-8bec-4484-b20b-6e703f4d5474" />
<br>
<br>

## Insights
<br>

**Strong revenue growth.** Revenue more than doubled from 2018 to 2020, growing from 3.6M to 7.8M (+119%) <br>
**Healthy gross margins.** Gross margin consistently above 66%, indicating strong pricing power relative to direct costs <br>
**2019 was the most efficient year.** Net margin peaked at 22.9%, the highest across all 3 years <br>
**2020 margin compression.** Despite record revenue, Net Margin declined from 22.9% to 16.5%, suggesting operating costs scaled faster than revenue in 2020. Worth investigating at the expense category level <br>
**EBIT plateau.** EBIT grew strongly from 2018 to 2019 (+99%) but nearly stalled in 2020 (+3%), driven by rising operating expenses <br>
<br>
<br>

## Visualizations
<br>
<img width="1304" height="457" alt="grafik" src="https://github.com/user-attachments/assets/14b41647-3819-41b3-a116-794d49693e1a" />
<br>
<br>
<img width="1304" height="457" alt="grafik" src="https://github.com/user-attachments/assets/7ba58fcb-a542-4b32-b897-2a85ab225330" />
<br>
<br>
<img width="1307" height="459" alt="grafik" src="https://github.com/user-attachments/assets/5dd3c1ed-ae9e-45a5-ab3b-e78c9624474a" />
<br>
<br>
<img width="1306" height="459" alt="grafik" src="https://github.com/user-attachments/assets/787e5283-4ae8-4af3-bf89-e0e8082eac8f" />
<br>
<br>

See more of the Visualization Code [here](https://github.com/timleiler/SQL1_Repository/blob/main/Code/Visualization.ipynb).



