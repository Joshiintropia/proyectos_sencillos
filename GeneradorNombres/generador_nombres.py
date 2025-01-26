import json
import random


with open("./GeneradorNombres/names.json", "r") as names_load:
    names = json.load(names_load)


def listarRegiones():
    for index, regiones in enumerate(names):
        print(f"index: {index}, Region: {regiones["region"]}")


def seleccionarRegion():
    
    try:
        
        id_region = int(input("\nSelecciona el Index de la region: "))
        
        region = names[id_region]

        return region

    except ValueError:
        print("Debes de introducir un valor valido (numero entero) dentro de la lista")
        seleccionarRegion()
    except IndexError:
        print("Debes de introducir un valor valido (numero entero) dentro de la lista")
        seleccionarRegion()


def generarNombre():
    listarRegiones()
    region = seleccionarRegion()

    genero = input("\nSelecciona el genero del nombre que quieres (M|F): ").upper()
    
    if not genero == "M" and not genero == "F": 
        print("Error al seleccionar el genero, intenta nuevamente")
        generarNombre()
    
    genero = "male" if genero == "M" else "female"
    
    nombre = random.choice(region[genero])
    apellido = random.choice(region["surnames"])

    print(f"\nNombre: {nombre} \nApellido: {apellido}")


def main():
    generarNombre()


if __name__=='__main__':
    main()