#Programa para calcular la propina en base al valor final de la cuenta

total = float(input("Ingrese el valor total de la cuenta: "))
propina = float(input("Ingrese el porcentaje de propina: "))

final = propina * total / 100 #Formula para calcular el porcentaje

print(f" El precio final es: {final}")