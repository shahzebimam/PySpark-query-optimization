# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC create schema PySpark

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC create table PySpark.DeltaLake (
# MAGIC   ID int,
# MAGIC   Salary int
# MAGIC )
# MAGIC
# MAGIC using delta
# MAGIC location '/FileStore/RawData/DeltaTbl'

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC insert into PySpark.DeltaLake values
# MAGIC (5, 200),
# MAGIC (6, 200);
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC OPTIMIZE delta.`/FileStore/RawData/DeltaTbl` ZORDER BY (ID)