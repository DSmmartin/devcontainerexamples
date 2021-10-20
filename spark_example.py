def spark_start(task):
    print("Starting Spark")
    spark = pyspark.sql.SparkSession.builder.appName(task) \
                                            .getOrCreate()
    print("Spark configuration")
    print(spark.sparkContext.uiWebUrl)
    print(spark.sparkContext.getConf().getAll())
    print_environment(spark)
    return spark

def print_environment(spark):
    print("Work directory:", os.getcwd())
    print("Files in cd:", os.listdir(os.curdir))
    print ('****************')
    print ('Python version: {}'.format(sys.version))
    print ('Spark version: {}'.format(spark.version))
    print ('****************')

my_spark = spark_start('aibootcamp')
print_environment(my_spark)