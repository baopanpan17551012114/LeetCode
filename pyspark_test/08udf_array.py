# cording:utf-8
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.types import IntegerType, StringType, StructType, ArrayType

if __name__ == '__main__':
    spark = SparkSession.builder.appName('udf_define').master('local[*]').getOrCreate()
    sc = spark.sparkContext

    # 构建一个RDD
    rdd = sc.parallelize([['hadoop spark flink'], ['hadoop flink java']])
    df = rdd.toDF(['line'])

    # 注册UDF，UDF的执行函数定义
    def split_line(data):
        return data.split(' ')


    # TODO 1:方式1注册UDF
    # 返回值用于DSL风格    内部注册的名称用于SQL(字符串表达式)风格
    udf2 = spark.udf.register('udf1', split_line, ArrayType(StringType()))

    # DLS 风格
    df.select(udf2(df['line'])).show()

    # SQL风格
    df.selectExpr('udf1(line)').show()

    df.createTempView('lines')
    spark.sql('SELECT udf1(line) FROM lines').show(truncate=False)

    # TODO 2:方式的形式构建UDF
    udf3 = F.udf(split_line, ArrayType(StringType()))
    df.select(udf3(df['line'])).show(truncate=False)

