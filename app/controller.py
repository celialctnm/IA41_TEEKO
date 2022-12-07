import modele

grille = modele.grille
gagnant = "gagnant"
NOMBRE_DE_LIGNES = 5
NOMBRE_DE_COLONNES = 5


# définir les combinaisons gagnantes signifiant l'arret de la partie
def combinaisonGagnante(grille, joueur):
    #Verticale
    for l in range(NOMBRE_DE_LIGNES-3):
        for c in range(NOMBRE_DE_COLONNES):
            if grille[l][c] == joueur and grille[l+1][c] == joueur and grille[l+2][c] == joueur and grille[l+3][c] == joueur:
                etat = True
                return etat

    #Horizontale
    for l in range(NOMBRE_DE_LIGNES):
        for c in range(NOMBRE_DE_COLONNES-3):
            if grille[l][c] == joueur and grille[l][c+1] == joueur and grille[l][c+2] == joueur and grille[l][c+3] == joueur:
                etat = True
                return etat

    #Diagonale positive
    for l in range(3, NOMBRE_DE_LIGNES):
        for c in range(NOMBRE_DE_COLONNES-3):
            print(grille[l][c],grille[l - 1][c + 1],grille[l - 2][c + 2],grille[l - 3][c + 3])
            if grille[l][c] == joueur and grille[l-1][c+1] == joueur and grille[l-2][c+2] == joueur and grille[l-3][c+3] == joueur:
                etat = True
                return etat

    #Diagonale négative
    for l in range(NOMBRE_DE_LIGNES-3):
        for c in range(NOMBRE_DE_COLONNES-3):
            if grille[l][c] == joueur and grille[l+1][c+1] == joueur and grille[l+2][c+2] == joueur and grille[l+3][c+3] == joueur:
                etat = True
                return etat

    #Carré
    for l in range(NOMBRE_DE_LIGNES-1):
        for c in range(NOMBRE_DE_COLONNES-1):
            if grille[l][c] == joueur and grille[l+1][c] == joueur and grille[l][c+1] == joueur and grille[l+1][c+1] == joueur:
                etat = True
                return etat

    etat = False
    return etat


# mise en place des 8 pions en début de partie
def quatrePremierTour():
    cpt = 0
    joueurActuel = "J1"
    while cpt < 8:
        cpt += 1
        print("C'est à " + joueurActuel + " de jouer")
        while True:
            try:
                L = int(input("Ligne (1-5): "))-1
                C = int(input("Colonne (1-5): "))-1
                break
            except:
                print("La valeur entrée n'est pas un nombre")
        while grille[L][C] != 0:
            print("Cette position est déjà prise, veuillez en choisir une autre")
            L = int(input("Ligne (1-5 : "))-1
            C = int(input("Colonne (1-5): "))-1
        if joueurActuel == "J1":
            grille[L][C] = 1
            joueurActuel = "J2"
            if combinaisonGagnante(modele.grille, 1):
                gagnant = "J1"
                print("Le gagnant est : " + gagnant)
                modele.dessinerPlateau()
                break
        else:
            modele.grille[L][C] = 2
            joueurActuel = "J1"
            if combinaisonGagnante(modele.grille, 2):
                gagnant = "J2"
                print("Le gagnant est : " + gagnant)
                modele.dessinerPlateau()
                break
        print(grille)
        modele.dessinerPlateau()

        # continuer la partie si aucune combinaison gagnante
        if combinaisonGagnante(modele.grille, 1):
            gagnant = "J1"
            print("Le gagnant est : " + gagnant)
        elif combinaisonGagnante(modele.grille, 2):
            gagnant = "J2"
            print("Le gagnant est : " + gagnant)
        else:
            partieEnCours()


def partieEnCours():
    # Etude des cas de chaque joueur
        # Choisir quel pion à déplacer

        # choisir le déplacement du pion

    return grille
     # 3 fonctions de déplacement
     # Se déplacer horizontalement droit et gauche
def deplacerHorizontalementàgauche(grille, joueur):
             for l in range (NOMBRE_DE_LIGNES):
                 for n in range(NOMBRE_DE_COLONNES):
                     grille[l][n] = grille[l][n - 1];
                     grille[l][n - 1] = 0;
def deplacerHorizontalementàdroite(grille ,joueur):
             for l in range(NOMBRE_DE_LIGNES):
                 for n in range(NOMBRE_DE_COLONNES):
                         grille[l][n] = grille[l][n + 1];
                         grille[l][n + 1]=0;
    # Se déplacer verticalement bas et haut
def deplacerVerticalementàdroite(grille,joueur):
            for l in range(NOMBRE_DE_LIGNES):
                for n in range(NOMBRE_DE_COLONNES):
                    grille[l][n] =grille[l+1][n]
                    grille[l+1][n]=0;
def deplacerVerticalementàgauche(grille,joueur):
        for l in range(NOMBRE_DE_LIGNES):
             for n in range(NOMBRE_DE_COLONNES):
                 grille[l][n] = grille[l - 1][n];
                 grille[l - 1][n] = 0;
          # Se déplacer diagonalement ligne supérieure et inférieure
          # en haut à gauche
def deplacerDiagoalementHautàgauche(grille,joueur):
        for l in range(NOMBRE_DE_LIGNES):
            for n in range(NOMBRE_DE_COLONNES):
                grille[l][n] = grille[l + 1][n-1];
                grille[l + 1][n - 1]=0;
          # en haut à droite
def deplacerDiagoalementHautàdroite(grille,joueur):
            for l in range(NOMBRE_DE_LIGNES):
                for n in range(NOMBRE_DE_COLONNES):
                    grille[l][n] = grille[l + 1][n + 1];
                    grille[l + 1][n + 1]=0;
          # en bas à droite
def deplacerDiagoalementBasàdroite(grille,joueur):
    for l in range(NOMBRE_DE_LIGNES):
        for n in range(NOMBRE_DE_COLONNES):
            grille[l][n] = grille[l - 1][n + 1];
            grille[l - 1][n + 1]=0;
          # en bas à gauche
def deplacerDiagoalementBasàgauche(grille,joueur):
    for l in range(NOMBRE_DE_LIGNES):
        for n in range(NOMBRE_DE_COLONNES):
            grille[l][n] = grille[l - 1][n - 1];
            grille[l - 1][n - 1]=0;