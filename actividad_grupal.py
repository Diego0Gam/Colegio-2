lista = []

while True:
    opcion = input("Quiere comprar cosas? s/n ")
    if opcion == "s":
        compra = input("ingrese que quiere comprar ")
        lista.append(compra)
        print(lista) 
    elif opcion == "n":
        break
    else:
        print("Opcion no valida")

if len(lista) != 0:
    while True:
     opcion_eliminar = input("Quiere borrar cosas? s/n ")
     if opcion_eliminar == "s":
        eliminar = input("Ingrese que quiere borrar ")
        lista.remove(eliminar)
        print(lista)
     elif opcion_eliminar == "n":
        break
     else:
        print("Opcion no valida")