import sys
from pyspark import SparkContext, SparkConf
conf = SparkConf()
stopwords = ["they","she","he","it","the","as","is","and"]
# create Spark context with necessary configuration
sc = SparkContext.getOrCreate(conf=conf)
# Conduct MapReduce and write the output to folder
wordCounts = sc.wholeTextFiles("./testData").flatMap(lambda file_contents: [(file_contents[0], word) for word in file_contents[1].lower().split(" ")]) \
.map(lambda file_word: (file_word[1], (1, file_word[0]))).reduceByKey(lambda x, y: (x[0]+y[0], y[1])) \
.coalesce(1).saveAsTextFile("./output")
 # .filter(lambda file_word: file_word[0] not in stopwords)\
# .reduceByKey(lambda a,b:a + b).map(lambda file_word: (file_word[1],1)).reduceByKey(lambda a,b:a + b) \    
sc.stop()