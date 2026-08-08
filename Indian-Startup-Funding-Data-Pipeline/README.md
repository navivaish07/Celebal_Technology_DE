# Indian Startup Funding Intelligence Pipeline

## 📌 Project Overview

The **Indian Startup Funding Intelligence Pipeline** is a cloud-based data engineering project developed to process, clean, transform, and analyze startup investment data.

The project uses Microsoft Azure services together with Databricks and PySpark to build an end-to-end data pipeline. The raw startup funding dataset is first stored in Azure Data Lake Storage Gen2 and then processed through a Medallion Architecture consisting of Bronze, Silver, and Gold layers.

The Gold layer contains analytical datasets that can be used to understand startup funding patterns across industries, cities, investors, investment stages, and years.

This project demonstrates the practical implementation of data ingestion, data cleaning, transformation, validation, Delta Lake storage, and SQL-based analytics.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Build an end-to-end cloud data engineering pipeline.
- Store startup funding data in Azure Data Lake Storage Gen2.
- Use Azure Data Factory for data movement and ingestion.
- Process data using Azure Databricks and PySpark.
- Implement Bronze, Silver, and Gold data layers.
- Clean and standardize the source dataset.
- Perform data quality and validation checks.
- Store processed datasets using Delta Lake.
- Create business-oriented analytical datasets.
- Perform SQL analysis on the processed data.
- Document the complete pipeline and its results.

---

## 🏗️ Project Architecture

The overall data flow implemented in this project is:

```text
                    Startup Funding Dataset
                              |
                              v
                  Azure Data Factory
                              |
                              v
                 Azure Data Lake Storage
                         Gen2
                              |
                              v
                     +----------------+
                     | Bronze Layer   |
                     | Raw Data       |
                     +----------------+
                              |
                              v
                       Azure Databricks
                           PySpark
                              |
                              v
                     +----------------+
                     | Silver Layer   |
                     | Cleaned Data   |
                     +----------------+
                              |
                              v
                     +----------------+
                     | Gold Layer     |
                     | Analytics      |
                     +----------------+
                              |
                    +---------+---------+
                    |         |         |
                    v         v         v
                  SQL      Analysis   Insights

## ☁️ Technologies and Tools

| Technology | Purpose |
|---|---|
| Microsoft Azure | Cloud platform used for the data pipeline |
| Azure Data Factory | Data ingestion and data movement |
| Azure Data Lake Storage Gen2 | Storage for Bronze, Silver, and Gold data |
| Azure Databricks | Data processing and analytics |
| PySpark | Data cleaning and transformation |
| Apache Spark | Distributed data processing |
| Delta Lake | Storage and reliable data management |
| SQL | Analytical queries and business insights |
| Python | Data engineering and transformation |
| GitHub | Source code and project submission |


## 📂 Project Structure

```text
Indian-Startup-Funding-Pipeline/
│
├── notebooks/
│   ├── 01_Bronze_Ingestion.py
│   ├── 02_Silver_Cleaning.py
│   └── 03_Gold_Analytics.py
│
├── sql/
│   └── Gold_Analytics_Queries.sql
│
├── screenshots/
│   ├── Azure_Storage/
│   ├── Data_Factory/
│   ├── Bronze/
│   ├── Silver/
│   ├── Gold/
│   └── SQL/
│
├── project-report/
│   └── Project_Report.pdf
│
└── README.md



---

## 📊 Dataset

Next:

