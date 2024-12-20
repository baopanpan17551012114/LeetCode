# cording:utf-8
import string
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.types import IntegerType, StringType, StructType, ArrayType

if __name__ == '__main__':
    spark = SparkSession.builder.appName('udf_define').master('local[*]').getOrCreate()
    sc = spark.sparkContext

    rdd = sc.parallelize([1, 2, 3, 4, 5], 3)
    df = rdd.map(lambda x: [x]).toDF(['num'])

    # 方法：使用RDD的mapPartitions 算子来完成聚合操作
    # 如果用mapPartitions API 完成UDAF聚合，一定要单分区
    single_partition_rdd = df.rdd.repartition(1)

    def process(iter):
        sum = 0
        for row in iter:
            sum += row['num']
        return [sum]  # 一定要嵌套list，因为mapPartitions方法要求返回值是list对象

    print(single_partition_rdd.mapPartitions(process).collect())

