import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'axes.grid' : False})


df = pd.read_csv("survey.csv")

cunt = df['Country'].value_counts()

fig, ax = plt.subplots()
#ax = fig.add_axes([0,0,1,1])
labels = ['South Africa','India','Germany' ,'Poland', 'Romania' ,'United States'     
,'Indonesia', 
'Philippines',               
'Hungary',           
'Norway' ,           
'France' ,           
'Brazil' ,           
'Netherlands',       
'Saudi Arabia',      
'Spain',             
'Denmark' ,          
'Argentina' ,        
'Canada' ,            
'Bangladesh' ,        
'Yugoslavia',         
'Lithuania' ,         
'Czech Republic' ,             
'Tunisina' ,          
'Colombia',          
'Finland' ,          
'Guatemala',         
'Azerbaijan',        
'Russia' ,           
'Italy',             
'Canadia',           
'Austria',           
'England' ,                 
'Greece',            
'Kosovo' ,           
'Estonia' ,          
'Slovakia',          
'Chile',             
'Hungary',           
'Malaysia',          
'Iraq' ,             
'Portugal',          
'Iran',              
'Moldova',           
'Slovenia']

ax.bar(labels,cunt)
plt.xlabel("Country",fontsize = 28)
plt.ylabel("Number of entries",fontsize = 28)
plt.show()