```markdown
## 📊 Dataset

The project uses a startup funding dataset containing information about Indian startups and their investment activities.

The dataset contains information related to:

- Startup name
- Industry
- Sub-vertical
- City
- Investors
- Investment type
- Investment amount
- Date

The dataset contains **1,100 records** and was used to demonstrate data ingestion, cleaning, transformation, and analytical processing.

The processed data covers startup funding information across multiple industries, cities, investors, investment stages, and years.

# 🔄 Pipeline Implementation

The pipeline was implemented in multiple stages, following the Medallion Architecture.

The main stages are:

1. Data Ingestion
2. Bronze Layer
3. Silver Layer
4. Gold Layer
5. SQL Analytics


## 1️⃣ Data Ingestion

The source startup funding dataset was uploaded to **Azure Data Lake Storage Gen2**.

Azure Data Factory was used to move the source data into the required storage location.

The Azure Data Factory pipeline was configured with the required source and destination connections and executed successfully.

The ingestion process was validated by checking the number of records transferred from the source to Azure storage.

### Ingestion Result

- Source records: **1,100**
- Records transferred: **1,100**
- Pipeline execution: **Successful**

This confirmed that the source data was successfully ingested into the cloud storage environment.


## 🥉 2️⃣ Bronze Layer

The Bronze layer represents the raw-data stage of the Medallion Architecture.

The purpose of this layer is to store and access the ingested source data before applying cleaning and transformation operations.

The Bronze data was accessed from Azure Data Lake Storage Gen2 using an ABFSS path.

The Bronze layer was validated using Databricks and PySpark.

### Bronze Validation

The following checks were performed:

- Verify storage connectivity
- Check available files
- Read the source dataset
- Inspect the schema
- Display sample records
- Check the number of records

The Bronze dataset contained **1,100 records**.

The data was then passed to the Silver layer for cleaning and standardization.


## 🥈 3️⃣ Silver Layer

The Silver layer contains the cleaned and standardized version of the Bronze data.

PySpark was used to perform the required transformations and prepare the dataset for analytical processing.

### Silver Layer Operations

The following operations were performed:

- Standardized column names
- Converted data types
- Converted the date column into a proper date format
- Extracted year from the date
- Extracted month from the date
- Checked duplicate records
- Validated categorical values
- Prepared the dataset for Gold-layer analysis


### 🧹 Silver Data Schema

The final Silver dataset contains the following fields:

| Column | Data Type | Description |
|---|---|---|
| startup | String | Name of the startup |
| industry | String | Startup industry |
| sub_vertical | String | Startup sub-sector |
| city | String | Startup city |
| investors | String | Investor information |
| investment_type | String | Type of investment |
| investment_amount_usd | Integer | Investment amount in USD |
| date | Date | Investment date |
| year | Integer | Investment year |
| month | Integer | Investment month |


### ✅ Data Quality Validation

Duplicate records were checked after the cleaning process.

The validation result was:

- Total rows: **1,100**
- Distinct rows: **1,100**
- Duplicate rows: **0**

This confirmed that no duplicate records were present in the processed dataset.

The categorical columns were also inspected to verify that the expected cities, industries, and investment types were available.


## 🥇 4️⃣ Gold Layer

The Gold layer contains business-oriented analytical datasets generated from the cleaned Silver data.

The purpose of the Gold layer is to transform the cleaned data into datasets that can directly answer analytical questions.

Six analytical datasets were created:

1. `top_funded_sectors`
2. `city_funding_rank`
3. `sector_yoy_snapshot`
4. `investor_deal_count`
5. `avg_deal_by_stage`
6. `sector_funding_history`


### 📈 4.1 Top Funded Sectors

The `top_funded_sectors` dataset ranks industries based on their total funding.

The main columns are:

- `industry`
- `total_funding_usd`
- `deal_count`
- `funding_rank`

This dataset helps identify which industries received the highest amount of funding.

### 🏙️ 4.2 City Funding Ranking

The `city_funding_rank` dataset analyzes startup funding by city.

The main columns are:

- `city`
- `total_funding_usd`
- `deal_count`
- `funding_rank`

This dataset allows comparison of startup investment activity across major Indian cities.

### 📊 4.3 Sector Year-over-Year Analysis

The `sector_yoy_snapshot` dataset tracks funding changes across industries over different years.

The dataset contains:

- `industry`
- `year`
- `total_funding_usd`
- `previous_year_funding`
- `yoy_change_percent`

This analysis helps identify sectors where funding increased or decreased compared with the previous year.

### 👥 4.4 Investor Activity

The `investor_deal_count` dataset analyzes investor participation.

The main fields are:

- `investor`
- `deal_count`
- `total_investment_usd`
- `investor_rank`

This dataset helps identify investors with high deal activity and significant investment amounts.

### 💰 4.5 Average Deal by Investment Stage

The `avg_deal_by_stage` dataset analyzes investment amounts according to investment type.

The dataset contains:

- `investment_type`
- `deal_count`
- `avg_deal_usd`
- `min_deal_usd`
- `max_deal_usd`

This allows comparison between early-stage and later-stage investment patterns.

### 📅 4.6 Sector Funding History

The `sector_funding_history` dataset contains historical funding information by industry and year.

The main fields are:

- `industry`
- `year`
- `total_funding_usd`

The dataset supports analysis of funding trends from **2020 to 2025**.

# 🧮 SQL Analytics

SQL was used to analyze the Silver and Gold datasets and generate business insights.

The SQL queries are stored in:

```text
sql/Gold_Analytics_Queries.sql


### ⚠️ Important

When putting the SQL file on GitHub, **do not put your real storage account key anywhere**.

Your `<storage-account>` placeholder is fine for README documentation.

---

# 📊 Analytical Results

Continue:

