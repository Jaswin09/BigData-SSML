from pyspark.sql.functions import *
from pyspark.ml.feature import *
import numpy as np
def features(df):
	hashingTF = HashingTF(inputCol="stemmed", outputCol="rawFeatures", numFeatures=500)
	df = hashingTF.transform(df)
	idf = IDF(inputCol="rawFeatures", outputCol="vectors")
	idfModel = idf.fit(df)
	rescaledData = idfModel.transform(df)
	df = rescaledData.select('sentiment', 'vectors')
	x=df.select('vectors').rdd.flatMap(lambda x: x).collect()
	y=df.select('sentiment').rdd.flatMap(lambda x: x).collect()
	#print(y)
	#x = np.array(df.select('vectors').collect())
	#x=x.reshape(x.shape[0]*x.shape[1],x.shape[2])
	#y = np.array(df.select('sentiment').collect())
	#y=y.flatten()
	print("features extracted")
	return x,y
