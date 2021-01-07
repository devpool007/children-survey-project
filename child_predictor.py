import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from mlxtend.plotting import plot_decision_regions
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report,confusion_matrix,f1_score
from scipy import sparse
sns.set()
sns.set_style({'axes.grid' : True})

df = pd.read_csv("survey_mk2.csv")

age = df['Age']
gender = df['Gender']
#Replace Male with 1 int value and Female with 0 int value
gen = []
#print(age)
for i in range(len(age)):
	if gender[i] == 'Male':
		gen.append(1)
	else:
		gen.append(0)
# vectorizer = TfidfVectorizer()
# gen = vectorizer.fit_transform(gender)
# print(type(gen))
# print(gen.shape)
# age = sparse.csr_matrix(age)
# age = age.transpose()
# print(age.shape)
#X = sparse.hstack([age,gen])

X = list(zip(age,gen))
X = np.array(X)
Y = df['Kids']
Y = Y.fillna(0) #fill NaN with zero kids
Y = list(Y.astype(int))  #convert float to int values 
#make it as if having kids or not having as data very less rn for multi classification
for i in range(len(age)):
	if Y[i] > 0:
		Y[i] = 1
Y = np.array(Y)

x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.3,random_state=101)
#print(x_train)


clf = SVC(class_weight={0:1.5,1:1.3})
clf.fit(x_train,y_train)

pf = clf.predict(x_test)
print("SVM RUN")
print("Accuracy of prediction in percentage ", accuracy_score(y_test,pf)*100)
print(classification_report(y_test,pf))


print("KNN RUN")
clf2 = KNeighborsClassifier(n_neighbors=3)
clf2.fit(x_train,y_train)
pf2 = clf2.predict(x_test)
print("Accuracy of prediction in percentage ", accuracy_score(y_test,pf2)*100)
print(classification_report(y_test,pf2))

# Plotting decision region
plot_decision_regions(X, Y, clf=clf2, legend=2)
# Adding axes annotations
plt.xlabel("Age")
plt.ylabel("Gender")
plt.title("KNN")
plt.show()



agi = int(input("Enter the age of the person:\n"))
geni = int(input("Enter 0 if the gender of person is FEMALE and 1 if it's MALE\n"))

res = clf2.predict([[agi,geni]])
if res == 1:
	print("Probably will have kids")
else:
	print("Probably won't have kids")