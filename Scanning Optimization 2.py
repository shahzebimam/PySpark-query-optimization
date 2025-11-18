# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.functions import col,lit, regexp_replace, StringType

# COMMAND ----------

df = spark.read.format('csv')\
    .option('header', True)\
    .option('inferSchema', True)\
    .load('/FileStore/RawData/BigMart_Sales.csv')

# COMMAND ----------

df = df.repartition(10)

# COMMAND ----------

df.rdd.getNumPartitions()

# COMMAND ----------

df.withColumn('Partition_id', spark_partition_id()).display()

# COMMAND ----------

df.write.format('parquet').mode('append').option('path', '/FileStore/RawData/ParquetFile').save()

# COMMAND ----------

df_New = spark.read.format('parquet').load('/FileStore/RawData/ParquetFile')

# COMMAND ----------

df_New.display()

# COMMAND ----------

df_New = df_New.filter(col('Outlet_Location_Type')=='Tier 1')

# COMMAND ----------

df_New.display()

# COMMAND ----------

df.write.format('parquet').mode('append').partitionBy('Outlet_Location_Type').option('path', '/FileStore/RawData/ParquetWriteOpttimization').save( )

# COMMAND ----------

df_New = spark.read.format('parquet').load('/FileStore/RawData/ParquetWriteOpttimization')

# COMMAND ----------

df_New = df_New.filter(col('Outlet_Location_Type')=='Tier 1')

df_New.display()