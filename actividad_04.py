monto = float(input("Ingresa el monto de la compra: "))
res = input("¿Es un usuario frecuente? SI/NO ")

if res == "SI":
    if monto >= 1000:
        precio_final = monto * 20 / 100
        print(f"El monto es de {monto}, y {precio_final} con descuento de 20%")
    elif monto <= 500:
        precio_final= monto * 20 / 100
        print(f"El monto es de {monto}, y {precio_final} con descuento de 20%")

if res == "NO":
    if monto >= 1000:
        precio_final = monto * 10 / 100
        print(f"El monto es de {monto}, y {precio_final} con descuento de 10%")
    elif monto <= 500:
        precio_final= monto * 10 / 100
        print(f"El monto es de {monto}, y {precio_final} con descuento de 10%")