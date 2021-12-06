
import time
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from preprocess import *
from pyspark.sql import SparkSession
import re
from pyspark.sql.functions import col,lower, regexp_replace, udf
from pyspark.sql.types import StringType
from models import *
from model_train import *
from feature_extract import *
sc = SparkContext.getOrCreate()
#sc.setLogLevel("OFF")
ssc = StreamingContext(sc, 1)
spark=SparkSession(sc)
data = ssc.socketTextStream("localhost", 6100)
print(data)

try:
	def readMyStream(rdd):
		df=spark.read.json(rdd)
		if(not df.rdd.isEmpty()):
			df=preprocess_transform(df)
			x,y=features(df)
			model_train(x,y)
			print()
		
		
except Exception as e:
	print(e)		


try:
	data.foreachRDD(lambda rdd: readMyStream(rdd))
	
except Exception as e:
	print(e)

ssc.start()
time.sleep(5000)
ssc.stop(stopSparkContext=False)

