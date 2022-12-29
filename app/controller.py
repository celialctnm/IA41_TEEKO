import random

import IA
import pygame


grille = IA.grille
LISTE_DEPLACEMENT_POSSIBLE_J1 = IA.LISTE_DEPLACEMENT_POSSIBLE_J1

IA.compteur = 0
IA.etat = False

nbr = 0

#### INTERFACE GRAPH ####

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (55, 164, 222)
ORANGE = (245, 167, 66)

WIDTH = 45
HEIGHT = 45
MARGIN = 5

pygame.init()
WINDOW_SIZE = [255, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("TEEKO")

done = False
clock = pygame.time.Clock()

#### INTERFACE GRAPH ####


#dessiner grille de jeu
def dessinerGrille():

    for row in range(5):
        for column in range(5):
            color = WHITE
            if grille[row][column] == 1:
                color = BLUE
            elif grille[row][column] == 2:
                color = ORANGE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])


# joueur vs ia
def joueurVSia():
    global etat
    etat = False
    pygame.init()
    WINDOW_SIZE = [255, 255]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("TEEKO")
    done = False
    clock = pygame.time.Clock()

    cpt = 0
    joueur = 1
    global compteur
    while cpt < 8:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)

                # attribuer case si conditions respectées
                if joueur == 1 and grille[row][column] == 0:
                    cpt += 1
                    compteur = cpt
                    grille[row][column] = 1
                    afficherGrille(grille)
                    joueur = 2

                print("Click ", pos, "Grid coordinates: ", row, column)

            if joueur == 2:
                cpt += 1
                compteur = cpt
                print(IA.minmax(None, 3, 3, True))
                if IA.minmax(None, 3, 3, True) == None:
                    print("IA bloqué, elle perdra forcément")
                    liste = []
                    for x in range(5):
                        for y in range(5):
                            if grille[x][y] == 0:
                                liste.append((x,y))
                    coord = random.choice(liste)
                else:
                    # assigner meilleur coup dans la grille
                    coord = IA.minmax(None, 3, 3, True)[0][1]
                x = coord[0]
                y = coord[1]
                grille[x][y] = 2
                joueur = 1

        if IA.combinaisonGagnante(grille, 1):
            print("Le gagnant est le joueur")
            afficherGrille(grille)
            screen.fill(BLACK)
            dessinerGrille()
            clock.tick(60)
        elif IA.combinaisonGagnante(grille, 2):
            print("Le gagnant est l'IA")
            afficherGrille(grille)
            screen.fill(BLACK)
            dessinerGrille()
            clock.tick(60)

        screen.fill(BLACK)
        dessinerGrille()
        clock.tick(60)
        pygame.display.flip()

    # Tours de placement
    while not IA.combinaisonGagnante(grille, 1) and not IA.combinaisonGagnante(grille, 2):
        compteur += 1
        for event in pygame.event.get():
            global nbr
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN and nbr == 0:
                pos1 = pygame.mouse.get_pos()
                column1 = pos1[0] // (WIDTH + MARGIN)
                row1 = pos1[1] // (HEIGHT + MARGIN)

                print("est passé")
                print("Click ", pos1, "Grid coordinates: ", row1, column1)

                if joueur == 1:
                    afficherGrille(grille)
                    # déplacement possible
                    IA.deplacementPossibleJ1(grille, IA.getPion(1))
                    if grille[row1][column1] == 1:
                        pion = IA.getPion(1).index((row1, column1))
                        pion = pion * 2
                        nbr = 1
            elif event.type == pygame.MOUSEBUTTONDOWN and nbr == 1:
                pos2 = pygame.mouse.get_pos()
                column2 = pos2[0] // (WIDTH + MARGIN)
                row2 = pos2[1] // (HEIGHT + MARGIN)

                if (row2, column2) in LISTE_DEPLACEMENT_POSSIBLE_J1[pion + 1]:
                    grille[row2][column2] = 1
                    grille[row1][column1] = 0
                    screen.fill(BLACK)
                    dessinerGrille()
                    clock.tick(60)
                    pygame.display.flip()
                    joueur = 2
                    nbr = 0
            elif joueur == 2:
                ##### TESTER EN PARTANT D4UN NOEUD ET NON DE NONE
                for pion in IA.getPion(1):
                    LISTE_DEPLACEMENT_POSSIBLE_J1.append((pion, [IA.voisinsPionJ1(grille, pion)]))

                IA.getPion(2)

                if IA.minmax(None, 4, 4, True) == None:
                    enfants = IA.getAllEnfant(grille, random.choice(IA.getPion(1)), True)
                    nombrePion = random.randint(0, len(enfants) - 1)
                    pion = enfants[nombrePion]
                    enfant = random.choice(pion)

                    coordOrigin = enfant[0]
                    coordDestination = enfant[1]

                else:
                    coordOrigin = IA.minmax(None, 4, 4, True)[0][0]
                    coordDestination = IA.minmax(None, 4, 4, True)[0][1]

                x = coordOrigin[0]
                y = coordOrigin[1]

                i = coordDestination[0]
                j = coordDestination[1]

                grille[i][j] = 2
                grille[x][y] = 0

                joueur = 1

                screen.fill(BLACK)
                dessinerGrille()
                clock.tick(60)
                pygame.display.flip()

    screen.fill(BLACK)
    dessinerGrille()
    clock.tick(60)
    pygame.display.flip()


