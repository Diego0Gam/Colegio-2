listanumeros = [3,7,2]

numero = float(input("Ingrese un numero: "))

if numero >= 0:
    if numero in listanumeros:
        print("Su numero esta en la lista")
    else:
        print("Su numero no esta en la lista")
else:
    print("El numero no tiene que ser negativo")