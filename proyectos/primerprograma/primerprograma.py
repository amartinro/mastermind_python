numero1 = int(input("Introduce un número: "))
numero2 = int(input("Introduce otro número: "))
numero3 = int(input("Introduce otro número: "))

maximo = max(numero1, numero2, numero3)
minimo = min(numero1, numero2, numero3)

#print("El maximo es "+str(maximo)+" el minimo es "+str(minimo))

print("El maximo es {} el minimo es {}".format(maximo, minimo))