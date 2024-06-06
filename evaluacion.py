tareas = []

while True:
  opciones = input("1.Agregar Tarea | 2.Eliminar Tarea | 3.Mostrar Tareas | 4.Salir ")
  if opciones == "1":
    agregar_tarea = input("Ingrese nombre de la tarea: ")
    tareas.append(agregar_tarea)
    print(f"Se agrego la tarea {agregar_tarea}")
  elif opciones == "2":
    eliminar_tarea = input("Ingrese el nombre de la tarea que quiere eliminar: ")
    if eliminar_tarea in tareas:
        tareas.remove(eliminar_tarea)
        print(f"Se elimino la tarea {eliminar_tarea}")
    else:
        print(f"No se encontro la tarea {eliminar_tarea}")
  elif opciones == "3":
        if len(tareas) == 0:
            print("La lista esta vacia")
        else:
            print(tareas)
  elif opciones == "4":
         print("Salio de la app")
         break
  else:
      print("Opcion no valida")