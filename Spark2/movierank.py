from __future__ import print_function
import sys
import re
import string
from operator import add
from pyspark.sql import SparkSession





if __name__ == "__main__":


    spark = SparkSession \
        .builder \
        .appName("PythonWordCount") \
        .getOrCreate()
    print("hello world")

    spark.stop()