# coding: utf-8
from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession.builder.\
        appName('test').\
        master('local[*]').\
        getOrCreate()

    sc = spark.sparkContext

    df = spark.read.csv()
    df.createTempView('score')

    # SQL风格
    spark.sql("""
    select * from score where name='语文'
    """).show()

    # DSL风格
    df.where("name='语文'").show()