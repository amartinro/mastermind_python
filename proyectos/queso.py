titulo = "Bienvenido al cuestionario"
print("\n"+titulo+"\n")
print("-"*len(titulo))

puntuacion=0

opcion = input("Pregunta 1\n"
                "A- \n"
                "B- \n"
                "C- \n")

if (opcion=="A"):
    puntuacion+=0
elif (opcion=="B"):
    puntuacion+=5
elif (opcion=="C"):
    puntuacion+=10
else:
    print("Opcion incorrecta")
    exit()

opcion = input("Pregunta 2\n"
                "A- \n"
                "B- \n"
                "C- \n")

if (opcion=="A"):
    puntuacion+=0
elif (opcion=="B"):
    puntuacion+=5
elif (opcion=="C"):
    puntuacion+=10
else:
    print("Opcion incorrecta")
    exit()

print("Tu puntuacion es {}".format(puntuacion))

