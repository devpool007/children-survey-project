import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'axes.grid' : False})

df = pd.read_csv("survey_mk2.csv")

gender = df['Gender']

male_nobby = []
female_nobby = []
# print(gender[0])
for i in gender:
	if(gender is 'Male' and df['']):














	
fig1,ax1 = plt.subplots(figsize =(15, 7))
ax1.pie(gender, labels=labels, autopct='%1.1f%%',startangle=90)
ax1.axis('equal')
plt.show()



