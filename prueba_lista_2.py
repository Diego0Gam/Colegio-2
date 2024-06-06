lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(lista)
print(lista[3])

for numero in lista:
    print(f"El numero es: {numero}")

lista.append(10)
print(lista)

lista.pop(8)
print(lista)

numero = input("ingrese un numero")
lista.append(numero)
print(lista)

numero2 = input("Quiere borrar un numero?")
lista.remove(numero2)
print(lista)

def is_list_empty(lista):
    if len(lista) == 0:
        return True
    return False