```markdown
# 📊 Analytical Results

The completed SQL analysis generated insights across industries, cities, investors, investment stages, and years.

### Top Funded Industries

The analysis showed strong funding activity across industries such as:

- Foodtech
- Consumer Electronics
- Retail
- Mobility
- Media
- Agritech
- E-commerce
- Fintech
- SaaS
- Edtech

### Top Funding Cities

The city-level analysis showed significant startup funding activity in:

- Pune
- Kolkata
- Delhi
- Gurugram
- Chennai
- Bengaluru
- Ahmedabad
- Mumbai
- Hyderabad
- Noida

### Investor Activity

Investor analysis was performed using deal count, total investment, and investor ranking.

The analysis included investors such as:

- Y Combinator
- Mirae Asset
- Info Edge
- Accel
- IFC
- Kalaari Capital
- Sequoia Capital India
- Prosus Ventures
- Tiger Global Management
- Nexus Venture Partners

### Investment Stage Analysis

Investment types such as Seed, Angel, Series A, Series B, Series C, Series D, Growth, Debt, Bridge, and Private Equity were compared using average, minimum, and maximum deal values.

### Year-over-Year Analysis

The sector funding history was analyzed from **2020 to 2025** to identify annual changes in funding across different industries.


# 📸 Screenshots

Screenshots documenting the implementation are included in the `screenshots/` directory.

The screenshots provide evidence of:

- Azure Storage configuration
- Azure Data Factory pipeline
- Successful data ingestion
- Bronze layer processing
- Silver layer cleaning
- Data validation
- Gold layer creation
- Gold dataset previews
- SQL query execution
- Analytical results

The screenshots are organized according to the different stages of the pipeline.


# 📄 Project Report

A detailed project report is included in the:

```text
project-report/



---

# 🔐 Security

Very important for GitHub:

```markdown
# 🔐 Security

No sensitive credentials should be committed to the GitHub repository.

The following information must be kept private:

- Azure storage account keys
- Passwords
- Access tokens
- Connection strings
- Secret keys

The notebooks submitted to GitHub should contain placeholders instead of actual credentials.

For production environments, secure authentication mechanisms such as Azure Key Vault or Managed Identity should be considered.


# 📚 Learning Outcomes

This project provided practical experience in:

- Azure cloud services
- Azure Data Factory
- Azure Data Lake Storage Gen2
- Databricks
- PySpark
- Apache Spark
- Delta Lake
- Medallion Architecture
- ETL pipeline development
- Data cleaning
- Data transformation
- Data validation
- SQL analytics
- Cloud data engineering
- GitHub project management


# 🚀 Future Enhancements

The pipeline can be extended in several ways:

### Power BI Dashboard
The Gold datasets can be connected to Power BI to create interactive dashboards.

### Pipeline Scheduling
Azure Data Factory can be configured to run the pipeline automatically on a scheduled basis.

### Incremental Processing
The pipeline can be modified to process only newly added records.

### Automated Data Quality
Additional automated checks can be introduced for missing values, invalid dates, duplicate records, and invalid investment amounts.

### Secure Authentication
Azure Key Vault or Managed Identity can be implemented for improved credential management.

### Predictive Analytics
Machine learning models can be added to study future startup funding trends.

### Real-Time Processing
The architecture can be extended to support streaming investment data.

# 🎯 Conclusion

The **Indian Startup Funding Intelligence Pipeline** demonstrates an end-to-end cloud data engineering workflow for processing and analyzing startup investment data.

The project uses Azure Data Factory for ingestion, Azure Data Lake Storage Gen2 for storage, Databricks and PySpark for processing, Delta Lake for structured data storage, and SQL for analytical queries.

The Medallion Architecture separates the data into Bronze, Silver, and Gold layers, making the pipeline easier to manage, validate, and extend.

The final Gold datasets provide useful analytical views of startup funding across industries, cities, investors, investment stages, and years.

Overall, the project demonstrates the practical application of modern cloud data engineering concepts to a real-world analytical problem.

---

# 👩‍💻 Author

**Vaishnavi Dhanwate**

B.Tech – Information Technology Engineering  
Sanjivani College of Engineering, Kopargaon

### Internship Project

**Indian Startup Funding Intelligence Pipeline**

**Internship Domain:** Data Engineering

### Technologies Used

- Microsoft Azure
- Azure Data Factory
- Azure Data Lake Storage Gen2
- Azure Databricks
- PySpark
- Delta Lake
- SQL
- GitHub

### Architecture

**Bronze → Silver → Gold**

---

**Developed as part of the Data Engineering Internship at Celebal Technologies.**
