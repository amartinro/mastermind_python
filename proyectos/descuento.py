
edad = int(input("Dime tu edad: "))
tipocarnet = input("Dime tu tipo de carnet E, P, F, N: ")

#caso1 = edad<=35 and edad >=25 and tipocarnet=='E'
caso1 = 25 <= edad <= 35 and tipocarnet=='E'
caso2 = edad<=10 
caso3 = edad>=65 and tipocarnet=='P'
caso4 = tipocarnet=='F'

if (caso1 or caso2 or caso3 or caso4):
    print("Entras")
else:
    print("No entras")