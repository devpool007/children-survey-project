import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
sns.set()
sns.set_style({'axes.grid' : True})


df = pd.read_csv("survey_mk2.csv")

age = df['Age'].value_counts()
age = age.sort_index()
#print(age.keys())
fig, ax = plt.subplots()
# labels = ['15', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32',
#             '33', '34', '35', '36', '37', '40', '59']
labels = age.keys()
ax.bar(labels,age)
plt.title("Age Demographic in survey",fontsize=22)
plt.xlabel("Age",fontsize = 22)
plt.ylabel("Number of entries",fontsize = 22)
plt.yticks(np.arange(0, 21, step=2),fontsize=20)
plt.xticks(fontsize = 20)
plt.show()