#!/usr/bin/env python
# coding: utf-8

# In[30]:


import tkinter as tk
from tkinter import ttk
from datetime import date, datetime
import pickle
import numpy as np
import pandas as pd
import csv


# My App Structure

# In[2]:


class myApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {} 

        for F in (StartPage, adminPage, predictionPage, newDataPage, informationPage, symptomPage, diseasePage, drugPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
            
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# Start Page

# In[3]:


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        head = ttk.Label(self, anchor= tk.CENTER, justify= tk.CENTER, text="Medical Diagnose System", foreground="black", background="light gray")
        head.config(font=("Elephant", 20))
        head.grid(row=1, column=0, columnspan=4, padx=50, pady=20)
        
        login = ttk.Label(self, anchor= tk.CENTER, justify= tk.CENTER, text="LOG-IN as", foreground="black", background="light gray")
        login.config(font=("Elephant", 15))
        login.grid(row=3, column=0, columnspan=2, padx=50, pady=20)

        info = ttk.Label(self, anchor= tk.CENTER, justify= tk.CENTER, text="For Information", foreground="black", background="light gray")
        info.config(font=("Elephant", 15))
        info.grid(row=3, column=2, columnspan=2, padx=50, pady=20)

        button1 = ttk.Button(self, text ="Admin", command = lambda : controller.show_frame(adminPage)).grid(row = 5, column = 0, padx = 30, pady = 10)        
        button2 = ttk.Button(self, text ="A Patient", command = lambda : controller.show_frame(predictionPage)).grid(row = 7, column = 0, padx = 30, pady = 10)        
        button3 = ttk.Button(self, text ="A Doctor", command = lambda : controller.show_frame(newDataPage)).grid(row = 9, column = 0, padx = 30, pady = 10)        
        button4 = ttk.Button(self, text ="Click Here", command = lambda : controller.show_frame(informationPage)).grid(row = 7, column = 3, padx = 30, pady = 10)


# Admin Page

# In[4]:


class adminPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        head = ttk.Label(self, anchor= tk.CENTER, justify= tk.CENTER, text="Login as Admin", foreground="black", background="light gray")
        head.config(font=("Elephant", 15))
        head.grid(row = 1, column=0, columnspan=3, padx=50, pady=20)
        
        usernamelb = ttk.Label(self, font='Elephant', width=12, text="Username :", foreground="black", background="light gray")
        usernamelb.grid(row = 3, column = 0, padx = 20, pady = 15)
        self.username = tk.StringVar()
        usernameEntry = ttk.Entry(self, textvariable = self.username, width = 10).grid(row = 3, column = 2)
        
        passwordlb = ttk.Label(self, font='Elephant', width=12, text="Password :", foreground="black", background="light gray")
        passwordlb.grid(row = 4, column = 0, padx = 20, pady = 15)
        self.password = tk.StringVar()
        passwordEntry = ttk.Entry(self, textvariable = self.password, width = 10, show='*').grid(row = 4, column = 2)
        
        self.button2 = ttk.Button(self, text ="Train Models")
        
        button1 = ttk.Button(self, text ="Validate", command = lambda : self.show()).grid(row = 5, column = 1, padx = 30, pady = 10)        
        backbutton = ttk.Button(self, text ="Back", command = lambda : controller.show_frame(StartPage)).grid(row = 7, column = 0, padx = 30, pady = 10)
        
    def show(self):
        if((self.username.get() == "Admin") and (self.password.get() == "admin")):
            self.button2.grid(row = 7, column = 1, padx = 30, pady = 10)


# Disease Predicion Page

# In[16]:


class predictionPage(tk.Frame):    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.disease = ""
        self.symptoms = pickle.load(open('myModel.sav', 'rb'))
        print('Total symptoms considered:',len(self.symptoms)-14)
        
        self.nb_model = pickle.load(open('mnb_model.sav', 'rb'))
        self.dtree_model = pickle.load(open('dTree_model.sav', 'rb'))

        self.symptom1 = tk.StringVar()
        self.symptom1.set('Select')
        self.symptom2 = tk.StringVar()
        self.symptom2.set('Select')
        self.symptom3 = tk.StringVar()
        self.symptom3.set('Select')
        self.symptom4 = tk.StringVar()
        self.symptom4.set('Select')
        self.symptom5 = tk.StringVar()
        self.symptom5.set('Select')
        self.Name = tk.StringVar()
        self.gender = tk.StringVar()
        self.gender.set('Select')
        self.age = tk.StringVar()
        self.age.set('Select')
        self.weight = tk.StringVar()

        head = ttk.Label(self, anchor= tk.CENTER, justify= tk.CENTER, text="Disease Predicter", foreground="black", background="light gray")
        head.config(font=("Elephant", 25))
        head.grid(row=1, column=0, columnspan=4, padx=50, pady=20)
        
        NameLb = ttk.Label(self, font='Elephant', width=15, text="Patient's Name:", foreground="black", background="light gray").grid(row=4, column=0, pady=15, padx=20)
        genderLb = ttk.Label(self, font='Elephant', width=15, text="Gender:", foreground="black", background="light gray").grid(row=5, column=0, pady=15, padx=20)
        ageLb = ttk.Label(self, font='Elephant', width=15, text= "Age:" ,foreground="black", background="light gray").grid(row=6, column=0, pady=15, padx=20)
        weightLb1 = ttk.Label(self, font='Elephant', width=15, text= "Weight:" ,foreground="black", background="light gray").grid(row=7, column=0, pady=15, padx=20)
        weightLb2 = ttk.Label(self, font='Elephant', width=15, text= "in Kgs" ,foreground="black", background="light gray").grid(row=7, column=2, pady=15, padx=20)
        
        dateLb = ttk.Label(self, font='Elephant', width=15, text= "Today's Date:", foreground="black", background="light gray")
        dateLb.grid(row=8, column=0, pady=15, padx=20)
        dateLb = ttk.Label(self, font='Elephant', width=15, text= date.today().strftime("%d/%m/%Y"), foreground="black", background="light gray")
        dateLb.grid(row=8, column=1, pady=15, padx=20)
        
        S1Lb = ttk.Label(self, font='Elephant12', width=15, text="Symptom 1:", foreground="yellow", background="blue").grid(row=10, column=0, pady=10, padx=20)
        S2Lb = ttk.Label(self, font='Elephant12', width=15, text="Symptom 2:", foreground="yellow", background="blue").grid(row=11, column=0, pady=10, padx=20)
        S3Lb = ttk.Label(self, font='Elephant12', width=15, text="Symptom 3:", foreground="yellow", background="blue").grid(row=12, column=0, pady=10, padx=20)
        S4Lb = ttk.Label(self, font='Elephant12', width=15, text="Symptom 4:", foreground="yellow", background="blue").grid(row=13, column=0, pady=10, padx=20)
        S5Lb = ttk.Label(self, font='Elephant12', width=15, text="Symptom 5:", foreground="yellow", background="blue").grid(row=14, column=0, pady=10, padx=20)
        
        resLb1 = ttk.Label(self, font='Elephant11', width=22, text='Predicted Disease :', foreground='white', background='red').grid(row=16, column=0, pady=10, padx=20)        
        resLb2 = ttk.Label(self, font='Elephant11', width=22, text='Predicted Drugs :', foreground='white', background='red').grid(row=18, column=0, pady=10, padx=20)
        
        NameEn = ttk.Entry(self, width=25, textvariable= self.Name).grid(row=4, column=1)
        genderEn = ttk.Combobox(self, textvariable= self.gender, values=['Female', 'Male']).grid(row=5, column=1)
        
        self.ageList = np.arange(1, 101, 1).tolist()
        self.ageList = ['Less then 1'] + self.ageList + ['Grater then 100']
        ageEn = ttk.Combobox(self, textvariable= self.age, values= self.ageList).grid(row=6, column=1)
        weightEn = ttk.Entry(self, textvariable= self.weight).grid(row=7, column=1)
        
        self.OPTIONS = list(np.sort(self.symptoms))
        self.rList = ['Female', 'Male', 'winter', 'summer', 'autumn', 'spring', 'infant', 'child', 'adolescene', 'adult', 'middle-age', 'older adult', 'early-old', 'old']
        for x in self.rList:
            self.OPTIONS.remove(x)
        self.OPTIONS = [str(x).title() for x in self.OPTIONS]
        
        S1En = ttk.Combobox(self, textvariable= self.symptom1, values= self.OPTIONS).grid(row=10, column=1)
        S2En = ttk.Combobox(self, textvariable= self.symptom2, values= self.OPTIONS).grid(row=11, column=1)
        S3En = ttk.Combobox(self, textvariable= self.symptom3, values= self.OPTIONS).grid(row=12, column=1)
        S4En = ttk.Combobox(self, textvariable= self.symptom4, values= self.OPTIONS).grid(row=13, column=1)
        S5En = ttk.Combobox(self, textvariable= self.symptom5, values= self.OPTIONS).grid(row=14, column=1)
        
        diseaseResult = ttk.Button(self, text='Predict Disease', command = lambda : self.predictDisease()).grid(row=16, column=2, pady=10, padx=30)
        drugResult = ttk.Button(self, text='Predict Drug', command = lambda : self.findDrug()).grid(row=18, column=2, pady=10, padx=30)

        backbutton = ttk.Button(self, text ="Back", command = lambda : controller.show_frame(StartPage)).grid(row = 20, column = 0, padx = 30, pady = 10)
        
    def agegrouping(self, x):
        if (x == 'Less then 1'):
            return 'infant'
        elif (x == 'grater then 100') :
            return 'old'
        elif(int(x) >= 1 and int(x)<= 10):
            return 'child'
        elif (int(x) >= 11 and int(x)<= 20) :
            return 'adolescene'
        elif(int(x) >= 21 and int(x)<= 30) :
            return 'adult'
        elif(int(x) >= 31 and int(x)< 45) :
            return 'middle-age'
        elif(int(x) >= 45 and int(x)<= 60):
            return 'older adult'
        elif(int(x) >= 61 and int(x)<= 75) :
            return 'early-old'
        else :
            return 'old'
    
    def getSeason(self, doy):
        spring = range(80, 172)
        summer = range(172, 264)
        fall = range(264, 355)
        if doy in spring:
            season = 'spring'
        elif doy in summer:
            season = 'summer'
        elif doy in fall:
            season = 'autumn'
        else:
            season = 'winter'
        return season
    
    def NB_model(self):
        ages = self.agegrouping(self.age.get())
        season = self.getSeason(datetime.today().timetuple().tm_yday)
        user_symptoms = [self.gender.get(), ages, season, self.symptom1.get().lower(), self.symptom2.get().lower(), self.symptom3.get().lower(), self.symptom4.get().lower(), self.symptom5.get().lower()]
        model_input = [0]*len(self.symptoms)
        for sym in user_symptoms:
            model_input[np.where (self.symptoms == sym )[0][0]] = 1

        pred = self.nb_model.predict([model_input])[0]
        return pred
        
    def DTree_model(self):
        ages = self.agegrouping(self.age.get())
        season = self.getSeason(datetime.today().timetuple().tm_yday)
        user_symptoms = [self.gender.get(), ages, season, self.symptom1.get().lower(), self.symptom2.get().lower(), self.symptom3.get().lower(), self.symptom4.get().lower(), self.symptom5.get().lower()]
        model_input = [0]*len(self.symptoms)
        for sym in user_symptoms:
            model_input[np.where (self.symptoms == sym )[0][0]] = 1

        pred = self.dtree_model.predict([model_input])[0]
        return pred
    
    def predictDisease(self):
        result1 = self.NB_model()
        result2 = self.DTree_model()
        
        if(result1 == result2):
            self.disease = result1
            print('Predicted Disease: '+result1)
            Resultfield = ttk.Label(self, text = result1.title(), foreground='white', background = 'black',font=('Arial',14)).grid(row=16, column=1, pady=10)
            
    def findDrug(self):
        df=pd.read_csv('Grouped_Drug_Recommendation_Normalized.csv')
        a=df[df['condition']== self.disease]
        b=a['meanNormalizedScore'].values.max() 
#         print("fdfd")
        c=a.loc[a['meanNormalizedScore']== b, 'drug name']
        c=[i for item in c for i in item.split()]
        
        drugLev = ttk.Label(self, text = c[0], foreground='white', background = 'black',font=('Arial',14)).grid(row=19, column=1, pady=10)
        if weight<10:
            doseLev = ttk.Label(self, text = "Dose: 5mg", foreground='white', background = 'black',font=('Arial',14)).grid(row=19, column=1, pady=10)
        elif (weight>=10 and weight<30):
            doseLev = ttk.Label(self, text = "Dose: 6.5mg", foreground='white', background = 'black',font=('Arial',14)).grid(row=19, column=1, pady=10)
        elif (weight>=30 and weight<50):
            doseLev = ttk.Label(self, text = "Dose: 8mg", foreground='white', background = 'black',font=('Arial',14)).grid(row=19, column=1, pady=10)
        elif weight>=50:
            doseLev = ttk.Label(self, text = "Dose: 10mg", foreground='white', background = 'black',font=('Arial',14)).grid(row=19, column=1, pady=10)


# New Data Page

# In[34]:


class newDataPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.symptom1 = tk.StringVar()
        self.symptom2 = tk.StringVar()
        self.symptom3 = tk.StringVar()
        self.symptom4 = tk.StringVar()
        self.symptom5 = tk.StringVar()
        self.Name = tk.StringVar()
        self.gender = tk.StringVar()
        self.gender.set('Select')
        self.age = tk.StringVar()
        self.weight = tk.StringVar()
        self.disease = tk.StringVar()
        self.drug = tk.StringVar()
        self.dose = tk.StringVar()

        head = ttk.Label(self, anchor= tk.CENTER, justify= tk.CENTER, text="Prescription", foreground="black", background="light gray")
        head.config(font=("Elephant", 25))
        head.grid(row=0, column=0, columnspan=3, padx=50, pady=20)
        
        NameLb = ttk.Label(self, font='Elephant', width=15, text="Patient's Name:", foreground="black", background="light gray").grid(row=2, column=0, pady=15, padx=20)
        genderLb = ttk.Label(self, font='Elephant', width=15, text="Gender:", foreground="black", background="light gray").grid(row=3, column=0, pady=15, padx=20)
        ageLb = ttk.Label(self, font='Elephant', width=15, text= "Age:" ,foreground="black", background="light gray").grid(row=4, column=0, pady=15, padx=20)
        weightLb1 = ttk.Label(self, font='Elephant', width=15, text= "Weight:" ,foreground="black", background="light gray").grid(row=5, column=0, pady=15, padx=20)
        weightLb2 = ttk.Label(self, font='Elephant', width=15, text= "in Kgs" ,foreground="black", background="light gray").grid(row=5, column=2, pady=15, padx=20)
        
        dateLb = ttk.Label(self, font='Elephant', width=15, text= "Today's Date:", foreground="black", background="light gray")
        dateLb.grid(row=6, column=0, pady=15, padx=20)
        dateLb = ttk.Label(self, font='Elephant', width=15, text= date.today().strftime("%d/%m/%Y"), foreground="black", background="light gray")
        dateLb.grid(row=6, column=1, pady=15, padx=20)
        
        S1Lb = ttk.Label(self, font='Elephant12', width=15, text="Symptom 1:", foreground="yellow", background="blue").grid(row=8, column=0, pady=10, padx=20)
        S2Lb = ttk.Label(self, font='Elephant12', width=15, text="Symptom 2:", foreground="yellow", background="blue").grid(row=9, column=0, pady=10, padx=20)
        S3Lb = ttk.Label(self, font='Elephant12', width=15, text="Symptom 3:", foreground="yellow", background="blue").grid(row=10, column=0, pady=10, padx=20)
        S4Lb = ttk.Label(self, font='Elephant12', width=15, text="Symptom 4:", foreground="yellow", background="blue").grid(row=11, column=0, pady=10, padx=20)
        S5Lb = ttk.Label(self, font='Elephant12', width=15, text="Symptom 5:", foreground="yellow", background="blue").grid(row=12, column=0, pady=10, padx=20)
        
        diseaseLb = ttk.Label(self, font='Elephant11', width=22, text='Predicted Disease :', foreground='white', background='red').grid(row=14, column=0, pady=10, padx=20)        
        drugLb = ttk.Label(self, font='Elephant11', width=22, text='Predicted Drugs :', foreground='white', background='red').grid(row=15, column=0, pady=10, padx=20)
        doseLb = ttk.Label(self, font='Elephant11', width=22, text='Dose in mgs :', foreground='white', background='red').grid(row=16, column=0, pady=10, padx=20)
        
        NameEn = ttk.Entry(self, width=26, textvariable= self.Name).grid(row=2, column=1)
        genderEn = ttk.Combobox(self, textvariable= self.gender, values=['Female', 'Male']).grid(row=3, column=1)
        ageEn = ttk.Entry(self, textvariable= self.age).grid(row=4, column=1)
        weightEn = ttk.Entry(self, textvariable= self.weight).grid(row=5, column=1)
        
        S1En = ttk.Entry(self, textvariable= self.symptom1).grid(row=8, column=1)
        S2En = ttk.Entry(self, textvariable= self.symptom2).grid(row=9, column=1)
        S3En = ttk.Entry(self, textvariable= self.symptom3).grid(row=10, column=1)
        S4En = ttk.Entry(self, textvariable= self.symptom4).grid(row=11, column=1)
        S5En = ttk.Entry(self, textvariable= self.symptom5).grid(row=12, column=1)
        
        diseaseEn = ttk.Entry(self, textvariable= self.disease).grid(row=14, column=1)
        drugEn = ttk.Entry(self, textvariable= self.drug).grid(row=15, column=1)
        doseEn = ttk.Entry(self, textvariable= self.dose).grid(row=16, column=1)
        
        addbutton = ttk.Button(self, text ="Add to Dataset", command = lambda : self.createNewFile()).grid(row = 17, column = 1, padx = 30, pady = 10)
        backbutton = ttk.Button(self, text ="Back", command = lambda : controller.show_frame(StartPage)).grid(row = 17, column = 0, padx = 30, pady = 10)
    
    def getSeason(self, doy):
        spring = range(80, 172)
        summer = range(172, 264)
        fall = range(264, 355)
        if doy in spring:
            season = 'spring'
        elif doy in summer:
            season = 'summer'
        elif doy in fall:
            season = 'autumn'
        else:
            season = 'winter'
        return season
    
    def createNewFile(self):
        with open("newData.csv", 'w', newline='') as file:
            columns = ['Name', 'Disease', 'Gender', 'Age', 'Season', 'Symptom', 'Weight']
            writer = csv.DictWriter(file, fieldnames=columns)

            writer.writeheader()
            writer.writerow({'Name': self.Name.get().title(), 'Disease': self.disease.get(), 'Gender': self.gender.get(), 'Age': self.age.get(), 
                             'Season': self.getSeason(datetime.today().timetuple().tm_yday), 
                             'Symptom': [self.symptom1.get().lower(), self.symptom2.get().lower(), self.symptom3.get().lower(), self.symptom4.get().lower(), self.symptom5.get().lower()],
                             'Weight': self.weight.get()})


# Information Page

# In[7]:


class informationPage(tk.Frame):
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        head = ttk.Label(self, anchor= tk.CENTER, justify= tk.CENTER, text="To Know More", foreground="black", background="light gray")
        head.config(font=("Elephant", 15))
        head.grid(row=1, column=0, columnspan=3, padx=50, pady=20)
        
        infoLb1 = ttk.Label(self, font= ('Arial', 8), width=30, text="1. Disease for a particular Symptom-").grid(row=3, column=0, pady=10, padx=20)
        infoLb2 = ttk.Label(self, font= ('Arial', 8), width=30, text="2. Full Information for a Disease-").grid(row=4, column=0, pady=10, padx=20)
        infoLb3 = ttk.Label(self, font= ('Arial', 8), width=30, text="3. Drugs Available for a Disease-").grid(row=5, column=0, pady=10, padx=20)
        
        infoButton1 = ttk.Button(self, text ="Click Here!", command = lambda : controller.show_frame(symptomPage)).grid(row = 3, column = 1, padx = 30, pady = 10)
        infoButton2 = ttk.Button(self, text ="Click Here!", command = lambda : controller.show_frame(diseasePage)).grid(row = 4, column = 1, padx = 30, pady = 10)
        infoButton3 = ttk.Button(self, text ="Click Here!", command = lambda : controller.show_frame(drugPage)).grid(row = 5, column = 1, padx = 30, pady = 10)
        
        backbutton = ttk.Button(self, text ="Back", command = lambda : controller.show_frame(StartPage)).grid(row = 7, column = 0, padx = 30, pady = 10)


# In[22]:


class symptomPage(tk.Frame):
    def findDiseases(self):
        df = self.data.loc[self.data['Symptom'] == self.symptom.get().lower()]
        diseases = df['Disease'].unique().tolist()
        diseases =  [str(x).title() for x in diseases]
        file = open("result.txt","w+")
        j=0
        for i in diseases:
            j +=1
            file.write(str(j) + ". " + i + "\n")
        resultLb = ttk.Label(self, font= ('Arial', 10), width=20, text="Find it in result.txt File").grid(row=5, column=1, pady=10, padx=20)
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.data = pd.read_csv('DatasetWithSymptom.csv', names=['Disease', 'Gender', 'Age', 'Season', 'Symptom', 'Weight'])
        self.data.drop(self.data.head(1).index, inplace=True)
        self.symptoms = self.data['Symptom'].unique().tolist()
        self.symptoms =  [str(x).title() for x in self.symptoms]
        self.symptom = tk.StringVar()
        self.symptom.set('Select')
        
        head = ttk.Label(self, anchor= tk.CENTER, justify= tk.CENTER, text="Disease for a particular Symptom", foreground="black", background="light gray")
        head.config(font=("Elephant", 10))
        head.grid(row=1, column=0, columnspan=3, padx=50, pady=20)
        
        symptomLb = ttk.Label(self, font= ('Arial', 10), width=15, text="Symptom : ").grid(row=3, column=0, pady=10, padx=20)
        symptomEn = ttk.Combobox(self, textvariable= self.symptom, values= self.symptoms).grid(row=3, column=1)
        diseaseLb = ttk.Label(self, font= ('Arial', 10), width=15, text="Diseases : ").grid(row=5, column=0, pady=10, padx=20)

        searchbutton = ttk.Button(self, text ="Search", command = lambda : self.findDiseases()).grid(row = 9, column = 1, padx = 30, pady = 10)
        backbutton = ttk.Button(self, text ="Back", command = lambda : controller.show_frame(informationPage)).grid(row = 9, column = 0, padx = 30, pady = 10)


# In[28]:


class diseasePage(tk.Frame):
    def findResults(self):
        df = self.data.loc[self.data['Disease'] == self.disease.get().lower()]
        np.savetxt('result.txt', df.values, fmt='%s')
        resultLb = ttk.Label(self, font= ('Arial', 10), width=20, text="Find it in result.txt File").grid(row=5, column=1, pady=10, padx=20)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.data = pd.read_csv('DatasetWithSymptom.csv', names=['Disease', 'Gender', 'Age', 'Season', 'Symptom', 'Weight'])
        self.data.drop(self.data.head(1).index, inplace=True)
        self.diseases = self.data['Disease'].unique().tolist()
        self.diseases =  [str(x).title() for x in self.diseases]
        self.disease = tk.StringVar()
        self.disease.set('Select')
        
        head = ttk.Label(self, anchor= tk.CENTER, justify= tk.CENTER, text="Full Information for a Disease", foreground="black", background="light gray")
        head.config(font=("Elephant", 10))
        head.grid(row=1, column=0, columnspan=3, padx=50, pady=20)
        
        diseaseLb = ttk.Label(self, font= ('Arial', 10), width=15, text="Disease : ").grid(row=3, column=0, pady=10, padx=20)
        diseaseEn = ttk.Combobox(self, textvariable= self.disease, values= self.diseases).grid(row=3, column=1)
        detailLb = ttk.Label(self, font= ('Arial', 10), width=15, text="Details : ").grid(row=5, column=0, pady=10, padx=20)

        searchbutton = ttk.Button(self, text ="Search", command = lambda : self.findResults()).grid(row = 9, column = 1, padx = 30, pady = 10)
        backbutton = ttk.Button(self, text ="Back", command = lambda : controller.show_frame(informationPage)).grid(row = 9, column = 0, padx = 30, pady = 10)


# In[10]:


class drugPage(tk.Frame):
    disease='d'
    weight=0
    def findDrug():
        disease=''
        df=pd.read_csv('Grouped_Drug_Recommendation_Normalized.csv')
        a=df[df['condition']==disease]
        b=a['meanNormalizedScore'].values.max() 
        print("fdfd")
        c=a.loc[a['meanNormalizedScore']== b, 'drug name']
    #     print(c)
        c=[i for item in c for i in item.split()]
    #     print(c)
        emptyLabel.config(text='take : '+c[0])
        if weight<10:
            emptyLabel1.config(text='dose : 5mg')
        elif (weight>=10 and weight<30):
            emptyLabel1.config(text='dose : 6.5mg')
        elif (weight>=30 and weight<50):
            emptyLabel1.config(text='dose : 8mg')
        elif weight>=50:
            emptyLabel1.config(text='dose : 10mg')
        
        
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        head = ttk.Label(self, anchor= tk.CENTER, justify= tk.CENTER, text="Drug Prediction", foreground="black", background="light gray")
        head.config(font=("Elephant", 25))
        head.grid(row=1, column=0, columnspan=3, padx=50, pady=20)
        
        label1=ttk.Label(self,text="Disease:",font='Elephant12', width=15,  foreground="black", background="light gray")
        label1.grid(row=6, column=0, pady=15, padx=20)
        self.data=tk.StringVar()
        disease= self.data.get()
        textbox= ttk.Entry(self,textvariable=self.data,font='Elephant12', width=15, foreground="black", background="white")
        textbox.grid(row=7, column=0, pady=15, padx=20)
        
        label2=ttk.Label(self,text="Weight in kg:",font='Elephant12', width=15,  foreground="black", background="light gray")
        label2.grid(row=8, column=0, pady=15, padx=20)
        self.data1=tk.IntVar()
        weight= self.data1.get()
        textbox= ttk.Entry(self,textvariable= self.data1,font='Elephant12', width=15, foreground="black", background="white")
        textbox.grid(row=9, column=0, pady=15, padx=20)
        
        button= ttk.Button(self,command= lambda : self.findDrug() ,text='Find Drug')
#         button.grid(row=1,column=1,sticky=W)
        button.grid(row=9, column=1, pady=15, padx=20)

        emptyLabel= ttk.Label(self, foreground='black',font=('Arial',14,'bold'))
        emptyLabel.grid(row=3,column=1, pady=10)
#         emptyLabel.config(text='take : '+c[0])
        emptyLabel1= ttk.Label(self, foreground='black',font=('Arial',14,'bold'))
        emptyLabel1.grid(row=5,column=1, pady=10)
    
    
        backbutton = ttk.Button(self, text ="Back", command = lambda : controller.show_frame(informationPage))
        backbutton.grid(row = 22, column = 0, padx = 30, pady = 10)


# In[37]:


app = myApp()
app.mainloop()


# In[ ]:




