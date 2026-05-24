Global Economic & Geopolitical Intelligence Dashboard

💡 Project Overview
An end-to-end data analytics project that integrates macroeconomic indicators with real-time commodity market trends. The dashboard provides a high-level view of how global inflation correlates with asset pricing (Gold & Crude Oil) across major economies including India, USA, China, and Germany.

🛠 Tech Stack
Language: Python 3.x

Database: MySQL (Relational Schema)

Visualization: Power BI

APIs: World Bank API (Macro Data), Yahoo Finance (Market Data)

Modeling: DAX (Data Analysis Expressions)

📈 Key Features
Automated Data Pipeline: Python scripts to fetch, clean, and load data directly into a local MySQL instance.

Star Schema Modeling: Optimized data model using a central Calendar table to synchronize yearly inflation data with daily stock/commodity prices.

Interactive Analytics: Dynamic country-level filtering and Top-N date-filtered KPI cards for real-time market snapshots.

Currency Benchmarking: Global market tracking for Gold and Crude Oil in USD.

📂 Repository Structure
Plaintext
├── sql_scripts/
│   └── schema_setup.sql       # MySQL table definitions
├── python_scripts/
│   ├── fetch_economics.py     # World Bank API integration
│   └── fetch_commodities.py   # Yahoo Finance integration
├── dashboard/
│   └── Global_Intelligence.pbix # Power BI File
└── README.md
🚀 How to Run
Database: Execute schema_setup.sql in MySQL Workbench.

Pipeline: Run the Python scripts in /python_scripts/ to populate the tables.

Analytics: Open the .pbix file in Power BI and click Refresh to sync with your MySQL data.
