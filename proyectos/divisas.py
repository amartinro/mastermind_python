dolar_euro = 0.91
libra_euro = 1.18

resultado = 0.0
valor_a_convertir = 0.0
moneda = ''

cadena_resultado = "El resultado es {} {}"

opcion = int(input("Que moneda quieres convertir?\n"
                "1- Dolar\n"
                "2- Libra\n"));

valor_a_convertir = float(input ("Euros: "))

if (opcion==1):
    resultado = dolar_euro*valor_a_convertir
    moneda = "USD"
elif (opcion==2):
    resultado = libra_euro*valor_a_convertir
    moneda = "LIB"
else:
    print("No has escogido una opcion valida")

print(cadena_resultado.format(resultado, moneda))