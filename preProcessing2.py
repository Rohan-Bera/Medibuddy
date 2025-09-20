#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from collections import Counter


# In[2]:


columns = ['Disease', 'Gender', 'Age', 'Season', 'Symptom', 'Weight']
data = pd.read_csv('FinalDatasetWithSymptom.csv', names=columns)
data.drop(data.head(2).index, inplace=True)


# In[3]:


symptoms = pd.get_dummies(data.Symptom)
diseases = data['Disease']
genders = pd.get_dummies(data.Gender)
age = pd.get_dummies(data.Age)
season = pd.get_dummies(data.Season)


# Preparing symptom table for final csv file

# In[4]:


symptomTable = pd.concat([diseases, symptoms], axis=1)

symptomTable.drop_duplicates(keep='first', inplace=True)
symptomTable = symptomTable.groupby(['Disease'], sort=False).sum()
symptomTable = symptomTable.reset_index()


# Preparing gender table for final csv file

# In[5]:


def createTableWithGender(disease, gender):
    newTable = pd.concat([disease, gender], axis=1)
    newTable.drop_duplicates(keep='first', inplace=True)

    newTable['Female'] = np.where((newTable['Nutral'] == 1), newTable['Nutral'], newTable['Female'])
    newTable['Male'] = np.where((newTable['Nutral'] == 1), newTable['Nutral'], newTable['Male'])

    newTable = newTable.drop(['Nutral'], axis=1)
    
    print(newTable.head(5), end='\n')
    return newTable


# In[6]:


genderTable = createTableWithGender(diseases, genders)


# Preparing age table for final csv file

# In[7]:


def createTableWithAge(disease, age):
    newTable = pd.concat([disease, age], axis=1)
    newTable.drop_duplicates(keep='first', inplace=True)

    newTable['middle-age'] = np.where((newTable['3rd-4th-5th decade of early age'] == 1), newTable['3rd-4th-5th decade of early age'], newTable['middle-age'])
    newTable['older adult'] = np.where((newTable['3rd-4th-5th decade of early age'] == 1), newTable['3rd-4th-5th decade of early age'], newTable['older adult'])

    newTable['adolescene'] = np.where((newTable['9-15 and old age'] == 1), newTable['9-15 and old age'], newTable['adolescene'])
    newTable['early-old'] = np.where((newTable['9-15 and old age'] == 1), newTable['9-15 and old age'], newTable['early-old'])
    newTable['old'] = np.where((newTable['9-15 and old age'] == 1), newTable['9-15 and old age'], newTable['old'])

    newTable['early-old'] = np.where((newTable['>60'] == 1), newTable['>60'], newTable['early-old'])
    newTable['old'] = np.where((newTable['>60'] == 1), newTable['>60'], newTable['old'])

    newTable['early-old'] = np.where((newTable['childrens and old age group'] == 1), newTable['childrens and old age group'], newTable['early-old'])
    newTable['old'] = np.where((newTable['childrens and old age group'] == 1), newTable['childrens and old age group'], newTable['old'])
    newTable['child'] = np.where((newTable['childrens and old age group'] == 1), newTable['childrens and old age group'], newTable['child'])

    newTable['older adult'] = np.where((newTable['increases with age but most likely after 40'] == 1), newTable['increases with age but most likely after 40'], newTable['older adult'])
    newTable['early-old'] = np.where((newTable['increases with age but most likely after 40'] == 1), newTable['increases with age but most likely after 40'], newTable['early-old'])
    newTable['old'] = np.where((newTable['increases with age but most likely after 40'] == 1), newTable['increases with age but most likely after 40'], newTable['old'])
    
    newTable['older adult'] = np.where((newTable['increases with age mostly after 45'] == 1), newTable['increases with age mostly after 45'], newTable['older adult'])
    newTable['early-old'] = np.where((newTable['increases with age mostly after 45'] == 1), newTable['increases with age mostly after 45'], newTable['early-old'])
    newTable['old'] = np.where((newTable['increases with age mostly after 45'] == 1), newTable['increases with age mostly after 45'], newTable['old'])
    
    newTable['child'] = np.where((newTable['less then 50'] == 1), newTable['less then 50'], newTable['child'])
    newTable['adolescene'] = np.where((newTable['less then 50'] == 1), newTable['less then 50'], newTable['adolescene'])
    newTable['adult'] = np.where((newTable['less then 50'] == 1), newTable['less then 50'], newTable['adult'])
    newTable['middle-age'] = np.where((newTable['less then 50'] == 1), newTable['less then 50'], newTable['middle-age'])
    
    newTable['middle-age'] = np.where((newTable['middle age - old age group'] == 1), newTable['middle age - old age group'], newTable['middle-age'])
    newTable['older adult'] = np.where((newTable['middle age - old age group'] == 1), newTable['middle age - old age group'], newTable['older adult'])
    newTable['early-old'] = np.where((newTable['middle age - old age group'] == 1), newTable['middle age - old age group'], newTable['early-old'])
    newTable['old'] = np.where((newTable['middle age - old age group'] == 1), newTable['middle age - old age group'], newTable['old'])
    
    newTable['infant'] = np.where((newTable['no effect'] == 1), newTable['no effect'], newTable['infant'])
    newTable['child'] = np.where((newTable['no effect'] == 1), newTable['no effect'], newTable['child'])
    newTable['adolescene'] = np.where((newTable['no effect'] == 1), newTable['no effect'], newTable['adolescene'])
    newTable['adult'] = np.where((newTable['no effect'] == 1), newTable['no effect'], newTable['adult'])
    newTable['middle-age'] = np.where((newTable['no effect'] == 1), newTable['no effect'], newTable['middle-age'])
    newTable['older adult'] = np.where((newTable['no effect'] == 1), newTable['no effect'], newTable['older adult'])
    newTable['early-old'] = np.where((newTable['no effect'] == 1), newTable['no effect'], newTable['early-old'])
    newTable['old'] = np.where((newTable['no effect'] == 1), newTable['no effect'], newTable['old'])
    
    newTable['adolescene'] = np.where((newTable['young - middle age group'] == 1), newTable['young - middle age group'], newTable['adolescene'])
    newTable['adult'] = np.where((newTable['young - middle age group'] == 1), newTable['young - middle age group'], newTable['adult'])
    newTable['middle-age'] = np.where((newTable['young - middle age group'] == 1), newTable['young - middle age group'], newTable['middle-age'])
    
    newTable = newTable.drop(['3rd-4th-5th decade of early age'], axis=1)    
    newTable = newTable.drop(['9-15 and old age'], axis=1)
    newTable = newTable.drop(['>60'], axis=1)
    newTable = newTable.drop(['childrens and old age group'], axis=1)
    newTable = newTable.drop(['increases with age but most likely after 40'], axis=1)    
    newTable = newTable.drop(['increases with age mostly after 45'], axis=1)
    newTable = newTable.drop(['less then 50'], axis=1)
    newTable = newTable.drop(['middle age - old age group'], axis=1)
    newTable = newTable.drop(['no effect'], axis=1)    
    newTable = newTable.drop(['young - middle age group'], axis=1)

    print(newTable.head(5), end='\n')
    return newTable


