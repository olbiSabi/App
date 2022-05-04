#!/usr/bin/env python
# coding: utf-8
from tkinter import filedialog
from pyexpat.errors import messages
from tkinter import *
from Traitement import *
import zipfile

#===================================================================================
#                     CREATION DE L'INSTANCE DE LA FENETRE
#===================================================================================
# On Crée une fenêtre, racine de notre interface
Fenetre = Tk()
# On personnaliser la fenêtre
Fenetre.title("TalHent")
Fenetre.geometry('{}x{}'.format(540, 300))
Fenetre.resizable(width=FALSE, height=FALSE)
#Fenetre.iconbitmap("logo-blanc.ICO")

#===================================================================================
#                             DEFINITION DES WIDGETS
#===================================================================================

#                    *********  LES FRAMES *********
# frame du haut
frame_Haut = Frame(Fenetre, width=530, height=70,pady=3)
bloc_Repertoire_Entre = LabelFrame(frame_Haut, text="Chemin d'accès du fichier d'entrer", fg= 'blue', width=530, height=65, pady=3, padx=3)

# frame du Bas
frame_Centre = Frame(Fenetre, width=530, height=190,pady=3,padx=3)

# frame à l'intérieur de la frame du bas
frame_Gauche_du_Centre = Frame(frame_Centre, width=320, height=190,pady=3,padx=3)
bloc_Repertoir_Sortie = LabelFrame(frame_Gauche_du_Centre, text="Informations sur les fichiers sortie", fg= 'blue', width=310, height=150, pady=3, padx=3)
frame_Centre_du_Bas = Frame(frame_Centre, bg='#848484', width=2, height=150,pady=3,padx=3)
frame_Droite_du_Centre = Frame(frame_Centre, width=170, height=190,pady=3,padx=3)
bloc_Separateur = LabelFrame(frame_Droite_du_Centre, text="Délimiteurs", fg= 'blue', width=100, height=170, pady=3, padx=3)
frame_bas = Frame(Fenetre, width=530, bg='#255236', height=20)


#                    *********  LES LABELS *********
# BLOC ENTRER (Chemin d'accès du fichier d'entrer)
label_NomFichier = Label(bloc_Repertoire_Entre, text='Fichier:')
label_EntreFichier = Entry(bloc_Repertoire_Entre, width=72,textvariable=StringVar)

# BLOC SORTIE (Informations sur les fichiers sortie)
label_NomRep_Sortie = Label(bloc_Repertoir_Sortie, text='Répertoire de sortie des fichiers:')
label_Rep_Sortie = Entry(bloc_Repertoir_Sortie, width=45,textvariable=StringVar)
label_FileName1 = Label(bloc_Repertoir_Sortie, text='Fichier de sortie Neocase :')
label_ChampFile1 = Entry(bloc_Repertoir_Sortie, width=20, textvariable=StringVar)
label_ChampFile1.insert(0, "SELOGER_contact")
label_FileName2 = Label(bloc_Repertoir_Sortie, text='Fichier de sortie Elevo :')
label_ChampFile2 = Entry(bloc_Repertoir_Sortie, width=20, textvariable=StringVar)
label_ChampFile2.insert(0, "SELOGER_elevo")
label_FileName3 = Label(bloc_Repertoir_Sortie, text='Fichier de sortie Place de la formation :')
label_ChampFile3 = Entry(bloc_Repertoir_Sortie, width=20, textvariable=StringVar,)
label_ChampFile3.insert(0, "Default_text")
labelSeparateur = Label(bloc_Separateur,text = "Faite le choix.")
# BLOC SEPARATEUR

#                    ********* LES BOUTONS RADIO *********
var =IntVar()
rdioOne = Radiobutton(bloc_Separateur, text='Point-virgule', variable=var, value=1,command=Callback(selection, labelSeparateur, var))
rdioTwo = Radiobutton(bloc_Separateur, text='Virgule', variable=var, value=2,command=Callback(selection, labelSeparateur, var))
rdioThree = Radiobutton(bloc_Separateur, text='Pipe', variable=var, value=3,command=Callback(selection, labelSeparateur, var))

# label_Test = Label(frame_bas, width=55)
# label_Test.pack()
#                    ********* LES BOUTONS *********

Bouton_Ouvrir = Button(bloc_Repertoire_Entre, text="Ouvrir fichier", command = Callback(browseFiles, label_EntreFichier))
Bouton_Repertoire = Button(bloc_Repertoir_Sortie, text="Répertoire", command = Callback(open_folder, label_Rep_Sortie))

# Bouton_Convertir = Button(frame_Droite_du_Centre, text="Convertir", width=8, command = Callback(valideFile,label_ChampFile1, label_ChampFile2,label_ChampFile3, label_Test))
Bouton_Convertir = Button(frame_Droite_du_Centre, text="Convertir", width=10, command = Callback(valideFile,label_ChampFile1, label_ChampFile2, label_ChampFile3))




#===================================================================================
#                             AFFICHAGE DES WIDGETS
#===================================================================================

frame_Haut.pack()
frame_Centre.pack()
frame_bas.pack()

bloc_Repertoire_Entre.pack()
bloc_Repertoir_Sortie.pack()
bloc_Separateur.grid(row=0, column=0, sticky="S")

frame_Gauche_du_Centre.grid(row=0, column=0)
frame_Centre_du_Bas.grid(row=0, column=1)
frame_Droite_du_Centre.grid(row=0, column=2)

label_NomFichier.grid(row=0, column=0,padx=8, pady=3)
label_EntreFichier.grid(row=0, column=1,padx=8)

label_NomRep_Sortie.grid(row=0, column=0)
label_Rep_Sortie.grid(row=1, columnspan=2, sticky="EW", padx=4)

label_FileName1.grid(row=2, column=0, pady=3,sticky="W")
label_ChampFile1.grid(row=2, column=1)

label_FileName2.grid(row=3, column=0, pady=3,sticky="W")
label_ChampFile2.grid(row=3, column=1)

label_FileName3.grid(row=4, column=0, pady=3,sticky="W")
label_ChampFile3.grid(row=4, column=1)

# label_Separateur.grid(column=0, row=3, sticky="W")

Bouton_Ouvrir.grid(row=1, column=1, sticky="e")
Bouton_Repertoire.grid(row=1, column=2, sticky="e")
Bouton_Convertir.grid(row=2, column=0, sticky="N",pady=10)

rdioOne.grid(column=0, row=0, sticky="W")
rdioTwo.grid(column=0, row=1, sticky="W")
rdioThree.grid(column=0, row=2, sticky="W")
labelSeparateur.grid(column=0, row=3, sticky="W")

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
Fenetre.mainloop()
