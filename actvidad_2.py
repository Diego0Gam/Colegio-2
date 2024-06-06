#Programa que pida los datos de un deportista

apellido = input("Apellido: ")
nombre = input("Nombre: ")
dni = int(input("DNI: "))
edad = int(input("Edad: "))
estadodeactividad = bool(input("Estado de actividad: "))
deporte = input("Deporte: ")

print(f"Su nombre completo es: {nombre} {apellido}. DNI: {dni}. Edad: {edad}. Estado de actividad: {estadodeactividad}. Deporte: {deporte}")