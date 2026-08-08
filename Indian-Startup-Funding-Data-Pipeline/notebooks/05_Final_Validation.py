# Databricks notebook source
storage_account = "vaishstartupstoragexxxxx"
storage_key = "xxxxxxxxxxxxxxxxxxxxxx"


spark.conf.set(
    f"fs.azure.account.key.{storage_account}.dfs.core.windows.net",
    storage_key
)

# COMMAND ----------

# DBTITLE 1,Define  paths
bronze_path = f"abfss://startup-data@{storage_account}.dfs.core.windows.net/bronze/startup_bronze.csv"

silver_path = f"abfss://startup-data@{storage_account}.dfs.core.windows.net/silver/startup_silver"

gold_base = f"abfss://startup-data@{storage_account}.dfs.core.windows.net/gold"

print("Bronze:", bronze_path)
print("Silver:", silver_path)
print("Gold:", gold_base)

# COMMAND ----------

# DBTITLE 1,Bronze Count
df_bronze = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(bronze_path)

print("Bronze row count:", df_bronze.count())

# COMMAND ----------

# DBTITLE 1,Sliver Count
df_silver = spark.read.format("delta").load(silver_path)

print("Silver row count:", df_silver.count())

# COMMAND ----------

df_silver.printSchema()

# COMMAND ----------

# DBTITLE 1,Gold validation
gold_tables = [
    "top_funded_sectors",
    "city_funding_rank",
    "sector_yoy_snapshot",
    "investor_deal_count",
    "avg_deal_by_stage",
    "sector_funding_history"
]

for table in gold_tables:
    path = f"{gold_base}/{table}"
    df = spark.read.format("delta").load(path)
    print(f"{table}: {df.count()} rows")

# COMMAND ----------

# DBTITLE 1,Validate the Gold outputs with actual data
display(
    spark.read.format("delta")
    .load(f"{gold_base}/top_funded_sectors")
    .orderBy("funding_rank")
    .limit(10)
)

# COMMAND ----------

display(
    spark.read.format("delta")
    .load(f"{gold_base}/city_funding_rank")
    .orderBy("funding_rank")
    .limit(10)
)

# COMMAND ----------

# DBTITLE 1,Gold preview
display(
    spark.read.format("delta")
    .load(f"{gold_base}/investor_deal_count")
    .orderBy("deal_count", ascending=False)
    .limit(10)
)

# COMMAND ----------

