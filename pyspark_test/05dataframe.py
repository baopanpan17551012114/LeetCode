# coding: utf-8
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType, IntegerType
import pandas as pd

if __name__ == '__main__':
    spark = SparkSession.builder.\
        appName('test').\
        master('local[*]').\
        getOrCreate()

    sc = spark.sparkContext

    # 方法1
    rdd = sc.textFile()
    df = spark.createDataFrame(rdd, schema=['name', 'age'])

    # 方法2
    schema = StructType().add('name', StringType(), nullable=True).\
        add('age', IntegerType, nullable=False)
    df = spark.createDataFrame(rdd, schema=schema)

    # 方法3
    df = rdd.toDF(['name', 'age'])