numeros = [23, 45, 12, 67, 8, 90, 4, 1, 78, 33, 56, 7, 9]

#Actividad 1
print("Numeros y sus dobles")

for doble in numeros:
    print(f"El numero es {doble} y su doble es {doble * 2}")

#Actividad 2
print("Par e Impar")

for par_impar in numeros:
    i = par_impar % 2
    if i == 0:
        print(f"El numero {par_impar} es par")
    else:
        print(f"El numero {par_impar} es impar")

#Actividad 3
print("Maximos, minimos y su suma")

num_max = max(numeros)
num_min = min(numeros)
sum_list = sum(numeros)
print(f"El numero maximo es {num_max}, el minimo es {num_min} y la suma de todo es {sum_list}")

#Actividad 4
print("Cantidad de pares e impares")

par = 0
impar = 0
for par_impar in numeros:
    cont = par_impar % 2
    if cont == 0:
        print(f"El numero {par_impar} es par")
        par = par + 1
        print(f"Hay {par} numeros pares")
    else:
        print(f"El numero {par_impar} es impar")
        impar = impar + 1
        print(f"Hay {impar} numeros impares")

#Actividad 5
print("Lista ordenada, agregar y eliminar un numero")
numeros.sort()
numeros.pop(6)
numeros.append(91)
print(f"La lista ordenada es: {numeros}")

#Actividad 6
print("El final es:")
print(f"El numero maximo es: {num_max}")
print(f"El numero minimo es: {num_min}")
print(sum_list)
print(par)
print(impar)