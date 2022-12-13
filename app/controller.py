import random

import modele

# OK
grille = modele.grille
gagnant = "gagnant"
NOMBRE_DE_LIGNES = 5
NOMBRE_DE_COLONNES = 5

# à vérifier
J1_DEPLACEMENTS_POSSIBLES = []
J2_DEPLACEMENTS_POSSIBLES = []

# à vérifier
LISTE_CP_J1 = []
LISTE_CP_J2 = []

# OK
# Liste des pions des 2 joueurs
CPTJ1 = []
CPTIA = []

# OK
# afficher les voisins pour chaque pion d'un joueur dans une liste
LISTE_DEPLACEMENT_POSSIBLE_IA = []
LISTE_DEPLACEMENT_POSSIBLE_J1 = []

grillePoint = [
    [1, 3, 5, 3, 1],
    [3, 10, 10, 10, 3],
    [5, 10, 10, 10, 5],
    [3, 10, 10, 10, 3],
    [1, 3, 5, 3, 1]
]


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


def premiersTours():
    cpt = 0
    joueur = 1
    while cpt < 8:
        cpt += 1
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
            modele.dessinerPlateau()
            afficherGrille(grille)
            if combinaisonGagnante(modele.grille, 1):
                gagnant = 1
                print("Le gagnant est : ", gagnant)
                modele.dessinerPlateau()
                return gagnant
        elif joueur == 2:
            IA(grille)
            modele.dessinerPlateau()
            joueur = 1
            # modele.grille[x][y] = 2
            # voisinsPion(grille, (x, y), x, y)
            joueurActuel = "J1"


def partieEnCours():
    premiersTours()
    joueur = 1
    while not combinaisonGagnante(grille, 1) and not combinaisonGagnante(grille, 2):
        recupererPion(grille, CPTJ1)

        if joueur == 1:
            recupererPion(grille, 1)
            print(LISTE_DEPLACEMENT_POSSIBLE_J1)
            print("________________")
            print("Déplacer un pion")
            print("________________")
            print("Pions disponibles : ", CPTJ1)
            L = int(input("Ligne (1-5) : ")) - 1
            C = int(input("Colonne (1-5): ")) - 1
            print("Pions de J1 : ", CPTJ1)
            while (L, C) not in CPTJ1:
                X = int(input("Ligne (1-5) : ")) - 1
                Y = int(input("Colonne (1-5): ")) - 1
            pion = CPTJ1.index((L, C))
            pion = pion*2
            print("Le déplacer sur ? ")
            recupererPion(grille,1)
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
            print("Liste des pions J1 : ", CPTJ1)
            #deplacementPossibleJ1(grille,CPTJ1)
            print("Déplacement possibles : ", LISTE_DEPLACEMENT_POSSIBLE_J1)
            modele.dessinerPlateau()
            afficherGrille(grille)

            print("fin J1")

        else:
            IA(grille)
            #modele.dessinerPlateau()
            #recupererPion(grille, 1)
            joueur = 1

# à vérifier
# mise en place des 8 pions en début de partie
def quatrePremierTour():
    cpt = 0
    joueurActuel = "J1"
    while cpt < 8:
        cpt += 1
        print("C'est à " + joueurActuel + " de jouer")
        while True:
            try:
                L = int(input("Ligne (1-5): ")) - 1
                C = int(input("Colonne (1-5): ")) - 1
                break
            except:
                print("La valeur entrée n'est pas un nombre")
        while grille[L][C] != 0:
            print("Cette position est déjà prise, veuillez en choisir une autre")
            L = int(input("Ligne (1-5 : ")) - 1
            C = int(input("Colonne (1-5): ")) - 1
        if joueurActuel == "J1":
            grille[L][C] = 1
            voisinsPion(grille, (L, C), L, C)
            CPTJ1.append((L, C))
            # deplacementPossible(grille, CPTJ1)
            joueurActuel = "J2"
            deplacementPossibleJ1(grille, CPTJ1)
            if combinaisonGagnante(modele.grille, 1):
                gagnant = "J1"
                print("Le gagnant est : " + gagnant)
                modele.dessinerPlateau()
                break
        else:
            IA(grille)
            # modele.grille[x][y] = 2
            # voisinsPion(grille, (x, y), x, y)
            joueurActuel = "J1"
            if combinaisonGagnante(modele.grille, 2):
                gagnant = "J2"
                print("Le gagnant est : " + gagnant)
                modele.dessinerPlateau()
                break
        afficheVariable()
        afficherGrille(grille)
        modele.dessinerPlateau()

        # continuer la partie si aucune combinaison gagnante
        if combinaisonGagnante(modele.grille, 1):
            gagnant = "J1"
            print("Le gagnant est : " + gagnant)
            return gagnant
        elif combinaisonGagnante(modele.grille, 2):
            gagnant = "J2"
            print("Le gagnant est : " + gagnant)
            return gagnant
    partieEnCours()

