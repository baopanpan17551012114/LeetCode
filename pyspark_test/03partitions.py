# coding: utf-8
import pandas as pd
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

conf = SparkConf().setMaster("local[*]").setAppName("WordCountHelloWorld")
sc = SparkContext(conf=conf)

rdd1 = sc.parallelize(list(range(10)), 3)
# mapPartitions
rdd2 = rdd1.mapPartitions(lambda x: [ele * 10 for ele in x])
print(rdd2.glom().collect())

# foreachPartition
rdd1.foreachPartition(lambda data: print('-'*10 + '\n', [ele for ele in data]))

rdd1_1 = sc.parallelize([(a, b) for (a, b) in zip(range(10), range(10))])
# partitionBy
rdd3 = rdd1_1.partitionBy(5, lambda x: x % 5)
# repartition
rdd4 = rdd1.repartition(1)
print(rdd4.glom().collect())


spark = SparkSession.builder\
    .appName("StocksDataWriteExample")\
    .enableHiveSupport()\
    .getOrCreate()

if __name__ == '__main__':
    # 没有累加器的代码，最后count打印为0；有累加器时结果为10
    rdd = sc.parallelize(list(range(1, 11)), 2)
    # count = 0
    count = sc.accumulator(0)
    def map_func(data):
        global count
        count += 1
        print(count)

    rdd.map(map_func).collect()
    print(count)





