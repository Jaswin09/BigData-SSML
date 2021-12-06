	
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
from sklearn.metrics import confusion_matrix
sc = SparkContext.getOrCreate()
sc.setLogLevel("OFF")
ssc = StreamingContext(sc, 1)
spark=SparkSession(sc)
data = ssc.socketTextStream("localhost", 6100)
print(data)

confnb=[[0,0],[0,0]]
confperc=[[0,0],[0,0]]
confpac=[[0,0],[0,0]]
try:
	def stream_read(rdd):
		df=spark.read.json(rdd)
		if(not df.rdd.isEmpty()):
			df = preprocess_transform(df)
			x,y=features(df)
			
			with open('nb_model1','rb') as f1:
				lr1 = pickle.load(f1)
			y_pred1 = lr1.predict(x)
			acc1 = accuracy_score(y,y_pred1)
			conf1=confusion_matrix(y,y_pred1)
			for i in range(len(conf1)):
				for j in range(len(conf1[i])):
					confnb[i][j]+=conf1[i][j]
			print('NB :',acc1,confnb)
			
			
			with open('perc_model1','rb') as f2:
				lr2 = pickle.load(f2)
			y_pred2 = lr2.predict(x)
			acc2 = accuracy_score(y,y_pred2)
			conf2=confusion_matrix(y,y_pred2)
			for i in range(len(conf2)):
				for j in range(len(conf2[i])):
					confperc[i][j]+=conf2[i][j]
			print('PERC :',acc2,confperc)
			
			
			with open('pac_model1','rb') as f3:
				lr3 = pickle.load(f3)
			y_pred3 = lr3.predict(x)
			acc3 = accuracy_score(y,y_pred3)
			conf3=confusion_matrix(y,y_pred3)
			for i in range(len(conf3)):
				for j in range(len(conf3[i])):
					confpac[i][j]+=conf3[i][j]
			print('PAC :',acc3,confpac)
			
			
			with open('nb200','a') as f4:
				f4.write(str(acc1)+'\n')
				f4.write(str(confnb)+'\n')
			with open('perc200','a') as f5:
				f5.write(str(acc2)+'\n')
				f5.write(str(confperc)+'\n')
			with open('pac200','a') as f6:
				f6.write(str(acc3)+'\n')
				f6.write(str(confpac)+'\n')
		
		
except Exception as e:
	print(e)		


try:
	data.foreachRDD(lambda rdd: stream_read(rdd))
	
except Exception as e:
	print(e)

ssc.start()
time.sleep(5000)
ssc.stop(stopSparkContext=False)

