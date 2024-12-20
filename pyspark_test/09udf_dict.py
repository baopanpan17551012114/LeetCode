# cording:utf-8
import string
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.types import IntegerType, StringType, StructType, ArrayType

if __name__ == '__main__':
    spark = SparkSession.builder.appName('udf_define').master('local[*]').getOrCreate()
    sc = spark.sparkContext

    # 假设 有三个数字： 1 2 3 在传入数字，返回数字所在序号对应的 字母 然后和数字结合组成dict返回
    # 例：传入1 返回{'num':1, 'letters': 'a'}
    rdd = sc.parallelize([[1], [2], [3]])
    df = rdd.toDF(['num'])

    # 注册UDF
    def process(data):
        return {'num': data, 'letters': string.ascii_letters[data]}

    '''
    UDF返回值是字典的话，需要用StructType来接收
    '''
    udf1 = spark.udf.register('udf1', process, StructType().add('num', IntegerType(), nullable=True).\
                              add('letters', StringType(), nullable=True))
    # SQL风格
    df.selectExpr('udf1(num)').show(truncate=False)
    # DSL风格
    df.select(udf1(df['num'])).show(truncate=False)