# OK
def recupererPion(grille, joueur):
    if joueur == 1:
        CPTJ1.clear()
        LISTE_DEPLACEMENT_POSSIBLE_J1.clear()
        for x in range(5):
            for y in range(5):
                if grille[x][y] == 1:
                    CPTJ1.append((x,y))
        deplacementPossibleJ1(grille,CPTJ1)
    return LISTE_DEPLACEMENT_POSSIBLE_J1


# déterminer voisins disponibles d'un joueur
def voisinsPion(grille, pion, ligne, colonne):
    liste = []
    indexASuppr = []

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
        #print("LEN : ", len(indexASuppr))
        #print("LISTE AV : ", liste)
        for element in indexASuppr:
            liste.remove(element)

            #del liste[indexASuppr.index(indice)]
            #print("LISTE AP : ", liste)
            #print("i : ", i)
            #print("liste : ", liste)
            #print("valeur index : ", int(indexASuppr[i]))
            #element_suppr = liste.pop(int(indexASuppr[i]))

    return liste


# déplacer pion
# si l'emplacement du pion à déplacer est dans les coups possibles du joueur
# alors déplacer le pion

# il faut min/max les points de l'IA et soustraire au joueur ? pourquoi ?


# déplacement possible pour chaque pion d'un joueur
# liste chaînée



# OK
def afficheVariable():
    print("__________________")
    print("Pions J1 : ", CPTJ1)
    print("Pions IA : ", CPTIA)
    print("Déplacement possible J1 : ", LISTE_DEPLACEMENT_POSSIBLE_J1)
    print("Déplacement possible IA : ", LISTE_DEPLACEMENT_POSSIBLE_IA)
    print("__________________")


def deplacementPossibles(grille, pionjoueur):
    LISTE_DEPLACEMENT_POSSIBLE_IA.append(pionjoueur[len(pionjoueur) - 1])
    #print("Déplacement possible IA : ",voisinsPion(grille, pionjoueur[len(pionjoueur) - 1], pionjoueur[len(pionjoueur) - 1][0],pionjoueur[len(pionjoueur) - 1][1]))
    LISTE_DEPLACEMENT_POSSIBLE_IA.append(
        voisinsPion(grille, pionjoueur[len(pionjoueur) - 1], pionjoueur[len(pionjoueur) - 1][0],
                    pionjoueur[len(pionjoueur) - 1][1]))

    return LISTE_DEPLACEMENT_POSSIBLE_IA


def deplacementPossibleJ1(grille, pionjoueur):
    for i in range(len(pionjoueur)):
        LISTE_DEPLACEMENT_POSSIBLE_J1.append(pionjoueur[i])
        LISTE_DEPLACEMENT_POSSIBLE_J1.append(voisinsPion(grille, pionjoueur[i], pionjoueur[i][0],pionjoueur[i][1]))
    return LISTE_DEPLACEMENT_POSSIBLE_J1


