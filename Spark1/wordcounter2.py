from __future__ import print_function
import sys
import re
import string
from operator import add
from pyspark.sql import SparkSession


def clean1(word):
    word = word.lower()
    if any(char.isdigit() for char in word): # if it contains a letter
        return []
    if len(word) == 0:
        return []
    if word[0] in string.punctuation:
        word = word[1:]
    if len(word) == 0:
        return []
    if word[len(word) - 1] in string.punctuation:
        word = word[:len(word)-1]
    if len(word) == 0:
        return []
    return [word]
        
    

file1 = open("output.txt","w")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)
    spark = SparkSession\
        .builder\
        .appName("PythonWordCount")\
        .getOrCreate()
    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])
    counts = lines.flatMap(lambda x: x.split(' ')).flatMap(clean1) \
        .map(lambda x: (x, 1)) \
        .reduceByKey(add).sortBy(lambda x: x[1], 0)
    output = counts.collect()
    for (word, count) in output:
        file1.write("%s: %i\n" % (word, count))

file1.close() 
spark.stop()