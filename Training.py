#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
import pydotplus


# In[2]:


finalFile = pd.read_csv('finalTable.csv')
final_symptoms = finalFile.columns[1:].values


#  Saving the symptoms in a file 

# In[3]:


filename = 'myModel.sav'
pickle.dump(final_symptoms, open(filename, 'wb'))


# In[4]:


x = finalFile[finalFile.columns[1:]]
y = finalFile['Disease']


# ### Training the Model Using Multinomial Neive Bayes Algorithm

# In[5]:


from sklearn.naive_bayes import MultinomialNB
mnb = MultinomialNB()
mnb.fit(x, y)
print('The Accuracy achieved:', mnb.score(x,y)*100,"%", '\n')


# Model Faileure

# In[6]:


disease_pred = mnb.predict(x)
disease_real = y.values

for i in range(len(disease_real)):
        if disease_pred[i] != disease_real[i]:
            print('Pred:',disease_pred[i])
            print('Actual:',disease_real[i])
            print('')


# Saving the trained model

# In[7]:


filename = 'mnb_model.sav'
pickle.dump(mnb, open(filename, 'wb'))


# ### Training the Model Using Decision Tree

# In[8]:


from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

dtree = DecisionTreeClassifier()
dtree = dtree.fit(x, y)
print('The Accuracy achieved:', dtree.score(x,y)*100,"%", '\n')


# In[9]:


data = tree.export_graphviz(dtree, max_depth = 5)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')

img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()


# In[10]:


disease_pred = dtree.predict(x)
disease_real = y.values

for i in range(len(disease_real)):
        if disease_pred[i] != disease_real[i]:
            print('Pred:',disease_pred[i])
            print('Actual:',disease_real[i])
            print('')


# In[11]:


filename = 'dTree_model.sav'
pickle.dump(mnb, open(filename, 'wb'))

