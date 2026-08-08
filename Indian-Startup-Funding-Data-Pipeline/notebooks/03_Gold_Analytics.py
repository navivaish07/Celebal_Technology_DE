# Databricks notebook source
storage_account = "vaishstartupstoragexxxxx"
storage_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

spark.conf.set(
    f"fs.azure.account.key.{storage_account}.dfs.core.windows.net",
    storage_key
)

# COMMAND ----------

silver_path = f"abfss://startup-data@{storage_account}.dfs.core.windows.net/silver/startup_silver"

df_silver = spark.read \
    .format("delta") \
    .load(silver_path)

display(df_silver.limit(10))

# COMMAND ----------

from pyspark.sql.functions import sum, col

sector_yoy = df_silver.groupBy(
    "industry",
    "year"
).agg(
    sum("investment_amount_usd").alias("total_funding_usd")
)

display(
    sector_yoy.orderBy("industry", "year")
)

# COMMAND ----------

df_silver.printSchema()

# COMMAND ----------

# DBTITLE 1,Create top_funded_sectors
from pyspark.sql.functions import sum, count, round, col

top_funded_sectors = df_silver.groupBy(
    "industry"
).agg(
    sum("investment_amount_usd").alias("total_funding_usd"),
    count("*").alias("deal_count")
).orderBy(
    col("total_funding_usd").desc()
)

display(top_funded_sectors)

# COMMAND ----------

# DBTITLE 1,Add ranking columns
from pyspark.sql.window import Window
from pyspark.sql.functions import rank

sector_window = Window.orderBy(
    col("total_funding_usd").desc()
)

top_funded_sectors = top_funded_sectors.withColumn(
    "funding_rank",
    rank().over(sector_window)
)

display(top_funded_sectors)

# COMMAND ----------

# DBTITLE 1,Save Gold Table 1 as Delta
top_sector_path = f"abfss://startup-data@{storage_account}.dfs.core.windows.net/gold/top_funded_sectors"

top_funded_sectors.write \
    .format("delta") \
    .mode("overwrite") \
    .save(top_sector_path)

# COMMAND ----------

display(
    dbutils.fs.ls(
        f"abfss://startup-data@{storage_account}.dfs.core.windows.net/gold/"
    )
)

# COMMAND ----------

# DBTITLE 1,Read the saved Gold table
display(
    dbutils.fs.ls(
        f"abfss://startup-data@{storage_account}.dfs.core.windows.net/gold/"
    )
)

# COMMAND ----------

# DBTITLE 1,city_funding_rank----Cell 1 — Aggregate funding by city
from pyspark.sql.functions import sum, count, col

city_funding = df_silver.groupBy(
    "city"
).agg(
    sum("investment_amount_usd").alias("total_funding_usd"),
    count("*").alias("deal_count")
)

display(city_funding.orderBy(col("total_funding_usd").desc()))

# COMMAND ----------

# DBTITLE 1,Add ranking
from pyspark.sql.window import Window
from pyspark.sql.functions import rank

city_window = Window.orderBy(
    col("total_funding_usd").desc()
)

city_funding_rank = city_funding.withColumn(
    "funding_rank",
    rank().over(city_window)
)

display(
    city_funding_rank.orderBy("funding_rank")
)   

# COMMAND ----------

# DBTITLE 1,Save as Gold Delta
city_rank_path = f"abfss://startup-data@{storage_account}.dfs.core.windows.net/gold/city_funding_rank"

city_funding_rank.write \
    .format("delta") \
    .mode("overwrite") \
    .save(city_rank_path)

# COMMAND ----------

# DBTITLE 1,Verify
display(
    dbutils.fs.ls(
        f"abfss://startup-data@{storage_account}.dfs.core.windows.net/gold/"
    )
)

# COMMAND ----------

# DBTITLE 1,Sector YoY Snapshot----cell1-Aggregate funding by industry and year
from pyspark.sql.functions import sum, col

sector_year = df_silver.groupBy(
    "industry",
    "year"
).agg(
    sum("investment_amount_usd").alias("total_funding_usd")
)

display(
    sector_year.orderBy("industry", "year")
)

# COMMAND ----------

# DBTITLE 1,Calculate Previous Year's Funding
from pyspark.sql.window import Window
from pyspark.sql.functions import lag

sector_window = Window.partitionBy(
    "industry"
).orderBy(
    "year"
)

sector_yoy = sector_year.withColumn(
    "previous_year_funding",
    lag("total_funding_usd").over(sector_window)
)

