# cording:utf-8
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, StringType, StructType, ArrayType

if __name__ == '__main__':
    spark = SparkSession.builder.appName('udf_define').master('local[*]').getOrCreate()
    sc = spark.sparkContext

    rdd = sc.parallelize([
        ('张三', 'class_1', 99),
        ('王五', 'class_2', 35),
        ('王三', 'class_3', 57),
        ('王久', 'class_4', 12),
        ('王丽', 'class_5', 99),
        ('王娟', 'class_1', 90),
        ('王军', 'class_2', 91),
        ('王俊', 'class_3', 33),
        ('王君', 'class_4', 55),
        ('王珺', 'class_5', 66),
        ('郑颖', 'class_1', 11),
        ('郑辉', 'class_2', 33),
        ('张丽', 'class_3', 36),
        ('张张', 'class_4', 79),
        ('黄凯', 'class_5', 90),
        ('黄开', 'class_1', 90),
        ('黄恺', 'class_2', 90),
        ('王凯', 'class_3', 11),
        ('王凯杰', 'class_1', 11),
        ('王开杰', 'class_2', 3),
        ('王景亮', 'class_3', 99)])
    schema = StructType().add('name', StringType()). \
        add('class', StringType()). \
        add('score', IntegerType())
    df = rdd.toDF(schema)
    # 创建表
    df.createTempView('stu')

    # TODO 1:聚合窗口函数的演示
    spark.sql('''
        SELECT *, AVG(score) over() AS avg_socre FROM stu
    ''').show()

    # TODO 2： 排序相关的窗口函数计算
    # RANK over, DENSE_RANK over, ROW_NUMBER over
    spark.sql('''
        SELECT *, ROW_NUMBER() OVER(ORDER BY score DESC) AS row_number_rank,
        DENSE_RANK() OVER(PARTITION BY class ORDER BY score DESC) AS dense_rank,
        RANK() OVER(ORDER BY score) AS RANK
        FROM stu
    ''').show()

    # TODO NTILE
    spark.sql('''
        SELECT *, NTILE(6) OVER(ORDER BY score DESC) FROM stu
    ''').show()

