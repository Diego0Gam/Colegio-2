monto = float(input("Ingresa el monto de la compra: "))
res = input("¿Es un usuario frecuente? SI/NO ")

if monto >= 1000 and res == "SI":
    final = (monto * 20) / 100
    print(f"{final} con un descuento del 20%")
elif monto <= 500 and res == "SI":
    final = (monto * 20) / 100
    print(f"{final} con un descuento del 20%")

if monto >= 1000 and res == "NO":
    final = (monto * 10) / 100
    print(f"{final} con un descuento del 10%")
elif monto <= 500 and res == "NO":
    final = (monto * 10) / 100
    print(f"{final} con un descuento del 10%")