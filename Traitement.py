#!/usr/bin/env python
#coding: utf-8
from fileinput import filename
from tkinter import *
from tkinter import filedialog
from tkinter import *
File_Input=''
Folder_Output=''
firstFile=''
secondFile=''
thirdFile=''
separateur=''
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
    global File_Entre
    filename = filedialog.askopenfilename(initialdir = "/",	title = "Select a File", filetypes = (("all files", "*.*"),("Text files", "*.txt*")))
    Btn.delete(0, END)
    Btn.insert(0, filename)
    File_Entre = Btn.get()

def valideFile(Champ1, Champ2, Champ3, Btn):
    global firstFile
    global secondFile
    global thirdFile
    global separateur
    firstFile = Champ1.get()
    secondFile = Champ2.get()
    thirdFile = Champ3.get()
    Btn.configure(text=separateur)

def print_selection(label, v1, v2, v3):
    if (v1.get() == 1) & (v2.get() == 0)  & (v3.get() == 0):
        separateur = ';'
        label.configure(text='Séparateur: ( '+separateur+' )')
    elif (v1.get() == 0) & (v2.get() == 1) & (v3.get() == 0):
        separateur = ','
        label.configure(text='Séparateur: ( '+separateur+' )')
    elif (v1.get() == 0) & (v2.get() == 0) & (v3.get() == 1):
        separateur = '|'
        label.configure(text='Séparateur: ( '+separateur+' )')
    else:
        label.configure(text='Choisisez un seul')