# Databricks notebook source
from pyspark.sql.functions import *


# COMMAND ----------

data = [('A', 100),
        ('A',200),
        ('A',300),
        ('B',400),
        ('C',500)]
df = spark.createDataFrame(data, ['UserID', 'purchase'])     

# COMMAND ----------

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC **Adding Salt Column**

# COMMAND ----------

df = df.withColumn('Salt Column', floor(rand()*3))

# COMMAND ----------

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC **Creating Concate on Original GroupBy Column & Salt Column to create a new groupby column**

# COMMAND ----------

df = df.withColumn('User_id_Salt', concat('userid', lit('-'), 'Salt Column'))

# COMMAND ----------

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC **Applying groupby on new column**

# COMMAND ----------

df = df.groupBy('User_id_Salt').agg(sum('Purchase').alias('Total_Amount')).display()