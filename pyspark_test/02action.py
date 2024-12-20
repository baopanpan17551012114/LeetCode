# coding: utf-8
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("WordCountHelloWorld")
sc = SparkContext(conf=conf)
"""KV型"""
rdd1 = sc.parallelize([('a', 1), ('a', 2), ('b', 3), ('c', 4), ('c', 5)])
# ountByKey
value1 = rdd1.countByKey()
# reduce
value2 = rdd1.reduce(lambda a, b: (a[0] + b[0], a[1] + b[1]))
# fold
value3 = sc.parallelize(range(10), 3).fold(10, lambda a, b: a + b)
# first
value4 = rdd1.first()
# take
value5 = rdd1.take(8)
# count
value6 = rdd1.count()
# takeSample
value7 = rdd1.takeSample(False, 3)
# takeOrdered
value8 = rdd1.takeOrdered(3, lambda x: x[1])
# foreach
rdd1.foreach(lambda x: print(x))

rdd1.saveAsTextFile('data/data')