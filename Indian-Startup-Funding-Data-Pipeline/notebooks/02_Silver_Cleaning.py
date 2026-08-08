# Databricks notebook source
storage_account = "vaishstartupstoragexxxxx"
storage_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

spark.conf.set(
    f"fs.azure.account.key.{storage_account}.dfs.core.windows.net",
    storage_key
)

# COMMAND ----------

display(
    dbutils.fs.ls(
        f"abfss://startup-data@{storage_account}.dfs.core.windows.net/"
    )
)

# COMMAND ----------

# DBTITLE 1,Read Bronze
bronze_path = f"abfss://startup-data@{storage_account}.dfs.core.windows.net/bronze/startup_bronze.csv"

df_bronze = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(bronze_path)

display(df_bronze.limit(10))

# COMMAND ----------

# DBTITLE 1,Inspect dataset
print("Number of rows:", df_bronze.count())
print("Number of columns:", len(df_bronze.columns))

print("\nColumn names:")
print(df_bronze.columns)

print("\nSchema:")
df_bronze.printSchema()

# COMMAND ----------

# DBTITLE 1,Check missing values
from pyspark.sql.functions import col, sum, when

null_counts = df_bronze.select([
    sum(when(col(c).isNull(), 1).otherwise(0)).alias(c)
    for c in df_bronze.columns
])

display(null_counts)

# COMMAND ----------

# DBTITLE 1,Check duplicates
total_rows = df_bronze.count()
distinct_rows = df_bronze.dropDuplicates().count()

print("Total rows:", total_rows)
print("Distinct rows:", distinct_rows)
print("Duplicate rows:", total_rows - distinct_rows)

# COMMAND ----------

# DBTITLE 1,Standardize column names
df_silver = df_bronze

df_silver = df_silver.withColumnRenamed("Startup", "startup") \
                     .withColumnRenamed("Industry", "industry") \
                     .withColumnRenamed("SubVertical", "sub_vertical") \
                     .withColumnRenamed("City", "city") \
                     .withColumnRenamed("Investors", "investors") \
                     .withColumnRenamed("InvestmentType", "investment_type") \
                     .withColumnRenamed("InvestmentAmount_USD", "investment_amount_usd")

display(df_silver.limit(10))

# COMMAND ----------

# DBTITLE 1,Clean text columns
from pyspark.sql.functions import trim, col

text_columns = [
    "startup",
    "industry",
    "sub_vertical",
    "city",
    "investors",
    "investment_type"
]

for c in text_columns:
    df_silver = df_silver.withColumn(c, trim(col(c)))

display(df_silver.limit(10))

# COMMAND ----------

# DBTITLE 1,Standardize City Names
from pyspark.sql.functions import lower, initcap

df_silver = df_silver.withColumn(
    "city",
    initcap(lower(trim(col("city"))))
)

display(
    df_silver.select("city").distinct().orderBy("city")
)

# COMMAND ----------

# DBTITLE 1,Standardize Industry
df_silver = df_silver.withColumn(
    "industry",
    initcap(lower(trim(col("industry"))))
)

display(
    df_silver.select("industry").distinct().orderBy("industry")
)

# COMMAND ----------

df_silver.printSchema()

# COMMAND ----------

# DBTITLE 1,Standardize the Date column
df_silver = df_silver.withColumnRenamed("Date", "date")

display(df_silver.limit(10))

# COMMAND ----------

# DBTITLE 1,Create useful date columns
from pyspark.sql.functions import year, month

df_silver = df_silver.withColumn(
    "year",
    year(col("date"))
)

df_silver = df_silver.withColumn(
    "month",
    month(col("date"))
)

display(df_silver.limit(10))

# COMMAND ----------

# DBTITLE 1,Handle text values safely
from pyspark.sql.functions import length

for c in text_columns:
    count_empty = df_silver.filter(
        (col(c).isNull()) | (trim(col(c)) == "")
    ).count()
    
    print(f"{c}: {count_empty} empty/null values")

# COMMAND ----------

# DBTITLE 1,Check City Standardization
display(
    df_silver
    .select("city")
    .distinct()
    .orderBy("city")
)   

# COMMAND ----------

# DBTITLE 1,Check Industry Values
display(
    df_silver
    .select("industry")
    .distinct()
    .orderBy("industry")
)

# COMMAND ----------

# DBTITLE 1,Standardize industry spelling/capitalization
from pyspark.sql.functions import when

df_silver = df_silver.withColumn(
    "industry",
    when(col("industry") == "Saas", "SaaS")
    .otherwise(col("industry"))
)

display(df_silver.select("industry").distinct().orderBy("industry"))

# COMMAND ----------

# DBTITLE 1,Final Silver quality check
print("Total rows:", df_silver.count())
print("Total columns:", len(df_silver.columns))

print("\nSchema:")
df_silver.printSchema()

# COMMAND ----------

# DBTITLE 1,Check nulls one final time
null_counts = df_silver.select([
    sum(when(col(c).isNull(), 1).otherwise(0)).alias(c)
    for c in df_silver.columns
])

display(null_counts)

# COMMAND ----------

# DBTITLE 1,Save the Silver Layer as Delta
silver_path = f"abfss://startup-data@{storage_account}.dfs.core.windows.net/silver/startup_silver"

df_silver.write \
    .format("delta") \
    .mode("overwrite") \
    .save(silver_path)

# COMMAND ----------

# DBTITLE 1,Verify Silver
display(
    dbutils.fs.ls(
        f"abfss://startup-data@{storage_account}.dfs.core.windows.net/silver/"
    )
)

# COMMAND ----------

display(df_silver.limit(10))

# COMMAND ----------

df_silver.printSchema()

# COMMAND ----------

