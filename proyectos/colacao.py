hayleche = input("hay leche? (S/N)")
haycolacao = input("hay colacao? (S/N)")

if (hayleche != "S" or haycolacao != "S"):
    print("voy al super")
    if (hayleche != "S"):
        print("Compro leche")
    if (haycolacao != "S"):
        print("Compro colacao")

if hayleche=='S':
    print("hay leche")
    
    if haycolacao=='S':
        print("hay colacao")
    else:
        print("no hay colacao")
else:
    print("no hay leche")
