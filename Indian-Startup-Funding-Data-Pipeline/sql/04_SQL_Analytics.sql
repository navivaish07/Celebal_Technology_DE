-- Databricks notebook source
-- MAGIC %python
-- MAGIC storage_account = "vaishstartupstoragexxxxx"
-- MAGIC storage_key = "xxxxxxxxxxxxxxxxxxxxxxxxxx"
-- MAGIC
-- MAGIC
-- MAGIC spark.conf.set(
-- MAGIC     f"fs.azure.account.key.{storage_account}.dfs.core.windows.net",
-- MAGIC     storage_key
-- MAGIC )

-- COMMAND ----------

-- DBTITLE 1,First SQL query: Top Funded Sectors
SELECT
    industry,
    total_funding_usd,
    deal_count,
    funding_rank
FROM delta.`abfss://startup-data@vaishstartupstoragexxxxx.dfs.core.windows.net/gold/top_funded_sectors`
ORDER BY funding_rank;

-- COMMAND ----------

-- DBTITLE 1,Sector Funding Analysis
SELECT
    industry,
    SUM(investment_amount_usd) AS total_funding_usd,
    COUNT(*) AS deal_count
FROM delta.`abfss://startup-data@vaishstartupstoragexxxxx.dfs.core.windows.net/silver/startup_silver`
GROUP BY industry
ORDER BY total_funding_usd DESC;

-- COMMAND ----------

-- DBTITLE 1,City Funding Ranking
SELECT
    city,
    SUM(investment_amount_usd) AS total_funding_usd,
    COUNT(*) AS deal_count,
    RANK() OVER (
        ORDER BY SUM(investment_amount_usd) DESC
    ) AS city_rank
FROM delta.`abfss://startup-data@vaishstartupstoragexxxxx.dfs.core.windows.net/silver/startup_silver`
GROUP BY city
ORDER BY city_rank;

-- COMMAND ----------

-- DBTITLE 1,Investor Activity
SELECT
    investors,
    COUNT(*) AS deal_count,
    SUM(investment_amount_usd) AS total_investment_usd
FROM delta.`abfss://startup-data@vaishstartupstoragexxxxx.dfs.core.windows.net/silver/startup_silver`
WHERE investors IS NOT NULL
  AND TRIM(investors) <> ''
GROUP BY investors
ORDER BY deal_count DESC
LIMIT 20;

-- COMMAND ----------

-- DBTITLE 1,Average Deal by Investment Stage
SELECT
    investment_type,
    COUNT(*) AS deal_count,
    ROUND(AVG(investment_amount_usd), 2) AS avg_deal_usd,
    MIN(investment_amount_usd) AS min_deal_usd,
    MAX(investment_amount_usd) AS max_deal_usd
FROM delta.`abfss://startup-data@vaishstartupstoragexxxxx.dfs.core.windows.net/silver/startup_silver`
GROUP BY investment_type
ORDER BY avg_deal_usd DESC;

-- COMMAND ----------

-- DBTITLE 1,Year-over-Year Funding Analysis
WITH yearly_funding AS (
    SELECT
        industry,
        year,
        SUM(investment_amount_usd) AS total_funding_usd
    FROM delta.`abfss://startup-data@vaishstartupstoragexxxxx.dfs.core.windows.net/silver/startup_silver`
    GROUP BY industry, year
)

SELECT
    industry,
    year,
    total_funding_usd
FROM yearly_funding
ORDER BY industry, year;

-- COMMAND ----------

-- DBTITLE 1,Actual Year-over-Year Funding Change
WITH yearly_funding AS (
    SELECT
        industry,
        year,
        SUM(investment_amount_usd) AS total_funding_usd
    FROM delta.`abfss://startup-data@vaishstartupstoragexxxxx.dfs.core.windows.net/silver/startup_silver`
    GROUP BY industry, year
),

funding_with_previous_year AS (
    SELECT
        industry,
        year,
        total_funding_usd,
        LAG(total_funding_usd) OVER (
            PARTITION BY industry
            ORDER BY year
        ) AS previous_year_funding
    FROM yearly_funding
)

SELECT
    industry,
    year,
    total_funding_usd,
    previous_year_funding,
    ROUND(
        ((total_funding_usd - previous_year_funding)
        / previous_year_funding) * 100,
        2
    ) AS yoy_change_percent
FROM funding_with_previous_year
ORDER BY industry, year;

-- COMMAND ----------

-- DBTITLE 1,Focused EdTech + FinTech Analysis
WITH yearly_funding AS (
    SELECT
        industry,
        year,
        SUM(investment_amount_usd) AS total_funding_usd
    FROM delta.`abfss://startup-data@vaishstartupstoragexxxxx.dfs.core.windows.net/silver/startup_silver`
    WHERE industry IN ('Edtech', 'Fintech')
    GROUP BY industry, year
),

yoy_analysis AS (
    SELECT
        industry,
        year,
        total_funding_usd,
        LAG(total_funding_usd) OVER (
            PARTITION BY industry
            ORDER BY year
        ) AS previous_year_funding
    FROM yearly_funding
)

SELECT
    industry,
    year,
    total_funding_usd,
    previous_year_funding,
    ROUND(
        ((total_funding_usd - previous_year_funding)
        / previous_year_funding) * 100,
        2
    ) AS yoy_change_percent
FROM yoy_analysis
WHERE year >= 2021
ORDER BY industry, year;

-- COMMAND ----------

