#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re


# In[2]:


columns = ['Disease', 'Gender', 'Age', 'Season', 'Symptom', 'Weight']
data = pd.read_csv('DatasetWithSymptom.csv', names=columns)


# Make AGE devision as Following :
# 
# Periods of Human Age
# 
# Childhood: 
# 1) Newborn child (6 weeks):  period of innate reflex movements
# 2) Suckling (6 weeks to 1 year):  period of body straightening, grabbing and locomotion
# 3) Early childhood (1 to 3 years):  period of developing walk, run and handling objects     
# 4) Pre-school childhood (3 to 7 years):  period of developing new, mainly overall, movements
# 5) School childhood (7 to 11 years):  period of enhanced motor learning
# 
# Adolescence:
# 1) Puberty (11 to 15 years):  period of differentiation and redevelopment of motor skills
# 2) Adolescence (15 to 20 years):  period of integration and completing motor development
# 
# Adulthood:
# 1) Early adulthood (20 to 30 years):  period of the climax of motor efficiency
# 2) Middle adulthood (30 to 45 years):  period of stabilized motor efficiency
# 3) Late adulthood (45 to 60 years):  period of decline in motor efficiency
# 
# Old Age:
# 1) Early old age (60 to 75 years):  period of initial involution of human motor skills
# 2) Middle old age (75 to 90 years):  period of involution of human motor skills
# 3) Late old age (over 90 years):  period of decline in human motor skills
# 
# From the information provided in the above chart, for this case I use 8 different age group section :
# 1. For < 1 year : Infant
# 2. 1-10 : Child
# 3. 11-20: Adolescene
# 4. 21-30: Adult
# 5. 31-45 : Middle-age
# 6. 45-60 : Older Adult
# 7. 61-75 : Early-old
# 8. For > 75 : Old

# In[3]:


data['Age'] = data['Age'].replace(['decreases with age premature ageing', 'brain ageing', 'no effect of age', 'all age groups',  'as age increases cases increase but severity decreases', 'risk increases with age no specific age group', 'no specific effect of age', 'any age group complexity to control increases with age', 'increases with age',  'increases with age risk increases 1% per year',  'increases with age more specifically brain ageing', 'any age group complexity to control increases with age'], 'no effect')


# In[4]:


data['Age'] = data['Age'].replace(['child 6-12 months', 'less then 6 months'], 'infant')


# In[5]:


data['Age'] = data['Age'].replace(['elderly infant', 'infant elder'], 'child')


# In[6]:


data['Age'] = data['Age'].replace(['teenage-middle age', 'after puberty', 'young and adolescents'], 'adolescene')


# In[7]:


data['Age'] = data['Age'].replace(['more common in young age',  'young adults'], 'adult')


# In[8]:


data['Age'] = data['Age'].replace(['38 +- 16', '30-40'], 'middle-age')


# In[9]:


data['Age'] = data['Age'].replace(['56 +- 16', '50-64'], 'older adult')


# In[10]:


data['Age'] = data['Age'].replace(['60-64 most likely'], 'early-old')


# In[11]:


data['Age'] = data['Age'].replace(['increases with age most likely after 85'], 'old')


# In[12]:


data['Age'] = data['Age'].replace(['increases with age mostly after 60', 'more likely in old age group', 'most likely in old age groups', 'elderly adults', 'increases with age most likely after 60', 'most like after 65', 'most likely after 60', 'increases with age but most likely after 65', 'older age group'], '>60')


# In[13]:


age = data.Age[1:]
differentAge = age.unique()
print(differentAge)
print(len(differentAge))


# In[14]:


data['Season'] = data['Season'].replace(['high in winters', 'winters', 'increases in cold weather', 'dry winters', 'cold weather',  'cold winters'], 'winter')


# In[15]:


data['Season'] = data['Season'].replace(['no effect',  'independent other then sad',  'changes with season and colors', 'sudden change in season', 'sunlight cure required', 'low uv ray exposion', 'little heat', 'changing barometric and atmospheric pressure'], 'any season')


# In[16]:


data['Season'] = data['Season'].replace(['summers', ], 'summer')


# In[17]:


data['Season'] = data['Season'].replace([ 'cold-spring'], 'spring')


# In[18]:


data['Season'] = data['Season'].replace(['rainy season'], 'autumn')


# In[19]:


data['Season'] = data['Season'].replace(['ability to think decline in winter and early spring', 'late winter to early spring', 'winter to early spring',  'winter - spring'], 'winter-spring')


# In[20]:


data['Season'] = data['Season'].replace(['humid weather', 'more likely in rainy season', 'warmer weather', 'sunlight exposure'], 'summer-autumn')


# In[21]:


data['Season'] = data['Season'].replace(['spring and humid weather',  'summer - spring'], 'spring-summer')


# In[22]:


season = data.Season[1:]
differentSeason = season.unique()
print(differentSeason)
print(len(differentSeason))


# In[23]:


data.to_csv("FinalDatasetWithSymptom.csv", index=False)

