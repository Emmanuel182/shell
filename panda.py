
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

names=['Bob', 'Cam', 'Kate','Kendra','Abi']
births=[915,52,32,83,15]
age=[11,22,33,44,55,66]


# In[290]:

BabyDataSet=list(zip(names,births))
BabyDataset2=list(zip(names,age))


# In[184]:

BabyDataSet


# In[292]:

BabyDataset2


# In[294]:

df = pd.DataFrame(data = BabyDataSet, columns = ['Names ', 'Births'])
df


# In[295]:

df.to_csv('birthsfile.csv',index=False,header=False)



# In[299]:

Location=r'/home/jatzet/birthsfile.csv'


# In[304]:

Location=r'/home/jatzet/birthsfile.csv'
df = pd.read_csv(Location)


# In[305]:

df


# In[334]:

df = pd.read_csv(Location, header=None)
df


# In[333]:

df=pd.read_csv(Location)
df 


# In[335]:

df.dtypes
df.Births.dtype



# In[336]:

sorted=df.sort_values(['Births'],ascending= False)
sorted.head(1)
df['Births'].max()


# In[ ]:

df['Births'].plot()
MaxValue=df['Births'].max()
MaxName=df['Names'][df['Births']==df['Births'].max()].values
Text=str(MaxValue)+ "_" +MaxName


# In[ ]:

plt.annotate(Text,xy=(1,MaxValue), xytext=(8,0),xycoords=('axes fraction', 'data'),textcoords ='off set points')


# In[337]:

print("The most popular name")
df[df['Births']==df['Births'].max()]

