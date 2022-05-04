#!/usr/bin/env python
#coding: utf-8
import tkinter as tk
import pandas as pd
import zipfile
import os

# NOM fichier de sortie
Fichier1= 'sortie.csv'
Fichier2= 'sortie.csv'
Fichier3= 'sortie.csv'

RepOut ='C:\\Users\\SabiOniankitan\\OneDrive - TALHENT\\Bureau\\App'

ZipOut = "C:\\Users\\SabiOniankitan\\OneDrive - TALHENT\\Bureau\\App\\sortie.zip"
data = "C:\\Users\\SabiOniankitan\\OneDrive - TALHENT\\Bureau\\Data\\Crosstalent.csv"
sortie = "C:\\Users\\SabiOniankitan\\OneDrive - TALHENT\\Bureau\\App\\sortie.csv"
delimiteur = ";"

def Crosstalent_Vers_Neocase(fichier_In, fichier_Out, delimiteur, zip_Out, fichierCsv_Out, Repertoire_Out):
    Donne_Vide = "colonne_Vide.csv"
    fichier_In = pd.read_csv(fichier_In , delimiter= delimiteur)
    Donne_Vide = pd.read_csv(Donne_Vide , delimiter= delimiteur)
    
    DFram1 = fichier_In[['Matricule de paie du collaborateur','Civilité du collaborateur','Nom du collaborateur','Prénom du collaborateur','Adresse email professionnelle du collaborateur']]
    DFram1.insert(5,"colonne_6",'')
    DFram1.insert(6,"colonne_7",'')
    DFram1.insert(7,"colonne_8",'')
    DFram1.insert(8,"colonne_9",'')
    DFram1.insert(9,"PAYS_UTILISATEUR",'FR')
    DFram1.columns = ['IDENTIFIER','TITLE','NAME','FIRST NAME','EMAIL','COLONNE_6','COLONNE_7','COLONNE_8','COLONNE_9','COUNTRY']
    d = {'Male':0,'Female':1}
    DFram1["TITLE"] = DFram1["TITLE"].map(d)
    
    DFram2 = fichier_In[['Service','Adresse email professionnelle du collaborateur']]
    DFram2.insert(0,"PAYS_UTILISATEUR",'FR')
    DFram2.insert(2,"CODELANGUE",'FR')
    DFram2.insert(3,"SERVICE CATALOG",'')
    DFram2.insert(5,"colonne_16",'')
    DFram2.insert(6,"colonne_17",'')
    DFram2.insert(7,"ROLES",'FONCTION Collaborateur')
    DFram2.insert(8,"TYPE RELATIONSHIP 1",'Mon équipe;Mon Manager')
    DFram2.insert(9,"IDENTIFIER RELATIONSHIP 1",'')
    DFram2.insert(10,"TYPE RELATIONSHIP 2",'RRH de;Mon RRH')
    DFram2.insert(11,"IDENTIFIER RELATIONSHIP 2",'')
    DFram2.columns = ['COLONNE_11','ORGANIZATION','LANGUAGE','SERVICE CATALOG','LOGIN','COLONNE_16','COLONNE_17','ROLES','TYPE RELATIONSHIP 1','IDENTIFIER RELATIONSHIP 1','TYPE RELATIONSHIP 2','IDENTIFIER RELATIONSHIP 2']
    
    DFram3 = fichier_In[['Adresse email professionnelle du collaborateur']]
    DFram3.insert(0,"colonne_174",'IRIS')
    DFram3.insert(1,"colonne_175",'')
    DFram3.columns = ['SOURCE','COLONNE_175','ID SLACK']
    
    DFram4 = pd.concat([DFram1,DFram2,Donne_Vide,DFram3], axis=1)
    DFram5 = DFram4.fillna("")
    
    try: # On essaye de faire la copie de la data
        DFram5.to_csv(fichier_Out, index=False, sep = '|', encoding = "UTF-8")#encoding à modifier encoding = "ISO-8859-1"
        
        absolute_path = r''+Repertoire_Out
        filepath = r''+zip_Out
        get_file = os.path.join(absolute_path, fichierCsv_Out)
        zip_name = zipfile.ZipFile(filepath, 'w')
        zip_name.write(get_file, fichierCsv_Out)
        os.remove(fichier_Out)
    except:
        print("Veuillez fermer le fichier de sortie Neocase ouvert.")



print("Debut")

Crosstalent_Vers_Neocase(data, sortie, delimiteur, ZipOut, Fichier1, RepOut)

print("Fin:")