display(
    sector_yoy.orderBy("industry", "year")
)

# COMMAND ----------

# DBTITLE 1,Calculate YoY Change
from pyspark.sql.functions import when

sector_yoy = sector_yoy.withColumn(
    "yoy_change_usd",
    col("total_funding_usd") - col("previous_year_funding")
)

sector_yoy = sector_yoy.withColumn(
    "yoy_change_percent",
    when(
        col("previous_year_funding").isNull() |
        (col("previous_year_funding") == 0),
        None
    ).otherwise(
        (col("yoy_change_usd") / col("previous_year_funding")) * 100
    )
)

display(
    sector_yoy.orderBy("industry", "year")
)

# COMMAND ----------

# DBTITLE 1,Round the percentage
from pyspark.sql.functions import round

sector_yoy = sector_yoy.withColumn(
    "yoy_change_percent",
    round(col("yoy_change_percent"), 2)
)

display(
    sector_yoy.orderBy("industry", "year")
)

# COMMAND ----------

# DBTITLE 1,Save as Gold Delta
sector_yoy_path = f"abfss://startup-data@{storage_account}.dfs.core.windows.net/gold/sector_yoy_snapshot"

sector_yoy.write \
    .format("delta") \
    .mode("overwrite") \
    .save(sector_yoy_path)

# COMMAND ----------

# DBTITLE 1,Verify Gold
display(
    dbutils.fs.ls(
        f"abfss://startup-data@{storage_account}.dfs.core.windows.net/gold/"
    )
)

# COMMAND ----------

# DBTITLE 1,investor_deal_count---cell 1- Split investor names
from pyspark.sql.functions import split, explode, trim, col

investor_data = df_silver.withColumn(
    "investor",
    explode(
        split(col("investors"), ",")
    )
)

investor_data = investor_data.withColumn(
    "investor",
    trim(col("investor"))
)

display(
    investor_data.select(
        "startup",
        "investor",
        "investment_amount_usd"
    ).limit(20)
)

# COMMAND ----------

# DBTITLE 1,Count investor deals
investor_deal_count = investor_data.groupBy(
    "investor"
).agg(
    count("*").alias("deal_count"),
    sum("investment_amount_usd").alias("total_investment_usd")
)

investor_deal_count = investor_deal_count.orderBy(
    col("deal_count").desc()
)

display(investor_deal_count.limit(20))

# COMMAND ----------

from pyspark.sql.window import Window
from pyspark.sql.functions import rank

investor_window = Window.orderBy(
    col("deal_count").desc()
)

investor_deal_count = investor_deal_count.withColumn(
    "investor_rank",
    rank().over(investor_window)
)

display(
    investor_deal_count.limit(20)
)

# COMMAND ----------

# DBTITLE 1,Save Gold Table 4
investor_path = f"abfss://startup-data@{storage_account}.dfs.core.windows.net/gold/investor_deal_count"

investor_deal_count.write \
    .format("delta") \
    .mode("overwrite") \
    .save(investor_path)

# COMMAND ----------

# DBTITLE 1,Verify
display(
    dbutils.fs.ls(
        f"abfss://startup-data@{storage_account}.dfs.core.windows.net/gold/"
    )
)

# COMMAND ----------

# DBTITLE 1,avg_deal_by_stage---cell1 -First inspect the actual investment types
display(
    df_silver
    .select("investment_type")
    .distinct()
    .orderBy("investment_type")
)

# COMMAND ----------

# DBTITLE 1,Create the aggregation
from pyspark.sql.functions import avg, min, max, count, round, col

avg_deal_by_stage = df_silver.groupBy(
    "investment_type"
).agg(
    round(avg("investment_amount_usd"), 2).alias("avg_deal_usd"),
    min("investment_amount_usd").alias("min_deal_usd"),
    max("investment_amount_usd").alias("max_deal_usd"),
    count("*").alias("deal_count")
).orderBy(
    col("avg_deal_usd").desc()
)

display(avg_deal_by_stage)

# COMMAND ----------

# DBTITLE 1,Add ranking
from pyspark.sql.window import Window
from pyspark.sql.functions import rank

stage_window = Window.orderBy(
    col("avg_deal_usd").desc()
)

avg_deal_by_stage = avg_deal_by_stage.withColumn(
    "stage_rank",
    rank().over(stage_window)
)

display(avg_deal_by_stage)

# COMMAND ----------

# DBTITLE 1,Save as Delta
stage_path = f"abfss://startup-data@{storage_account}.dfs.core.windows.net/gold/avg_deal_by_stage"

avg_deal_by_stage.write \
    .format("delta") \
    .mode("overwrite") \
    .save(stage_path)

# COMMAND ----------

# DBTITLE 1,Verify
display(
    dbutils.fs.ls(
        f"abfss://startup-data@{storage_account}.dfs.core.windows.net/gold/"
    )
)

# COMMAND ----------

# DBTITLE 1,Create the SCD2 source
from pyspark.sql.functions import current_date, lit

sector_history = sector_yoy.select(
    "industry",
    "year",
    "total_funding_usd"
)

display(sector_history.orderBy("industry", "year"))

# COMMAND ----------

# DBTITLE 1,Create sector_history
from pyspark.sql.functions import current_date, lit

sector_history = sector_yoy.select(
    "industry",
    "year",
    "total_funding_usd"
)

display(
    sector_history.orderBy("industry", "year")
)

# COMMAND ----------

# DBTITLE 1,Add SCD Type 2 columns
sector_history = sector_history \
    .withColumn("effective_from", current_date()) \
    .withColumn("effective_to", lit(None).cast("date")) \
    .withColumn("is_current", lit(True))

display(sector_history)

# COMMAND ----------

# DBTITLE 1,Save it as a Delta table
scd2_path = f"abfss://startup-data@{storage_account}.dfs.core.windows.net/gold/sector_funding_history"

sector_history.write \
    .format("delta") \
    .mode("overwrite") \
    .save(scd2_path)

# COMMAND ----------

# DBTITLE 1,Verify it was created
display(
    dbutils.fs.ls(
        f"abfss://startup-data@{storage_account}.dfs.core.windows.net/gold/"
    )
)

# COMMAND ----------

# DBTITLE 1,Read the SCD2 Delta table
from delta.tables import DeltaTable

scd2_path = f"abfss://startup-data@{storage_account}.dfs.core.windows.net/gold/sector_funding_history"

scd2_table = DeltaTable.forPath(
    spark,
    scd2_path
)

display(spark.read.format("delta").load(scd2_path))

# COMMAND ----------

# DBTITLE 1,Verify current records
current_records = spark.read \
    .format("delta") \
    .load(scd2_path) \
    .filter("is_current = true")

display(
    current_records.orderBy("industry", "year")
)

# COMMAND ----------

# DBTITLE 1,Important SCD2 test
from pyspark.sql.functions import lit

test_update = spark.createDataFrame(
    [
        ("Fintech", 2025, 99999999)
    ],
    ["industry", "year", "total_funding_usd"]
)

test_update = test_update \
    .withColumn("effective_from", current_date()) \
    .withColumn("effective_to", lit(None).cast("date")) \
    .withColumn("is_current", lit(True))

display(test_update)

# COMMAND ----------

# DBTITLE 1,: Create a final Gold verification cell
gold_base = f"abfss://startup-data@{storage_account}.dfs.core.windows.net/gold"

display(dbutils.fs.ls(gold_base))

# COMMAND ----------

# DBTITLE 1,Check each Gold dataset
display(
    spark.read.format("delta")
    .load(f"{gold_base}/top_funded_sectors")
    .limit(10)
)

# COMMAND ----------

display(
    spark.read.format("delta")
    .load(f"{gold_base}/city_funding_rank")
    .limit(10)
)

# COMMAND ----------

display(
    spark.read.format("delta")
    .load(f"{gold_base}/sector_yoy_snapshot")
    .limit(10)
)

# COMMAND ----------

display(
    spark.read.format("delta")
    .load(f"{gold_base}/sector_yoy_snapshot")
    .limit(10)
)

# COMMAND ----------

display(
    spark.read.format("delta")
    .load(f"{gold_base}/avg_deal_by_stage")
    .limit(10)
)

# COMMAND ----------

display(
    spark.read.format("delta")
    .load(f"{gold_base}/sector_funding_history")
    .limit(10)
)

# COMMAND ----------

display(
    spark.read.format("delta")
    .load(f"{gold_base}/top_funded_sectors")
    .limit(10)
)

# COMMAND ----------

display(
    spark.read.format("delta")
    .load(f"{gold_base}/city_funding_rank")
    .limit(10)
)

# COMMAND ----------

display(
    spark.read.format("delta")
    .load(f"{gold_base}/investor_deal_count")
    .limit(10)
)

# COMMAND ----------

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

