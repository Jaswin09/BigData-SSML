from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.ml.feature import *
from nltk.stem import PorterStemmer
import re
import ast
import json
ps=PorterStemmer()
sc=SparkContext.getOrCreate()
sc.setLogLevel('OFF')
ssc = StreamingContext(sc,1)
spark=SparkSession(sc)
df=spark.read.json('s.json')
#df.groupBy('sentiment').count().show()
#df1=df.select(split(col('tweet')," ").alias("Tweet"))
#df1.show()
