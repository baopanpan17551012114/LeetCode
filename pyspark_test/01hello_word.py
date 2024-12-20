# coding: utf-8
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("WordCountHelloWorld")
sc = SparkContext(conf=conf)

file_rdd = sc.textFile("data/words.txt")
words_rdd = file_rdd.flatMap(lambda line: line.split(" "))
words_with_one_rdd = words_rdd.map(lambda x: (x, 1))
result_rdd = words_with_one_rdd.reduceByKey(lambda a, b: a + b)
print(result_rdd.collect())

"""单维"""
rdd1 = sc.parallelize([1, 2, 3, 4, 5, 6, 6, 3, 4])
# groupBy
rdd2 = rdd1.groupBy(lambda x: 1 if (x % 2 == 0) else 2)
# print(rdd2.map(lambda x: (x[0], list(x[1]))).collect())
# filter
rdd3 = rdd1.filter(lambda x: x % 2 == 0)
# distinct
rdd4 = rdd1.distinct()
# union
rdd5 = rdd1.union(sc.parallelize(['a', ['b', 1]]))
# join
rdd6 = sc.parallelize([(1001, "zhangsan"), (1002, "lisi")]).join(sc.parallelize([(1001, "tech"), (1002, "ui")]))
# intersection
rdd7 = rdd1.intersection(sc.parallelize([1, 2]))
print(rdd7.glom().collect())

"""多维"""
rdd1 = sc.parallelize([[1, 2, 3], [4, 5, 6]])
# map
rdd2 = rdd1.map(lambda x: x + [2])
# flatMap
rdd3 = rdd1.flatMap(lambda x: x + [2])

"""KV型"""
rdd1 = sc.parallelize([('a', 1), ('a', 2), ('b', 3), ('c', 4), ('c', 5)])
# reduceByKey
rdd4 = rdd1.reduceByKey(lambda a, b: a**b)
# mapValues
rdd5 = rdd1.mapValues(lambda x: x * 10)
# groupByKey
rdd6 = rdd1.groupByKey()
# sortBy
rdd7 = rdd1.sortBy(lambda x: x[1])
# sortByKey
rdd8 = rdd1.sortByKey(keyfunc=lambda x: str(x).lower())
print(rdd8.collect())




