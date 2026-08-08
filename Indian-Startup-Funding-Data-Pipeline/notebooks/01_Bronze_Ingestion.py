# Databricks notebook source
storage_account = "vaishstartupstoragexxxxx"
storage_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

spark.conf.set(
    f"fs.azure.account.key.{storage_account}.dfs.core.windows.net",
    storage_key
)

# COMMAND ----------

# DBTITLE 1,Test the connection
display(
    dbutils.fs.ls(
        f"abfss://startup-data@{storage_account}.dfs.core.windows.net/"
    )
)

# COMMAND ----------

# DBTITLE 1,Read the Bronze CSV
bronze_path = f"abfss://startup-data@{storage_account}.dfs.core.windows.net/bronze/startup_bronze.csv"

df_bronze = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(bronze_path)

display(df_bronze)

# COMMAND ----------

print("Columns:")
print(df_bronze.columns)

print("\nData types:")
df_bronze.printSchema()


# COMMAND ----------

display(df_bronze.limit(10))

# COMMAND ----------

# DBTITLE 1,Inspect the Bronze Data
df_bronze.printSchema()

# COMMAND ----------

print(df_bronze.columns)


# COMMAND ----------

display(df_bronze)

# COMMAND ----------