def PTIAvsIA():
    global etat
    etat = True
    pygame.init()
    WINDOW_SIZE = [255, 255]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("TEEKO")
    done = False
    clock = pygame.time.Clock()

    cpt = 0
    joueur = 1
    global compteur
    while cpt < 8:

        if joueur == 1:
            cpt += 1
            compteur = cpt
            print(IA.minmax(None, 3, 3, False))
            if IA.minmax(None, 3, 3, False) == None:
                liste = []
                for i in range(5):
                    for j in range(5):
                        if grille[i][j] == 0:
                            liste.append((i,j))
                coord = random.choice(liste)

            else:
            # assigner meilleur coup dans la grille
                coord = IA.minmax(None, 3, 3, False)[0][1]
            x = coord[0]
            y = coord[1]
            print(x, y)
            grille[x][y] = 1
            afficherGrille(grille)
            joueur = 2

        elif joueur == 2:
            cpt += 1
            compteur = cpt
            if IA.minmax(None, 3, 3, True) == None:
                liste = []
                for i in range(5):
                    for j in range(5):
                        if grille[i][j] == 0:
                            liste.append((i, j))
                coord = random.choice(liste)
            else:
                #assigner meilleur coup dans la grille
                coord = IA.minmax(None, 3, 3, True)[0][1]
            x = coord[0]
            y = coord[1]
            print(x,y)
            grille[x][y] = 2
            afficherGrille(grille)
            joueur = 1

        if IA.combinaisonGagnante(grille, 1):
            print("Le gagnant est IA 1")
            afficherGrille(grille)
            screen.fill(BLACK)
            dessinerGrille()
            clock.tick(60)
        elif IA.combinaisonGagnante(grille, 2):
            print("Le gagnant est IA 2")
            afficherGrille(grille)
            screen.fill(BLACK)
            dessinerGrille()
            clock.tick(60)

        screen.fill(BLACK)
        dessinerGrille()
        clock.tick(60)
        pygame.display.flip()

    while not IA.combinaisonGagnante(grille, 1) and not IA.combinaisonGagnante(grille, 2):
        compteur += 1
        if joueur == 1:
            IA.getPion(1)
            if IA.minmax(None, 3, 3, False) == None:
                enfants = IA.getAllEnfant(grille, random.choice(IA.getPion(1)), False)
                nombrePion = random.randint(0, len(enfants) - 1)
                pion = enfants[nombrePion]
                enfant = random.choice(pion)

                coordOrigin = enfant[0]
                coordDestination = enfant[1]

            else:
                coordOrigin = IA.minmax(None, 3, 3, False)[0][0]
                coordDestination = IA.minmax(None, 3, 3, False)[0][1]

            x = coordOrigin[0]
            y = coordOrigin[1]

            i = coordDestination[0]
            j = coordDestination[1]

            grille[i][j] = 1
            grille[x][y] = 0

            joueur = 2


        elif joueur == 2:
            IA.getPion(2)
            if IA.minmax(None, 4, 4, True) == None:
                print("est passé")
                enfants = IA.getAllEnfant(grille, random.choice(IA.getPion(2)), True)
                nombrePion = random.randint(0, len(enfants) - 1)
                pion = enfants[nombrePion]
                enfant = random.choice(pion)

                coordOrigin = enfant[0]
                coordDestination = enfant[1]

            else:
                coordOrigin = IA.minmax(None, 4, 4, True)[0][0]
                coordDestination = IA.minmax(None, 4, 4, True)[0][1]

            x = coordOrigin[0]
            y = coordOrigin[1]

            i = coordDestination[0]
            j = coordDestination[1]

            grille[i][j] = 2
            grille[x][y] = 0

            joueur = 1

        screen.fill(BLACK)
        dessinerGrille()
        clock.tick(60)
        pygame.time.wait(500)
        pygame.display.flip()

    if IA.combinaisonGagnante(grille, 1):
        print("Le gagnant est IA BLEUE")
        afficherGrille(grille)
        screen.fill(BLACK)
        dessinerGrille()
        clock.tick(60)
    elif IA.combinaisonGagnante(grille, 2):
        print("Le gagnant est IA 2 JAUNE")
        afficherGrille(grille)
        screen.fill(BLACK)
        dessinerGrille()
        clock.tick(60)

    screen.fill(BLACK)
    dessinerGrille()
    clock.tick(60)
    pygame.time.wait(500)
    pygame.display.flip()

# afficher grille terminal
def afficherGrille(grille):
    for x in grille:
        for elem in x:
            print(elem, end=' ')
        print()
