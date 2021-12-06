from pyspark.sql.functions import *
from pyspark.ml.feature import *
from nltk.stem import PorterStemmer
from pyspark.ml.classification import NaiveBayes
from pyspark.sql.types import *
import re
import ast
ps=PorterStemmer()
def preprocess_transform(df):
	noise=lambda x:re.sub(r"[^a-zA-Z\s]",'',x)
	spaces=lambda x:re.sub(r'\s\s+',' ',x,flags=re.I) 
	ste=lambda x: [ps.stem(i.strip()) for i in ast.literal_eval(str(x))]
	
	df=df.withColumn('tweet1',trim(df.tweet))
	df=df.withColumn('tweet1',udf(noise,StringType())('tweet1'))
	df=df.withColumn('tweet1',udf(spaces,StringType())('tweet1'))
	df=df.withColumn('sentiment', when(df.sentiment.endswith('4'),regexp_replace(df.sentiment,'4','1'))\
	.when(df.sentiment.endswith('0'),regexp_replace(df.sentiment,'0','0')).cast(IntegerType()))
	df = Tokenizer(inputCol='tweet1', outputCol='words').transform(df)
	df = StopWordsRemover(inputCol="words", outputCol="filtered").transform(df)
	df=df.withColumn('stemmed',udf(ste,ArrayType(StringType()))('filtered'))
	
	
	#df.show()
	return df