# In[8]:


ageTable = createTableWithAge(diseases, age)


# Preparing season table for final csv file

# In[9]:


def createTableWithSeason(disease, season):
    newTable = pd.concat([disease, season], axis=1)
    newTable.drop_duplicates(keep='first', inplace=True)

    newTable['winter'] = np.where((newTable['any season'] == 1), newTable['any season'], newTable['winter'])
    newTable['summer'] = np.where((newTable['any season'] == 1), newTable['any season'], newTable['summer'])
    newTable['autumn'] = np.where((newTable['any season'] == 1), newTable['any season'], newTable['autumn'])
    newTable['spring'] = np.where((newTable['any season'] == 1), newTable['any season'], newTable['spring'])
    
    newTable['winter'] = np.where((newTable['winter-spring'] == 1), newTable['winter-spring'], newTable['winter'])
    newTable['spring'] = np.where((newTable['winter-spring'] == 1), newTable['winter-spring'], newTable['spring'])
    
    newTable['spring'] = np.where((newTable['spring-summer'] == 1), newTable['spring-summer'], newTable['spring'])
    newTable['summer'] = np.where((newTable['spring-summer'] == 1), newTable['spring-summer'], newTable['summer'])
    
    newTable['summer'] = np.where((newTable['summer-autumn'] == 1), newTable['summer-autumn'], newTable['summer'])
    newTable['autumn'] = np.where((newTable['summer-autumn'] == 1), newTable['summer-autumn'], newTable['autumn'])
    
    newTable['summer'] = np.where((newTable['low of winters and high of summers'] == 1), newTable['low of winters and high of summers'], newTable['summer'])
    newTable['winter'] = np.where((newTable['low of winters and high of summers'] == 1), newTable['low of winters and high of summers'], newTable['winter'])

    newTable = newTable.drop(['any season'], axis=1)
    newTable = newTable.drop(['winter-spring'], axis=1)
    newTable = newTable.drop(['spring-summer'], axis=1)
    newTable = newTable.drop(['summer-autumn'], axis=1)
    newTable = newTable.drop(['low of winters and high of summers'], axis=1)
    
    print(newTable.head(5), end='\n')
    return newTable


# In[10]:


seasonTable = createTableWithSeason(diseases, season)


# Prepearing Final CSV file

# In[11]:


finalTable = pd.merge(genderTable, ageTable, on='Disease')
finalTable = pd.merge(finalTable, seasonTable, on='Disease')
finalTable = pd.merge(finalTable, symptomTable, on='Disease')
print(finalTable.head(5), end='\n')


# In[12]:


finalTable.to_csv('finalTable.csv', index=False)


# In[ ]:




