from tkinter import *

# création de la fenêtre principale
fenetre = Tk()

grille = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

grillePoint = [
    [1, 3, 5, 3, 1],
    [3, 10, 10, 10, 3],
    [5, 10, 11, 10, 5],
    [3, 10, 10, 10, 3],
    [1, 3, 5, 3, 1]
]

compteur = 0
# initialisation des pions
pionJ1 = PhotoImage(file="bleu.png")
pionJ2 = PhotoImage(file="orange.png")
caseVide = PhotoImage(file="vide.png")

labels = [
    [Button, Button, Button, Button, Button],
    [Button, Button, Button, Button, Button],
    [Button, Button, Button, Button, Button],
    [Button, Button, Button, Button, Button],
    [Button, Button, Button, Button, Button]
]

NOMBRE_DE_LIGNES = 5
NOMBRE_DE_COLONNES = 5

LISTE_DEPLACEMENT_POSSIBLE_J1 = []

## IA MIN MAX ##
def minmax(node, depth, originalDepth, est_IA):
    noeud = None
    value = -5000
    estNoeudTerm = False


    if node:
        i = node[1][0]
        j = node[1][1]
        if node[0]:
            i_source = node[0][0]
            j_source = node[0][1]
            grille[i_source][j_source] = 0
        if est_IA:
            grille[i][j] = 1
        else:
            grille[i][j] = 2


    if depth <= 0 or combinaisonGagnante(grille, 1) or combinaisonGagnante(grille, 2):
        value = evalGrid()
        estNoeudTerm = True
        #print(eval)
    #print("############")
    #print(getAllEnfant(grille, node, est_IA))
    #print("############")

    if est_IA and not estNoeudTerm:
        value = -1000
        #print("__________")
        #afficherGrille(grille)
        #print("tzst : ", getAllEnfant(grille, node, est_IA))
        for enfant in getAllEnfant(grille, node, est_IA):
            valueEnfant = max(value, minmax(enfant[0], depth - 1, originalDepth, False))
            #print("Value : ", value)
            #print("Value enfant : ", valueEnfant)
            if value < valueEnfant:
                value = valueEnfant
                #print("value 2 : ", value)
                noeud = enfant
    elif not est_IA and not estNoeudTerm:
        value = 1000
        for enfant in getAllEnfant(grille, node, est_IA):
            valueEnfant = min(value, minmax(enfant[0], depth - 1, originalDepth, True))
            if value > valueEnfant:
                value = valueEnfant
                noeud = enfant

    if node:
        grille[i][j] = 0
        if node[0]:
            if est_IA:
                grille[i_source][j_source] = 1
            else:
                grille[i_source][j_source] = 2


    if estNoeudTerm:
        return value


    #print("-------------")
    #afficherGrille(grille)
    #print(depth, value)
    #if noeud:
        #print(noeud)

    if depth == originalDepth:
        return noeud
    ## faire remonter les coord ##
    return value

def evalGrid():
    if combinaisonGagnante(grille, 2):
        return 20000
    elif combinaisonGagnante(grille, 1):
        return -10000
    else:
        return sommePion(2) - sommePion(1)

def sommePion(joueur):
    res = 0
    for x in range(5):
        for y in range(5):
            if grille[x][y] == joueur:
                res += grillePoint[x][y]
    #print("RESULTAT POINT : ", res, " joueur : ", joueur)
    return res

def getAllEnfant(grille, node, estIA):
    # format de la liste [[is,js,id,jd],]
    global compteur
    tempListePosPossible = list()
    if compteur < 9:
        for i in range(5):
            for j in range(5):
                if grille[i][j] == 0:
                    tempListePosPossible.append([[(None), (i, j)]])
        return tempListePosPossible
    else:
        if estIA:
            listPion = getPion(2)
            for pion in listPion:
                #print("VOISINS : ", voisinsPion(grille,getPion(2)[i]))
                vp = voisinsPion(grille, pion)
                if len(vp) != 0:
                    tempListePosPossible.append(voisinsPion(grille, pion))
            # deplacement possible pour chaque destination

            return tempListePosPossible
        else:
            listPion = getPion(1)
            for pion in listPion:
                vp = voisinsPion(grille, pion)
                if len(vp) != 0:
                    tempListePosPossible.append(voisinsPion(grille, pion))
            # deplacement possible pour chaque destination
            return tempListePosPossible

