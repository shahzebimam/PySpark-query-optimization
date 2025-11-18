# Databricks notebook source
# MAGIC %md
# MAGIC **Turn Off AQE**

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.functions import col,lit, regexp_replace, StringType

# COMMAND ----------

spark.conf.set('spark.sql.adaptive.enabled', False)

# COMMAND ----------

spark.conf.get('spark.sql.adaptive.enabled')

# COMMAND ----------

df = spark.read.format('csv')\
    .option('header', True)\
    .option('inferSchema', True)\
    .load('/FileStore/RawData/BigMart_Sales.csv')

# COMMAND ----------

display(df)

# COMMAND ----------

df.rdd.getNumPartitions()

# COMMAND ----------

# MAGIC %md
# MAGIC **Changing default Partition to 128KB**

# COMMAND ----------

spark.conf.set("spark.sql.files.maxPartitionBytes",131072 )

# COMMAND ----------

df = spark.read.format('csv')\
    .option('header', True)\
    .option('inferSchema', True)\
    .load('/FileStore/RawData/BigMart_Sales.csv').display()

# COMMAND ----------

# MAGIC %md
# MAGIC **Changing the default Partition size to 128MB**

# COMMAND ----------

spark.conf.set('spark.sql.files.maxPartitionBytes', 134217728)

# COMMAND ----------

# MAGIC %md
# MAGIC **Repartitioning**