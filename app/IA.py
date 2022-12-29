import random
from tkinter import *

grille = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

grillePoint = [
    [1, 3, 5, 3, 1],
    [3, 5, 10, 5, 3],
    [5, 7, 11, 7, 5],
    [3, 5, 10, 5, 3],
    [1, 3, 5, 3, 1]
]

grillePointV2 = [
    [10, 3, 5, 3, 10],
    [3, 7, 10, 7, 3],
    [5, 7, 1, 7, 5],
    [3, 7, 10, 7, 3],
    [10, 3, 5, 3, 10]
]

compteur = 0
etat = False

NOMBRE_DE_LIGNES = 5
NOMBRE_DE_COLONNES = 5

LISTE_DEPLACEMENT_POSSIBLE_J1 = []


# IA MIN MAX
# Noeud de départ, profondeur, profondeur identique à celle précédente, boolean est_IA
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

    # si la profondeur max est atteinte ou combinaison gagnante, on fait remonter le noeud
    if depth <= 0 or combinaisonGagnante(grille, 1) or combinaisonGagnante(grille, 2):
        value = evalGrid()
        estNoeudTerm = True

    # si c'est au tour de l'IA
    if est_IA and not estNoeudTerm:
        value = -10001

        # Pour chaque enfant du noeud, on prend la valeur la plus élevé = on maximise nos gains
        for enfant in getAllEnfant(grille, node, est_IA):
            valueEnfant = max(value, minmax(enfant[0], depth - 1, originalDepth, False))

            # si la valeur est inférieur à celle de l'enfant, on prend la plus grande
            # on récupère les coordonnées du noeud associé à la valeur
            if value < valueEnfant:
                value = valueEnfant
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

    if depth == originalDepth or combinaisonGagnante(grille, 1) or combinaisonGagnante(grille, 2):
        return noeud

    if estNoeudTerm:
        return value

    ## faire remonter les coord ##
    return value


# évaluer les scores de chaque joueur
def evalGrid():
    from controller import etat
    global etat

    # si l'IA gagne, on retourne une valeur très haute
    if combinaisonGagnante(grille, 2):
        return 20000

    # si le joueur gagne, on retourne une valeur très basse
    elif combinaisonGagnante(grille, 1):
        return -20000
    else:
        from controller import compteur
        global compteur
        compteur = compteur

        # si nous sommes dans les tours de placement
        # on calcule la différence de points entre les pions IA / joueur
        if compteur < 9:
            return sommePion(2, grillePoint) - sommePion(1, grillePoint)

        # si nous sommes dans les tours de déplacement et que c'est un IAvsIA
        # on change la grille des points de manière aléatoire
        # => pour avoir un gagnant, sinon les déplacements tournent en boucle
        elif compteur >= 9 and etat == True:
            for i in range(5):
                for j in range(5):
                    grillePointV2[i][j] = random.randint(1, 30)
            return sommePion(2, grillePointV2) - sommePion(1, grillePointV2)

        # si nous sommes dans les tours de déplacement et que c'est joueur contre IA
        # on calcule la différence de points entre les pions IA / joueur
        elif compteur >= 9 and etat == False:
            return sommePion(2, grillePoint) - sommePion(1, grillePoint)

# alph béta, ne fonctionne pas
def alphabeta(node, alpha, beta, estIA, depth):
    noeud = None
    valeur = -5000
    estNoeudTerm = False

    if node:
        print(node[0][1])
        i = node[0][1][0]
        j = node[0][1][1]
        if node[0][0]:
            i_source = node[0][0][0]
            j_source = node[0][0][1]
            grille[i_source][j_source] = 0

    # si noeud terminal, on retourne le noeud
    if depth == 0 or combinaisonGagnante(grille, 1) or combinaisonGagnante(grille, 2):
        return node
    else:
        # si c'est le joueur qui joue
        if not estIA:
            valeur = 2000
            # on parcourt les enfants du noeud
            for enfant in getAllEnfant(grille, node, False):
                # on cherche à minimiser ses gains
                valeur = min(valeur, alphabeta(enfant, alpha, beta, False, depth-1))
                # coupure alpha / beta
                if alpha >= valeur:
                    return valeur
                beta = min(beta, valeur)
        else:
            # si c'est l'IA qui joue
            valeur = -2000
            for enfant in getAllEnfant(grille,node, True):
                # on cherche à maximiser ses gains
                valeur = max(valeur, alphabeta(enfant, alpha, beta, True, depth-1))
                if valeur >= beta:
                    return valeur
                alpha = max(alpha, valeur)

    return valeur


# calculer le nombre de point pour chaque joueur en fonction des pions placés
def sommePion(joueur, grillePoint):
    res = 0
    for x in range(5):
        for y in range(5):
            if grille[x][y] == joueur:
                res += grillePoint[x][y]
    return res


# récupérer tous les enfants d'un noeud
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
    # on supprime les voisins qui sont des pions
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


# obtenir tous les pions d'un joueur
def getPion(joueur):
    pions = list()
    for i in range(5):
        for j in range(5):
            if grille[i][j] == joueur:
                pions.append((i,j))
    return pions


# déterminer voisins disponibles de J1
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
    # on enlève les voisins si c'est un pion
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

# déplacement possible pour J1
def deplacementPossibleJ1(grille, pionjoueur):
    LISTE_DEPLACEMENT_POSSIBLE_J1.clear()
    for i in range(len(pionjoueur)):
        LISTE_DEPLACEMENT_POSSIBLE_J1.append(pionjoueur[i])
        LISTE_DEPLACEMENT_POSSIBLE_J1.append(voisinsPionJ1(grille, pionjoueur[i]))
    return LISTE_DEPLACEMENT_POSSIBLE_J1

