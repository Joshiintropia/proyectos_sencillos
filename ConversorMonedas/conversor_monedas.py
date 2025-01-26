import json


with open("./ConversorMonedas/monedas.json", "r") as data:
    pais = json.load(data)


def listarMonedas():
    print("{:<3} | {:<15}".format("ID", "Moneda"))
    for index, moneda in enumerate(pais):
        print("{:<3}==> {:<15}".format(index + 1, moneda["moneda"].capitalize()))


def main():
    listarMonedas()
    try:
        moneda = int(input("Selecciona el id de la moneda que quieres convertir: "))
        moneda = pais[moneda-1]
        moneda2 = int(input("Selecciona el id de tu moneda: "))
        moneda2 = pais[moneda2-1]

        valor = int(input(f"Ingresa la cantidad que quieres convertir a {moneda["moneda"].capitalize()}: "))

        conversor = round((moneda["valor"]/moneda2["valor"]) * valor, 2)

        print(f"{valor} {moneda2["monedas"].capitalize()} equivalen a {conversor} {moneda["monedas"].capitalize()}")


    except ValueError:
        print("Debes seleccionar un numero entero del menu")
    except IndexError:
        print("Debes seleccionar un numero entero del menu")



if __name__=="__main__":
    main()