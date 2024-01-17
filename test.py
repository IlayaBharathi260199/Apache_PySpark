from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder \
    .appName("MySparkSession") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# Test the Spark session
spark.range(5).show()
