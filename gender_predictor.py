import matplotlib.pyplot as plt
import pandas as pd
from mlxtend.plotting import plot_decision_regions
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn import datasets
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
Y = []
#print(age)
for i in range(len(age)):
	if gender[i] == 'Male':
		Y.append(1)
	else:
		Y.append(0)

kid = df['Kids']
kid = kid.fillna(0) #fill NaN with zero kids
kid = list(kid.astype(int))  #convert float to int values 
X = list(zip(age,kid))


x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.3,random_state=11)
#print(x_train)

print("KNN RUN")
clf2 = KNeighborsClassifier(n_neighbors=5)
clf2.fit(x_train,y_train)
pf2 = clf2.predict(x_test)
print("Accuracy of prediction in percentage ", accuracy_score(y_test,pf2)*100)
print(classification_report(y_test,pf2))


# #Plotting decision region
# plot_decision_regions(np.array(x_train), np.array(y_train), clf=clf2, legend=2)
# plt.xlabel("Age")
# plt.ylabel("Children")
# plt.title("SVM")
# plt.show()


agi = int(input("Enter the age of the person: (MUST BE ABOVE 16)\n"))
geni = int(input("Enter the number of children the person wants to have\n"))

res = clf2.predict([[agi,geni]])
if res == 1:
	print("Probably a male")
else:
	print("Probably a female")
