
# import module 
from pyspark.sql import SparkSession

# Arif 2021-07-24 V1 "basic program to read file and count"
# Require Haddop integration with Spark if you want to read file from hadoop 

# run option-1:
# Use spark-submit to run your application
# $ YOUR_SPARK_HOME/bin/spark-submit --master local[4] SimpleApp.py
# $ /usr/local/src/spark/bin/spark-submit --master local[4] SimpleApp.py

# run option-2:
# python SimpleApp.py

# output: Lines with a: 64, lines with b: 32 


# reading from hadoop path
# logFile = "Spark-README.md"  # Should be some file on hadoop fs

# reading from local file system
logFile = "file:///usr/local/src/spark/README.md"  # Should be some file on your system


spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
logData = spark.read.text(logFile).cache()

numAs = logData.filter(logData.value.contains('a')).count()
numBs = logData.filter(logData.value.contains('b')).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

spark.stop()




