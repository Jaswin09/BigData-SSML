import pickle
from sklearn.linear_model import Perceptron
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.model_selection import train_test_split
from sklearn.cluster import MiniBatchKMeans
import numpy as np
def model_train(x,y):
	#x=df.select('vectors').rdd.flatMap(lambda x: x).collect()
	#y=df.select('sentiment').rdd.flatMap(lambda x: x).collect()
	#x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
	nb=MultinomialNB()
	clf = SGDClassifier(loss='hinge',penalty='l2')
	pac = PassiveAggressiveClassifier(max_iter=1000, random_state=0,tol=1e-3)
	model = Perceptron()
	
	nb.partial_fit(x,y,classes=np.unique(y))
	#y_pred1=nb.predict(x_test)
	#acc1=accuracy_score(y_test,y_pred1)
	print("MNB")
	
	#clf.partial_fit(x,y,classes=np.unique(y))
	#y_pred2=clf.predict(x_test)
	#acc2=accuracy_score(y_test,y_pred2)
	#print("SGD")
	
	model.partial_fit(x,y,classes=np.unique(y))
	#y_pred3=model.predict(x_test)
	#acc3=accuracy_score(y_test,y_pred3)
	print("PERC")
	
	pac.partial_fit(x,y,classes=np.unique(y))
	#y_pred4=pac.predict(x_test)
	#acc4=accuracy_score(y_test,y_pred4)
	print("PAC")
	
	f1="nb_model2"
	#f2="clf_model"
	f3="perc_model2"
	f4="pac_model2"
	
	pickle.dump(nb,open(f1,'wb'))
	#pickle.dump(clf,open(f2,'wb'))
	pickle.dump(pac,open(f3,'wb'))
	pickle.dump(model,open(f4,'wb'))
	
def clustering(x):
	kmeans = MiniBatchKMeans(n_clusters=2,random_state=0)
	kmeans = kmeans.partial_fit(x)
	f="kmeans_model"
	pickle.dump(kmeans,open(f,'wb'))

