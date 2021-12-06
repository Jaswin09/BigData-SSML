	
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
	def stream_read(rdd):
		df=spark.read.json(rdd)
		if(not df.rdd.isEmpty()):
			df = preprocess_transform(df)
			x,y=features(df)
			
			with open('nb_model2','rb') as f1:
				lr1 = pickle.load(f1)
			y_pred1 = lr1.predict(x)
			acc1 = accuracy_score(y,y_pred1)
			print('NB :',acc1)
			
			
			with open('perc_model2','rb') as f2:
				lr2 = pickle.load(f2)
			y_pred2 = lr2.predict(x)
			acc2 = accuracy_score(y,y_pred2)
			print('PERC : ',acc2)
			
			
			with open('pac_model2','rb') as f3:
				lr3 = pickle.load(f3)
			y_pred3 = lr3.predict(x)
			acc3 = accuracy_score(y,y_pred3)
			print('PAC :',acc3)
			
			
			with open('nb','a') as f4:
				f4.write(str(acc1)+'\n')
			with open('perc','a') as f5:
				f5.write(str(acc2)+'\n')
			with open('pac','a') as f6:
				f6.write(str(acc3)+'\n')
		
		
except Exception as e:
	print(e)		


try:
	data.foreachRDD(lambda rdd: stream_read(rdd))
	
except Exception as e:
	print(e)

ssc.start()
time.sleep(5000)
ssc.stop(stopSparkContext=False)