def fonctionTest():
    res2 = 0
    coord = (0, 0)
    for x in range(5):
        for y in range(5):
            # res2 = scoreIA(grille)
            if grille[x][y] == 2:
                res2 += grillePoint[x][y]

            res = grillePoint[x][y]
            if grille[x][y] == 0 and res2 < res:
                res2 = res
                #print("Coordonnées : ", "(", x, ",", y, ")")
                #print("Résultat : ", res)
                coord = x, y
    return coord


def scoreIA(grille):
    res = 0
    for x in range(5):
        for y in range(5):
            if grille[x][y] == 2:
                res += grillePoint[x][y]
    print("RESULTAT POINT IA : ", res)
    return res


# afficher grille terminal
def afficherGrille(grille):
    for x in grille:
        for elem in x:
            print(elem, end=' ')
        print()


# afficher liste des voisins d'un pion
def afficherVoisinJoueur(grille, joueur):
    print("Liste pions IA : ", joueur)
    print("Liste des coups possibles IA taille : ", len(grille), ", coups : ", grille)

    if len(grille) >= 8:
        for i in range(0, 8, 2):
            print(grille[i])


# IA au moment de placer un pion (4 premiers tour)
def IA(grille):
    coord = (0, 0)
    coord = (random.randint(0, 4), random.randint(0, 4))

    while grille[coord[0]][coord[1]] != 0:
        coord = (random.randint(0, 4), random.randint(0, 4))
    grille[coord[0]][coord[1]] = 2
    CPTIA.append(coord)
    deplacementPossibles(grille, CPTIA)

    return coord


# IA au moment de déplacer des pions
def IADeplacement(grille):
    coord = (0, 0)
    return coord


def deplacerHorizontalementàgauche(grille, joueur):
    for l in range(NOMBRE_DE_LIGNES):
        for n in range(NOMBRE_DE_COLONNES):
            grille[l][n] = grille[l][n - 1];
            grille[l][n - 1] = 0;


def deplacerHorizontalementàdroite(grille, joueur):
    for l in range(NOMBRE_DE_LIGNES):
        for n in range(NOMBRE_DE_COLONNES):
            grille[l][n] = grille[l][n + 1];
            grille[l][n + 1] = 0;


# Se déplacer verticalement bas et haut
def deplacerVerticalementàdroite(grille, joueur):
    for l in range(NOMBRE_DE_LIGNES):
        for n in range(NOMBRE_DE_COLONNES):
            grille[l][n] = grille[l + 1][n]
            grille[l + 1][n] = 0;


def deplacerVerticalementàgauche(grille, joueur):
    for l in range(NOMBRE_DE_LIGNES):
        for n in range(NOMBRE_DE_COLONNES):
            grille[l][n] = grille[l - 1][n];
            grille[l - 1][n] = 0;
    # Se déplacer diagonalement ligne supérieure et inférieure
    # en haut à gauche


def deplacerDiagoalementHautàgauche(grille, joueur):
    for l in range(NOMBRE_DE_LIGNES):
        for n in range(NOMBRE_DE_COLONNES):
            grille[l][n] = grille[l + 1][n - 1];
            grille[l + 1][n - 1] = 0;
    # en haut à droite


def deplacerDiagoalementHautàdroite(grille, joueur):
    for l in range(NOMBRE_DE_LIGNES):
        for n in range(NOMBRE_DE_COLONNES):
            grille[l][n] = grille[l + 1][n + 1];
            grille[l + 1][n + 1] = 0;


# en bas à droite
def deplacerDiagoalementBasàdroite(grille, joueur):
    for l in range(NOMBRE_DE_LIGNES):
        for n in range(NOMBRE_DE_COLONNES):
            grille[l][n] = grille[l - 1][n + 1];
            grille[l - 1][n + 1] = 0;
        # en bas à gauche


def deplacerDiagoalementBasàgauche(grille, joueur):
    for l in range(NOMBRE_DE_LIGNES):
        for n in range(NOMBRE_DE_COLONNES):
            grille[l][n] = grille[l - 1][n - 1];
            grille[l - 1][n - 1] = 0;
