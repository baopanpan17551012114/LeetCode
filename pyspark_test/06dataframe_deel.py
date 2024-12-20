# coding: utf-8
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType, IntegerType

if __name__ == '__main__':
    spark = SparkSession.builder.\
        appName('test').\
        master('local[*]').\
        getOrCreate()

    df = spark.createDataFrame()

    # DSL风格
    df.select(['id', 'subject']).show()
    df.filter('score < 99').show()
    df.where('score < 99').show()
    df.groupBy('subject').count().show()
    # df.groupBy API的返回值GroupedData, 不是DataFrame
    # 它是一个有分组关系的数据结构, 有一些API供我们对分组做聚合
    # SQL: group by 后接上聚合: sum, avg, count, min, mean
    # GroupedData 类似于SQL分组后的数据结构, 同样有各种聚合方法
    # GroupedData 调用聚合方法后, 返回值依旧是DataFrame
    # GroupedData 只是一个中转的对象, 最终还是要获得DataFrame的结果

    # SQL风格
    # 注册DataFrame称为表, 然后通过使用spark.sql()来执行SQL语句查询, 结果返回一个DataFrame。
    # 将DataFrame注册成表的方式:
    df.createTempView('score')  # 注册一个临时视图(表)
    df.createOrReplaceTempView('score')  # 注册一个临时表, 如果存在进行替换
    df.createGlobalTempView('score')  # 注册一个全局表
    # 全局表: 跨SparkSession对象使用, 在一个程序内的多个SparkSession中均可调用, 查询前带上前缀: global_tmp
    spark.sql("select word, count(*) as cnt from words group by word order by cnt desc").show()