def getTotalPionOnGrid():
    tot = 0
    for x in range(5):
        for y in range(5):
            if grille[x][y] != 0:
                tot += 1
    return tot

# OK
# définir les combinaisons gagnantes signifiant l'arret de la partie
def combinaisonGagnante(grille, joueur):
    # Verticale
    for l in range(NOMBRE_DE_LIGNES - 3):
        for c in range(NOMBRE_DE_COLONNES):
            if grille[l][c] == joueur and grille[l + 1][c] == joueur and grille[l + 2][c] == joueur and grille[l + 3][
                c] == joueur:
                etat = True
                return etat

    # Horizontale
    for l in range(NOMBRE_DE_LIGNES):
        for c in range(NOMBRE_DE_COLONNES - 3):
            if grille[l][c] == joueur and grille[l][c + 1] == joueur and grille[l][c + 2] == joueur and grille[l][
                c + 3] == joueur:
                etat = True
                return etat

    # Diagonale positive
    for l in range(3, NOMBRE_DE_LIGNES):
        for c in range(NOMBRE_DE_COLONNES - 3):
            # print(grille[l][c], grille[l - 1][c + 1], grille[l - 2][c + 2], grille[l - 3][c + 3])
            if grille[l][c] == joueur and grille[l - 1][c + 1] == joueur and grille[l - 2][c + 2] == joueur and \
                    grille[l - 3][c + 3] == joueur:
                etat = True
                return etat

    # Diagonale négative
    for l in range(NOMBRE_DE_LIGNES - 3):
        for c in range(NOMBRE_DE_COLONNES - 3):
            if grille[l][c] == joueur and grille[l + 1][c + 1] == joueur and grille[l + 2][c + 2] == joueur and \
                    grille[l + 3][c + 3] == joueur:
                etat = True
                return etat

    # Carré
    for l in range(NOMBRE_DE_LIGNES - 1):
        for c in range(NOMBRE_DE_COLONNES - 1):
            if grille[l][c] == joueur and grille[l + 1][c] == joueur and grille[l][c + 1] == joueur and grille[l + 1][
                c + 1] == joueur:
                etat = True
                return etat
    etat = False
    return etat

# déterminer voisins disponibles d'un joueur
def voisinsPion(grille, pion):
    liste = []
    indexASuppr = []

    ligne = pion[0]
    colonne = pion[1]

    indexASuppr.clear()
    liste.clear()
    # calculer voisins d'un pion
    if ligne - 1 >= 0:
        liste.append((ligne - 1, colonne))
        if colonne - 1 >= 0:
            liste.append((ligne - 1, colonne - 1))
        if colonne + 1 <= 4:
            liste.append((ligne - 1, colonne + 1))

    if colonne - 1 >= 0:
        #liste.append([(ligne, colonne), (ligne, colonne - 1)])
        liste.append((ligne, colonne - 1))
    if colonne + 1 <= 4:
        liste.append((ligne, colonne + 1))

    if ligne + 1 <= 4:
        liste.append((ligne + 1, colonne))
        if colonne - 1 >= 0:
            liste.append((ligne + 1, colonne - 1))
        if colonne + 1 <= 4:
            liste.append((ligne + 1, colonne + 1))

    # la liste d'un pion ne contient que les déplacements possibles
    indice = 0, 0
    for voisin in range(len(liste)):
        x = liste[voisin][0]
        y = liste[voisin][1]
        indice = x, y
        if grille[x][y] != 0:
            indexASuppr.append(indice)

    if len(indexASuppr) != 0:
        for element in indexASuppr:
            liste.remove(element)

    newListe = list()

    for i in range(len(liste)):
        newListe.append([(ligne, colonne), liste[i]])

    return newListe

def getPion(joueur):
    pions = list()
    for i in range(5):
        for j in range(5):
            if grille[i][j] == joueur:
                pions.append((i,j))
    return pions

## FIN IA MIN MAX ##

# afficher grille terminal
def afficherGrille(grille):
    for x in grille:
        for elem in x:
            print(elem, end=' ')
        print()

