import controller

## MAIN ##


menu = int(input(" 1) J1 VS IA \n 2) IA VS IA \n"))

if menu == 1:
    depth = int(input("Si vous voulez une profondeur plus efficace mais qui met plus de temps pour charger un coup, taper 4, sinon taper 3"))
    if depth == 4:
        controller.joueurVSia(depth)
    else:
        controller.joueurVSia(3)
elif menu == 2:
    controller.PTIAvsIA()



