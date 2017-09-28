
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
BabyDataSet=list(zip(names,births))
BabyDataSet


# In[290]:
df=pd.DataFrame(data=BabyDataSet,columns=['names','births'])
df


# In[184]:
df.to_csv('birthsfile.csv',index=False,header=False)

# In[292]:

Location=r'/home/jatzet/birthsfile.csv'
df=pd.read_csv(Location)
df=pd.read_csv(Location,header = None)
df=pd.read_csv(Location,names=['names','births'])


# In[294]:
import os
os.remove(Location)


# In[295]:
Sorted = df.sort_values(['births'],ascending=False)
Sorted.head(1)
df['births'].max()


# In[299]:
df['births'].plot()
MaxValues=df['births'].max()
MaxName=df['names'][df['births']==df['births'].max()].values
Text=str(MaxValue)+"_"+MaxName

# In[304]:

plt.annotate(Text,xy=(1,MaxValue),xytext=(8,0),xycoords=('axes fraction','data'),textcoords='offset points')
print("The most popular name")
df[df['births']==df['births'].max()]