# affichage graphique du plateau en fonction des éléments du tableau 2d grille
def dessinerPlateau():
    cpt = 0
    for ligne in range(5):
        for colonne in range(5):
            if grille[ligne][colonne] == 1:
                #J1Lab = Button(fenetre, image=pionJ1, command=lambda m=(ligne, colonne): recupCoord(m))
                J1Lab = Button(fenetre, image=pionJ1)
                J1Lab.grid(row=ligne, column=colonne)
                #J1Lab = Label(fenetre, cursor="plus", image=pionJ1, borderwidth=1)
                #J1Lab.grid(row=ligne, column=colonne)
                labels[ligne][colonne] = J1Lab
                cpt += 1
                # labels.append(Label(fenetre, image=pionJ1, borderwidth=1))
                # Label(fenetre, image=pionJ1, borderwidth=1).grid(row=ligne, column=colonne)
            elif grille[ligne][colonne] == 2:
                J2Lab = Button(fenetre, image=pionJ2)
                J2Lab.grid(row=ligne, column=colonne)
                #J2Lab = Button(fenetre, image=pionJ2, command=lambda m=(ligne, colonne): recupCoord(m))
                #J2Lab.grid(row=ligne, column=colonne)
                #J2Lab = Label(fenetre, cursor="plus", image=pionJ2, fg='white', borderwidth=1)
                #J2Lab.grid(row=ligne, column=colonne)
                labels[ligne][colonne] = J2Lab
                cpt += 1
            else:
                #J3Lab = Button(fenetre, image=caseVide, command=lambda m=(ligne, colonne): recupCoord(m))
                #J3Lab.grid(row=ligne, column=colonne)
                J3Lab = Button(fenetre, image=caseVide)
                J3Lab.grid(row=ligne, column=colonne)
                #J3Lab = Label(fenetre, image=caseVide, borderwidth=1)
                #J3Lab.grid(row=ligne, column=colonne)
                labels[ligne][colonne] = J3Lab
                cpt += 1
    # mise à jour de la fenêtre
    fenetre.update()

def premiersTours():
    dessinerPlateau()
    cpt = 0
    joueur = 1
    global compteur
    while cpt < 8:
        cpt += 1
        compteur = cpt
        print("c'est au joueur", joueur, " de jouer ! ")
        while joueur == 1:
            try:
                L = int(input("Ligne (1-5): ")) - 1
                C = int(input("Colonne (1-5): ")) - 1
                break
            except:
                print("La valeur entrée n'est pas un nombre")
        while grille[L][C] != 0 and joueur == 1:
            print("Cette position est déjà prise, veuillez en choisir une autre")
            L = int(input("Ligne (1-5 : ")) - 1
            C = int(input("Colonne (1-5): ")) - 1
        #print("Joueur : ", joueur)
        if joueur == 1:
            grille[L][C] = 1
            #voisinsPion(grille, (L, C), L, C)
            #CPTJ1.append((L, C))
            #deplacementPossibleJ1(grille, CPTJ1)
            joueur = 2
            dessinerPlateau()
            afficherGrille(grille)
            if combinaisonGagnante(grille, 1):
                gagnant = 1
                print("Le gagnant est : ", gagnant)
                dessinerPlateau()
                return gagnant
        elif joueur == 2:
            print(minmax(None, 3, 3, True))
            if minmax(None, 3, 3, True) == None:
                print("test")
            #assigner meilleur coup dans la grille
            coord = minmax(None, 3, 3, True)[0][1]
            x = coord[0]
            y = coord[1]
            print(x,y)
            grille[x][y] = 2
            afficherGrille(grille)
            dessinerPlateau()
            joueur = 1

