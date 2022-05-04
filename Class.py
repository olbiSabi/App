#!/usr/bin/env python
#coding: utf-8

class Personne:
    """Classe définissant une personne cractérisée par
    -son nom
    -son prenom
    -son âge
    -son lieu de résidence"""
    
    def __init__(self):
        self.nom = "Oniankitan"
        self.prenom = "Sabi"
        self.age = "31"
        self.lieu_Naissance = "Sabi"

olbi = Personne()
print(olbi.nom)