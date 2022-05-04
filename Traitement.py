#!/usr/bin/env python
#coding: utf-8
from fileinput import filename
from tkinter import *
from tkinter import filedialog
import zipfile

File_Input=''
Folder_Output=''
firstFile=''
secondFile=''
thirdFile=''
separateur=';'
#===================================================================================
#                         FONCTIONS POUR OUVRIRE UN FICHIER
#===================================================================================
    
class Callback:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
    def __call__(self):
        self.func(*self.args, **self.kwargs)

# FONCTIONS POUR OUVRIRE UN REPERTOIRE
def open_folder(Btn):
    global Folder_Output
    folder = filedialog.askdirectory(initialdir = "/",title="Select Folder to open")
    Btn.delete(0, END)
    Btn.insert(0, folder)
    Folder_Output = Btn.get() 

# FONCTIONS POUR OUVRIRE UN FICHIER	
def browseFiles(Btn):
    global File_Input
    filename = filedialog.askopenfilename(initialdir = "/",	title = "Select a File", filetypes = (("all files", "*.*"),("Text files", "*.txt*")))
    Btn.delete(0, END)
    Btn.insert(0, filename)
    File_Input = Btn.get()


# FONCTIONS POUR CHOISIR LE SEPARATEUR
def selection(label, value, ):
    choice = value.get()
    if choice == 1:
        separateur = ';'
        label.configure(text='Délimiteur: ( '+separateur+' )')
    elif choice == 2:
        separateur = ','
        label.configure(text='Délimiteur: ( '+separateur+' )')
    elif choice == 3:
        separateur = '|'
        label.configure(text='Délimiteur: ( '+separateur+' )')
        pass
    return separateur


# FONCTIONS POUR LANCER LA CONVERTION
def valideFile(Champ1, Champ2, Champ3):
    global firstFile
    global secondFile
    global thirdFile
    global separateur
    firstFile = Champ1.get()
    secondFile = Champ2.get()
    thirdFile = Champ3.get()
    
    CheminAbsoluFile1 = Folder_Output+"/"+firstFile+".csv"
    CheminAbsoluFile2 = Folder_Output+"/"+secondFile+".csv"
    CheminAbsoluFile3 = Folder_Output+"/"+thirdFile+".csv"
    
    CheminAbsoluZip1 = Folder_Output+"/"+firstFile+".zip"
    CheminAbsoluZip2 = Folder_Output+"/"+secondFile+".zip"
    CheminAbsoluZip3 = Folder_Output+"/"+thirdFile+".zip"
    
    Csv_File1 = firstFile+".csv"
    Csv_File2 = secondFile+".csv"
    Csv_File3 = thirdFile+".csv"
    
    # print(File_Input)
    # print(firstFile)
    # print(secondFile)
    # print(thirdFile)