def partieEnCours2():
    premiersTours()
    global compteur
    compteur += 1
    dessinerPlateau()
    joueur = 1
    while not combinaisonGagnante(grille, 1) and not combinaisonGagnante(grille, 2):
        print("________DEBUT BOUCLE ________")
        deplacementPossibleJ1(grille, getPion(1))
        print("________DEBUT BOUCLE ________")
        if joueur == 1:
            # déplacement possible
            deplacementPossibleJ1(grille, getPion(1))

            print("________________")
            print("Déplacer un pion")
            print("________________")
            print("Pions disponibles : ", getPion(1))
            L = int(input("Ligne (1-5) : ")) - 1
            C = int(input("Colonne (1-5): ")) - 1
            while (L, C) not in getPion(1):
                print("Pions disponibles : ", getPion(1))
                L = int(input("Ligne (1-5) : ")) - 1
                C = int(input("Colonne (1-5): ")) - 1
            pion = getPion(1).index((L, C))
            pion = pion*2
            print("Le déplacer sur ? ")
            #recupererPion(grille,1)
            print("Déplacement possibles : ", LISTE_DEPLACEMENT_POSSIBLE_J1[pion+1])
            X = int(input("Ligne (1-5) : ")) - 1
            Y = int(input("Colonne (1-5): ")) - 1
            print(LISTE_DEPLACEMENT_POSSIBLE_J1)
            while (X, Y) not in LISTE_DEPLACEMENT_POSSIBLE_J1[pion + 1]:
                X = int(input("Ligne (1-5) : ")) - 1
                Y = int(input("Colonne (1-5): ")) - 1
            print("OK")
            joueur = 2
            grille[X][Y] = 1
            grille[L][C] = 0
            #recupererPion(grille, 1)
            print("Liste des pions J1 : ", getPion(1))
            #deplacementPossibleJ1(grille,CPTJ1)
            print("Déplacement possibles : ", LISTE_DEPLACEMENT_POSSIBLE_J1)
            dessinerPlateau()
            afficherGrille(grille)

            print("fin J1")

        else:
            print("GET PION : ", getPion(1))
            for pion in getPion(1):
                LISTE_DEPLACEMENT_POSSIBLE_J1.append((pion, [voisinsPionJ1(grille, pion)]))
            print("LISTE DEPL : ", LISTE_DEPLACEMENT_POSSIBLE_J1)


            getPion(2)
            print("MIN MAX : ", minmax(None, 4, 4, True))
            coordOrigin = minmax(None, 4, 4, True)[0][0]
            coordDestination = minmax(None, 4, 4, True)[0][1]
            print("Origin : ", coordOrigin)
            print("Destination : ", coordDestination)

            x = coordOrigin[0]
            y = coordOrigin[1]

            i = coordDestination[0]
            j = coordDestination[1]

            grille[i][j] = 2
            grille[x][y] = 0

            dessinerPlateau()
            joueur = 1

# déterminer voisins disponibles d'un joueur
def voisinsPionJ1(grille, pion):
    liste = []
    indexASuppr = []

    ligne = pion[0]
    colonne = pion[1]

    indexASuppr.clear()
    liste.clear()
    # calculer voisins d'un pion
    if ligne - 1 >= 0:
        liste.append((ligne - 1, colonne))
        if colonne - 1 >= 0:
            liste.append((ligne - 1, colonne - 1))
        if colonne + 1 <= 4:
            liste.append((ligne - 1, colonne + 1))

    if colonne - 1 >= 0:
        liste.append((ligne, colonne - 1))
    if colonne + 1 <= 4:
        liste.append((ligne, colonne + 1))

    if ligne + 1 <= 4:
        liste.append((ligne + 1, colonne))
        if colonne - 1 >= 0:
            liste.append((ligne + 1, colonne - 1))
        if colonne + 1 <= 4:
            liste.append((ligne + 1, colonne + 1))

    # la liste d'un pion ne contient que les déplacements possibles
    indice = 0, 0
    for voisin in range(len(liste)):
        x = liste[voisin][0]
        y = liste[voisin][1]
        indice = x, y
        if grille[x][y] != 0:
            indexASuppr.append(indice)

    if len(indexASuppr) != 0:
        for element in indexASuppr:
            liste.remove(element)
    return liste

def deplacementPossibleJ1(grille, pionjoueur):
    LISTE_DEPLACEMENT_POSSIBLE_J1.clear()
    for i in range(len(pionjoueur)):
        LISTE_DEPLACEMENT_POSSIBLE_J1.append(pionjoueur[i])
        LISTE_DEPLACEMENT_POSSIBLE_J1.append(voisinsPionJ1(grille, pionjoueur[i]))
    return LISTE_DEPLACEMENT_POSSIBLE_J1

