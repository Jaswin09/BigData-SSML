import matplotlib.pyplot as plt
import json
import numpy as np
nb=[]
pac=[]
perc=[]
with open('nb200','r') as f:
	c=f.readlines()
	for i in range(0,len(c),2):
		nb.append(float(c[i].strip()))	
	l1=json.loads(c[-1])
			
with open('pac200','r') as f:
	c=f.readlines()
	for i in range(0,len(c),2):
		pac.append(float(c[i].strip()))
	l2=json.loads(c[-1])
				
with open('perc200','r') as f:
	c=f.readlines()
	for i in range(0,len(c),2):
		perc.append(float(c[i].strip()))
	l3=json.loads(c[-1])
	
def lineplot():
	#print(nb,pac,perc)
	batch=[i for i in range(len(nb))]

	plt.plot(batch,nb,label="NaiveBayes")
	plt.plot(batch,pac,label="PassiveAggressiveClassifier")
	plt.plot(batch,perc,label="Perceptron")
	plt.xlabel("Batches")
	plt.ylabel("Accuracy")
	plt.title("Classifier Comparison")
	plt.legend()
	plt.show()


def barplot():
	s1=0
	s2=0
	s3=0
	for i in nb:
		s1+=i
	avg1=(s1/len(nb))
	for i in pac:
		s2+=i
	avg2=(s2/len(pac))
	for i in perc:
		s3+=i
	avg3=(s3/len(perc))
	print(avg1,avg2,avg3)
	l = {'NaiveBayes':avg1
	     ,'PassiveAggressiveClassifier':avg2
	     ,'Perceptron':avg3}

	b=list(l.keys())
	avg=list(l.values())

	fig=plt.figure(figsize=(10,5))

	plt.bar(b,avg,color="red",width=0.4)
	plt.xlabel("Batches")
	plt.ylabel("Accuracy")
	plt.title("Classifier Comparison")
	plt.show()

def total_metrics():
	s1=0
	s2=0
	s3=0
	for i in range(len(l1)):
		for j in range(len(l1[i])):
			s1+=l1[i][j]
			s2+=l2[i][j]
			s3+=l3[i][j]
	X=['MUltinomialNB','PassiveAggressiveClassifier','Perceptron']
	
	acc1=(l1[0][0]+l1[1][1])/s1
	acc2=(l2[0][0]+l2[1][1])/s2
	acc3=(l3[0][0]+l3[1][1])/s3
	
	rec1=l1[0][0]/(l1[0][0]+l1[0][1])
	rec2=l2[0][0]/(l2[0][0]+l2[0][1])
	rec3=l3[0][0]/(l3[0][0]+l3[0][1])
	
	pre1=l1[0][0]/(l1[0][0]+l1[1][0])
	pre2=l2[0][0]/(l2[0][0]+l2[1][0])
	pre3=l3[0][0]/(l3[0][0]+l3[1][0])
	
	acc=[acc1,acc2,acc3]
	rec=[rec1,rec2,rec3]
	pre=[pre1,pre2,pre3]
	
	X_axis=np.arange(len(acc))
	plt.bar(X_axis,acc,0.1,label="accuracy")
	plt.bar(X_axis+0.1,rec,0.1,label="recall")
	plt.bar(X_axis-0.1,pre,0.1,label="precision")
	
	plt.xticks(X_axis,X)
	plt.xlabel("Classifiers")
	plt.ylabel("metrics")
	plt.title("Classifier Comparison")
	plt.legend()
	plt.show()

	print(acc1,acc2,acc3)
	
	
lineplot()
barplot()
total_metrics()
