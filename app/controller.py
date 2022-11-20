import modele

grille = modele.grille
gagnant = "gagnant"


# définir les combinaisons gagnantes signifiant l'arret de la partie
def combinaisonGagnante():
    etat = False
    return etat


# mise en place des 8 pions en début de partie
def quatrePremierTour():
    cpt = 0
    joueurActuel = "J1"
    while cpt < 8:
        cpt += 1
        print("C'est à " + joueurActuel + " de jouer")
        L = int(input("Ligne : "))
        C = int(input("Colonne : "))
        while grille[L][C] != 0:
            print("Cette position est déjà prise, veuillez en choisir une autre")
            L = int(input("Ligne : "))
            C = int(input("Colonne : "))
        if joueurActuel == "J1":
            grille[L][C] = 1
            joueurActuel = "J2"
        else:
            modele.grille[L][C] = 2
            joueurActuel = "J1"
        print(grille)
        modele.dessinerPlateau()

        # continuer la partie si aucune combinaison gagnante
        if combinaisonGagnante():
            print("Le gagnant est : " + gagnant)
        else:
            partieEnCours()


def partieEnCours():
    return grille
