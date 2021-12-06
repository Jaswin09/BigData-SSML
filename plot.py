import matplotlib.pyplot as plt

nb=[]
pac=[]
perc=[]
with open('nb','r') as f:
	for i in f:
		if i:
			nb.append(float(i.strip()))
				
with open('pac','r') as f:
	for i in f:
		if i:
			pac.append(float(i.strip()))
				
with open('perc','r') as f:
	for i in f:
		if i:
	
			perc.append(float(i.strip()))

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
	
lineplot()
barplot()
