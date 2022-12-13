import numpy as np
from tkinter import *

import modele
import controller


modele.dessinerPlateau()
controller.partieEnCours()

# test fonction labelClickable
# modele.labelClickable()
# laisser cette ligne pour ne pas que la fenêtre se ferme au bout des 8 placements vu que le code est pas fini
modele.fenetre.mainloop()
