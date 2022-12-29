import numpy as np
from tkinter import *

import controller

## MAIN ##


menu = int(input(" 1) J1 VS IA \n 2) IA VS IA \n"))

if menu == 1:
    controller.joueurVSia()
elif menu == 2:
    controller.PTIAvsIA()



