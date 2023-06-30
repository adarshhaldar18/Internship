#!/usr/bin/env python
# coding: utf-8

# # Importing Necessary libraries

# In[ ]:


#Importing All Required Libaries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from warnings import filterwarnings
filterwarnings(action='ignore')


# In[36]:


df=pd.read_csv(r'C:\Users\lenovo\Desktop\D-S\titanic_train.csv')
df.head()


# In[37]:


df.shape


# In[38]:


#Checking for Null values
df.isnull().sum()


# In[39]:


#Description of dataset
df.describe()


# In[40]:


#Description of dataset
df.describe(include="all")


# In[41]:


df.groupby('Survived').mean()


# In[42]:


df.corr()


# In[43]:


#Droping Useless Columns
df = df.drop(columns=['Ticket','Cabin','Name','PassengerId'], axis = 1)


# In[44]:


#Description of dataset
df.describe(include="all")


# #### Number of males and females

# In[45]:


male = len(df[df['Sex'] == 'male'])
print("No of Males in Titanic:",male)


# In[46]:


female = len(df[df['Sex'] == 'female'])
print("No of Females in Titanic:",female)


# In[47]:


#Plotting
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
gender = ['Male','Female']
index = [577,314]
ax.bar(gender,index)
plt.xlabel("Gender")
plt.ylabel("No of people onboarding ship")
plt.show()


# In[48]:


df.groupby('Sex')[['Survived']].mean()


# #### Alive and dead count

# In[49]:


alive = len(df[df['Survived'] == 1])
dead = len(df[df['Survived'] == 0])


# In[50]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
status = ['Survived','Dead']
ind = [alive,dead]
ax.bar(status,ind)
plt.xlabel("Status")
plt.show()


# ### Survived and cound'nt Survive according to age

# In[51]:


plt.figure(1)
age  = df.loc[df.Survived == 1, 'Age']
plt.title('The histogram of the age groups of the people that had survived')
plt.hist(age, np.arange(0,100,10))
plt.xticks(np.arange(0,100,10))


plt.figure(2)
age  = df.loc[df.Survived == 0, 'Age']
plt.title('The histogram of the age groups of the people that coudn\'t survive')
plt.hist(age, np.arange(0,100,10))
plt.xticks(np.arange(0,100,10))


# ### Filling the values

# In[52]:


#now we have to fill all the missing values
#age have 177  missing values
#either we fill missing values with mean or median form existing values 
df['Age']=df['Age'].fillna(df['Age'].median())
df['Age'].isnull().sum()


# In[53]:


df['Embarked'] = df['Embarked'].fillna(method ='pad')
df['Embarked'].isnull().sum()


# In[54]:


#now we need to convert sex into integer value 
d={'male':0, 'female':1}
df['Sex']=df['Sex'].apply(lambda x:d[x])
df['Sex'].head()


# In[55]:


e={'C':0, 'Q':1 ,'S':2}
df['Embarked']=df['Embarked'].apply(lambda x:e[x])
df['Embarked'].head()


# ### Model construction

# In[59]:



#training values
X=df.drop(columns=['Survived'],axis=1)
#target value
Y=df['Survived']


# In[61]:


#Training Testing and Spliting the model
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3,random_state=7)


# In[62]:


#Using LogisticRegression
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train,Y_train)
Y_pred = model.predict(X_test)

from sklearn.metrics import accuracy_score
print("Accuracy Score:",accuracy_score(Y_test,Y_pred))


# In[63]:


#Using KNN Neighbors
from sklearn.neighbors import KNeighborsClassifier
model2 = KNeighborsClassifier(n_neighbors=5)
model2.fit(X_train,Y_train)
y_pred2 = model2.predict(X_test)

from sklearn.metrics import accuracy_score
print("Accuracy Score:",accuracy_score(Y_test,y_pred2))


# In[66]:


#Using Decision Tree
from sklearn.tree import DecisionTreeClassifier
model4 = DecisionTreeClassifier(criterion='entropy',random_state=7)
model4.fit(X_train,Y_train)
y_pred4 = model4.predict(X_test)

from sklearn.metrics import accuracy_score
print("Accuracy Score:",accuracy_score(Y_test,y_pred4))


# #### Hence I will use Logistic regression model for prediction

# In[ ]:




