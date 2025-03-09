from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("PySparkApp").getOrCreate()

# Create a sample DataFrame
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)

# Show the DataFrame
df.show()

# Save the DataFrame as CSV
df.write.mode("overwrite").csv("/opt/spark-data/output")

df.coalesce(1).write.mode("overwrite").csv("/opt/spark-data/output", header=True)

# Stop Spark session
spark.stop()

# # Map reduce example

# from pyspark.sql import SparkSession

# # Initialize Spark session
# spark = SparkSession.builder.appName("MapReduceExample").getOrCreate()

# # Create an RDD from a sample text file
# rdd = spark.sparkContext.textFile("/opt/spark-data/input/sample.txt")

# # Map: Split lines into words and assign each word a count of 1
# word_counts = rdd.flatMap(lambda line: line.split(" ")) \
#                  .map(lambda word: (word, 1))

# # Reduce: Aggregate counts for each word
# word_counts = word_counts.reduceByKey(lambda a, b: a + b)

# # Collect and print the result
# for word, count in word_counts.collect():
#     print(f"{word}: {count}")

# # Save results to an output file
# word_counts.saveAsTextFile("/opt/spark-data/output/wordcount")

# # Stop Spark session
# spark.stop()
