import tkinter

import numpy
import numpy as np
from tkinter import *

# création de la fenêtre principale
fenetre = Tk()

# création du plateau de jeu
grille = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# initialisation des pions
pionJ1 = PhotoImage(file="bleu.png")
pionJ2 = PhotoImage(file="orange.png")
caseVide = PhotoImage(file="vide.png")

# liste labels
#labels = []

labels = [
    [Label, Label, Label, Label, Label],
    [Label, Label, Label, Label, Label],
    [Label, Label, Label, Label, Label],
    [Label, Label, Label, Label, Label],
    [Label, Label, Label, Label, Label]
]
#for i in range(25):
    #labels.append(Label)

# liste label cliqué
touchPress = []


# affichage graphique du plateau en fonction des éléments du tableau 2d grille
def dessinerPlateau():
    cpt = 0
    for ligne in range(5):
        for colonne in range(5):
            if grille[ligne][colonne] == 1:
                J1Lab = Label(fenetre, cursor="plus", image=pionJ1, borderwidth=1)
                J1Lab.grid(row=ligne, column=colonne)
                labels[ligne][colonne] = J1Lab
                cpt += 1
                # labels.append(Label(fenetre, image=pionJ1, borderwidth=1))
                # Label(fenetre, image=pionJ1, borderwidth=1).grid(row=ligne, column=colonne)
            elif grille[ligne][colonne] == 2:
                J2Lab = Label(fenetre, cursor="plus", image=pionJ2, fg='white', borderwidth=1)
                J2Lab.grid(row=ligne, column=colonne)
                labels[ligne][colonne] = J2Lab
                cpt += 1
            else:
                J3Lab = Label(fenetre, image=caseVide, borderwidth=1)
                J3Lab.grid(row=ligne, column=colonne)
                labels[ligne][colonne] = J3Lab
                cpt += 1
    # mise à jour de la fenêtre
    # print(labels)
    fenetre.update()


# réalise une action lorsqu'un label est cliqué
def mouseClick(event):
    etat = False
    print("mouse clicked")
    print(event.widget)
    for i in range(5):
        for x in range(5):
            if labels[i][x] == event.widget:
                if grille[i][x] == 0:
                    print(i,x)
                    grille[i][x] = joueurActuel
                    dessinerPlateau()
                    etat = True
                    return grille
            else:
                labelClickable(joueurActuel)
    return etat


joueurActuel = 1
# rend les labels clickables à l'aide la souris
def labelClickable(joueur):
    joueurActuel = joueur
    for i in range(5):
        for x in range(5):
            labels[i][x].bind("<Button-1>", mouseClick)
