import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
sns.set()
sns.set_style({'axes.grid' : True})

df = pd.read_csv("survey_mk2.csv")

age = df['Age']
gender = df['Gender']
#Replace Male with 1 int value and Female with 0 int value
gen = []
for i in range(len(age)):
	if gender[i] == 'Male':
		gen.append(1)
	else:
		gen.append(0)


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

x_train = x_train.astype("float32")
x_test = x_test.astype("float32")
y_train = y_train.astype("float32")
y_test = y_test.astype("float32")

# define the keras model
model = Sequential()
model.add(Dense(10, input_dim=2, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit the keras model on the dataset
model.fit(x_train, y_train, epochs=200, batch_size=10,verbose = 0)


# evaluate the keras model
accuracy = model.evaluate(x_test, y_test)
print("test acc:", accuracy[1]*100)

# agi = int(input("Enter the age of the person:\n"))
# geni = int(input("Enter 0 if the gender of person is FEMALE and 1 if it's MALE\n"))

# res = clf2.predict([[agi,geni]])
# if res == 1:
# 	print("Probably will have kids")
# else:
# 	print("Probably won't have kids")