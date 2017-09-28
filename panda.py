
# coding: utf-8

# In[286]:

from pandas import DataFrame, read_csv 
import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib 


# In[287]:

print('Python version'+sys.version)
print('Pandas ver'+pd.__version__)
print('Matplotlib ver'+matplotlib.__version__)


# In[288]:

names = ['bob','Abi','Jatzet','Notengonickfull','Cami']
births=[90,55,82,23,45]
BabyDataSet=list(zip(Names,Births))
BabyDataSet


# In[290]:
df=pd.DataFrame(data=BabyDataSet,columns=['Names','Births'])
df


# In[184]:
df.to_csv('Birthsfile.csv',index=False,header=False)

# In[292]:

Location=r'/home/jatzet/Birthsfile.csv'
df=pd.read_csv(Location)
df=pd.read_csv(Location,header = None)
df=pd.read_csv(Location,names=['Names','Births'])


# In[294]:
import os
os.remove(Location)


# In[295]:
Sorted = df.sort_values(['Births'],ascending=False)
Sorted.head(1)
df['Births'].max()


# In[299]:
df['Births'].plot()
MaxValues=df['Births'].max()
MaxName=df['names'][df['Births']==df['Births'].max()].values
Text=str(MaxValue)+"_"+MaxName

# In[304]:

plt.annotate(Text,xy=(1,MaxValue),xytext=(8,0),xycoords=('axes fraction','data'),textcoords='offset points')
print("The most popular name")
df[df['births']==df['births'].max()]

