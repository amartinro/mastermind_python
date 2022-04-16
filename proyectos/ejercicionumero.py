##el usuario tiene que adivinar un numero de 1 a 10
#si el numero es igual al que es y si no, terminamos

import random

numerosecreto = random.randint(1, 10)

numerousuario = int(input("Dime un numero entre 1 y 10: "))

if (numerousuario<=10 and numerousuario >=1):
    if (numerousuario==numerosecreto):
        print("Enhorabuena, has acertado!")
    else:
        print("Casi! el numero era {}".format(numerosecreto))
else:
    print("El numero no está entre 1 y 10")