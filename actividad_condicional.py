contraseña = "Hola123"
contra = input("Ingrese la contraseña: ")

if contra != contraseña:
    print("La contraseña es incorrecta")
    res = input("¿Quiere reestabecer la contraseña? si/no")
    if res == "si":
        nueva_contraseña = input("Ingrese nueva contraseña ")
        contraseña = nueva_contraseña
        print(f"contraseña nueva es: {contraseña}")
    else:
        print("No se puede reestablecer")
else:
    print("Contraseña correcta")