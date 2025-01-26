
def listarTareas(lista_tareas):
    if len(lista_tareas) == 0:
        print("No hay tareas para listar\n")
    else:
        print("{:<5} | {:<30} | {:<10}".format("  ID", "          Tarea", " Estatus"))
        print("{:<5} | {:<30} | {:<10}".format("-"*5, "-"*30, "-"*10))
        for index, task in enumerate(lista_tareas):
            print("{:<5} * {:<30} * {:<10}".format(index + 1, task["tarea"], task["estatus"]))
            print("{:<5} | {:<30} | {:<10}".format("-"*5, "-"*30, "-"*10))


def crearTarea(lista_tareas):
    tarea = input("Ingresa la tarea pendiente: ").capitalize()
    lista_tareas.append({"tarea": tarea, "estatus": "Pendiente"})
    print("Tarea creada con Exito...")


def realizarTarea(lista_tareas):
    listarTareas(lista_tareas)
    try:
        id_tarea = int(input("Ingresa el id de la tarea realizada: "))
        id_tarea -= 1

        for index, task in enumerate(lista_tareas):
            if index == id_tarea:
                task["estatus"] = "Realizada"

    except ValueError:
        print(ValueError)


def main():
    lista_tareas = []
    
    while True:
        print("""
        Ingresa la opcion que deseas realizar
              1) Listar Tarea
              2) Agregar Tarea
              3) Modificar Tarea
              4) Salir
                """)
        try:
            opcion = int(input("Ingresa una opcion del menu: "))

            match opcion:
                case 1:
                    listarTareas(lista_tareas)
                case 2:
                    crearTarea(lista_tareas)
                case 3:
                    realizarTarea(lista_tareas)
                case 4:
                    exit()
                case _:
                    print("Debes seleccionar una opcion del menu...")

        except ValueError:
            print("Debes seleccionar un numero entero.")
            continue


if __name__=='__main__':
    main()