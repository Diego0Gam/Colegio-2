#Actividad 1
def es_par(numero):
    resto = numero % 2
    if resto == 0:
        return True
    else:
        return False

par_impar = es_par(21)
print(par_impar)

#Actividad 2
nombre = input("Ingrese un nombre: ")

def saludar(nombre):
    print(f"Hola {nombre}")

saludar(nombre)

#Actividad 3
frutas = ["Manzana", "Pera", "Uva", "Naranja", "Mandarina"]

#Actividad 4
for i in frutas:
    print(i)

#Actividad 5
edad = int(input("Ingresa tu edad: "))

#Actividad 6
if edad >= 18:
    print("Usted es mayor")
else:
    print("Usted es menor")

#Actividad 7
numero1 = float(input("Ingresa un numero: "))
numero2 = float(input("Ingresa otro numero: "))

#Actividad 8
if numero1 == numero2:
    print("Ambos numeros son iguales")
elif numero1 > numero2:
    print(f"{numero1} es mayor a {numero2}")
else:
    print(f"{numero2} es mayor a {numero1}")

#Acticidad 9
numero_usuario = float(input("Ingrese un numero: "))

#Acticidad 10
es_par(numero_usuario)
print(par_impar)

#Actividad 11
def buscar_fruta(fruta):
    if fruta in frutas:
        return True
    else:
        return False
    
busc_fruta = buscar_fruta("Pera")
print(busc_fruta)

#Actividad 12
def cambiar_minuscula(cadena):
    return cadena.lower()

minuscula = cambiar_minuscula("HOLA")
print(minuscula)

#Actividad 13
texto_usuario = str(input("Ingrese un texto: "))

cambiar_minuscula(texto_usuario)
print(minuscula)

#Actividad 14
limite = int(input("Ingrese un numero: "))
numeros = 1

limite = limite + 1

while True:
    if numeros != limite:
        print(numeros)
        numeros = numeros + 1
    else: 
        break