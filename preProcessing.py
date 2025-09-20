#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import pandas as pd
from collections import defaultdict


# In[2]:


# Make a data list of disease and Symptoms....
def makeList(data):
    data_list = []
    data_name = data.replace('^','_').split('_')
    data_name = [s.lower() for s in data_name]
    n = 1
    for names in data_name:
        if n%2 == 0:
            data_list.append(names)
        n+=1
    return data_list


# In[3]:


def merge(list1, list2, list3, list4):
    merged_list = tuple(zip(list1, list2, list3, list4))
    return merged_list


# In[4]:


if __name__ == "__main__" :
    # Loading the rawDataset file....
    data = pd.read_excel('rawDataset.xlsx')
    # print(data.head(5), end='\n')

    # Filling Null cell with past data....
    data = data.fillna(method='ffill')
    # print(data.head(5), end='\n')

    ### Makeing Disease and Symptom base CSV file .......
    diseaseName = []
    diseaseSymptomDictionary = defaultdict(list)
    disease_symptom_count = {}
    count = 0

    for idx, row in data.iterrows():
        # Get the Disease Names
        if (row['Disease'] !="\xc2\xa0") and (row['Disease'] != ""):
            disease = row['Disease']
            diseaseName = makeList(disease)
            count = row['Count of Disease Occurrence']

        # Get the Symptoms Corresponding to Diseases
        if (row['Symptom'] !="\xc2\xa0") and (row['Symptom'] != ""):
            symptom = row['Symptom']
            symptom_list = makeList(symptom)
            for d in diseaseName:
                for s in symptom_list:
                    diseaseSymptomDictionary[d].append(s)
                disease_symptom_count[d] = count

    # Saving the cleaned data
    with open('diseaseSymptomData.csv','w') as csvfile:
        writer = csv.writer(csvfile)
        for k, val in diseaseSymptomDictionary.items():
            for v in val:
                k = str.encode(k).decode('utf-8')
                writer.writerow([k, v, disease_symptom_count[k]])

    columns = ['Disease', 'Symptom', 'Weight']
    data = pd.read_csv('diseaseSymptomData.csv', names=columns, encoding='ISO-8859-1')
    # print('Saving CSV file content of disease and Symptoms\n')
    data.to_csv('diseaseSymptomData.csv', index=False)
    ###.......... Complete the process

    # Loading the FinalDataset file....
    dataWithAttribute = pd.read_excel('FinalDataset.xlsx')
    # print(dataWithAttribute.head(5), end='\n')

    ### Makeing Disease and different attribute base CSV file .......
    # Get the Disease Names
    disease_name = dataWithAttribute['Disease'].tolist()
    disease_name = [s.lower() for s in disease_name]

    # Get the Gender Corresponding to Diseases List
    genderList = dataWithAttribute['Gender Most Likely'].tolist()
    genderList = [gender.replace('Female and if smoking inculded then male', 'Nutral').replace('Both are equally likely', 'Nutral') for gender in genderList]

    # Get the Age Corresponding to Diseases List
    ageList = dataWithAttribute['Age'].tolist()
    ageList = [s.lower() for s in ageList]
    
    # Get the Age Corresponding to Diseases List
    seasonList = dataWithAttribute['Season'].tolist()
    seasonList = [s.lower() for s in seasonList]

    finalData = merge(disease_name, genderList, ageList, seasonList)

    # Saving the finalData into a csv file
    with open('diseaseAttributeData.csv','w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(finalData)

    columns = ['Disease', 'Gender', 'Age', 'Season']
    data = pd.read_csv('diseaseAttributeData.csv', names=columns, encoding='ISO-8859-1')
    # print('Saving CSV file content of disease and Gender and Age\n')
    data.to_csv('diseaseAttributeData.csv', index=False)
    ###.......... Complete the process

    ### Joining symptom and attribute csv file in one
    symptomFile = pd.read_csv('diseaseSymptomData.csv')
    attributeFile = pd.read_csv('diseaseAttributeData.csv')

    finalFile = attributeFile.merge(symptomFile, on='Disease')
    print('Saving Final CSV file content of disease, Symptoms, Gender, Age and Season\n')
    finalFile.to_csv("DatasetWithSymptom.csv", index=False)

    # analyzing Final dataset
    columns = ['Disease', 'Gender', 'Age', 'Season', 'Symptom', 'Weight']
    data = pd.read_csv('DatasetWithSymptom.csv', names=columns)

    unique_diseases = data['Disease'].unique()
    unique_symptoms = data['Symptom'].unique()
    gendersType = data['Gender'].unique()
    differentAge = data['Age'].unique()
    differentSeason = data['Season'].unique()

    print('No. of diseases:',len(unique_diseases)-1)
    print('No. of symptoms:',len(unique_symptoms)-1)
    print('Gender Depandencies:', gendersType[1:])
    print('Age Depandencies :', differentAge[1:],'\n')
    print('Number of Different Age Depandencies : ', len(differentAge)-1,'\n')
    print('Season Depandencies :', differentSeason[1:],'\n')
    print('Number of Different Season Depandencies : ', len(differentSeason)-1)


# In[ ]:




