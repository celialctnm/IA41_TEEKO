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
labels = []
for i in range(25):
    labels.append(Label)

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
                labels[cpt] = J1Lab
                cpt += 1
                # labels.append(Label(fenetre, image=pionJ1, borderwidth=1))
                # Label(fenetre, image=pionJ1, borderwidth=1).grid(row=ligne, column=colonne)
            elif grille[ligne][colonne] == 2:
                J2Lab = Label(fenetre, cursor="plus", image=pionJ2, fg='white', borderwidth=1)
                J2Lab.grid(row=ligne, column=colonne)
                labels[cpt] = J2Lab
                cpt += 1
            else:
                J3Lab = Label(fenetre, image=caseVide, borderwidth=1)
                J3Lab.grid(row=ligne, column=colonne)
                labels[cpt] = J3Lab
                cpt += 1
    # mise à jour de la fenêtre
    # print(labels)
    fenetre.update()


# réalise une action lorsqu'un label est cliqué
def mouseClick(event):
    print("mouse clicked")

    # ajouter les labels cliqués dans une liste
    touchPress.append(event.widget)

    pion1 = Label
    caseVide = Label

    t = labels.index(touchPress[0])
    print(t)
    print(labels[t])

    # si deux labels sont cliqués, ils devront être interveti, le pion prendrait la place de la case vide
    if len(touchPress) == 2:
        pion1 = touchPress[0]
        caseVide = touchPress[1]
        # fonction pour déplacer les pions en fonction des deux cases selectionnées
        print(caseVide,pion1)
        touchPress.clear()
    


# rend les labels clickables à l'aide la souris
def labelClickable():
    for label in labels:
        label.bind("<Button-1>", mouseClick)
