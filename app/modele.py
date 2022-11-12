import numpy as np
from tkinter import *

# création de la fenêtre principale
fenetre = Tk()

# création du plateau de jeu
grille = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

# initialisation des pions
pionJ1 = PhotoImage(file="bleu.png")
pionJ2 = PhotoImage(file="orange.png")
caseVide = PhotoImage(file="vide.png")

# affichage graphique du plateau en fonction des éléments du tableau 2d grille
def dessinerPlateau():
    for ligne in range(5):
        for colonne in range(5):
            if grille[ligne][colonne] == 1:
                Label(fenetre, image=pionJ1, borderwidth=1).grid(row=ligne, column=colonne)
            elif grille[ligne][colonne] == 2:
                Label(fenetre,image=pionJ2, fg='white', borderwidth=1).grid(row=ligne, column=colonne)
            else:
                Label(fenetre, image=caseVide, borderwidth=1).grid(row=ligne, column=colonne)
            # mise à jour de la fenêtre
            fenetre.update()
