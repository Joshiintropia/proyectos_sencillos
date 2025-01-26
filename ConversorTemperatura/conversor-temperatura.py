
def CaK(celsius):
    kelvin = celsius + 273.15
    print(kelvin)


def KaC(kelvin):
    celsius = kelvin - 273.15
    print(celsius)


def FaC(celsius):
    farengeing = (1.8*celsius) + 32
    print(farengeing)


def CaF(farengeing):
    celsius = (farengeing - 32) / 1.8
    print(celsius)


def main():
    
    while True:
        print("""Ingresa la escala de temperatura a convertir
              1) Celsius a Farengeing
              2) Farengeing a Celsius
              3) Celsius a Kelvin
              4) Kelvin a Celsius
              5) Salir""")
              
        try:
            opcion = int(input("Elige la opción deseada (1|2|3|4|5): "))

            match opcion:
                case 1:
                    temperatura = float(input("Ingresa la temperatura en Celsius: "))
                    CaF(temperatura)
                case 2:
                    temperatura = float(input("Ingresa la temperatura en Farengeing: "))
                    FaC(temperatura)
                case 3:
                    temperatura = float(input("Ingresa la temperatura en Celsius: "))
                    CaK(temperatura)
                case 4:
                    temperatura = float(input("Ingresa la temperatura en Kelvin: "))
                    KaC(temperatura)
                case 5:
                    exit();
                case _:
                    print("Solo puedes elegir una opción del menú.")
                    main()

        except ValueError:
            print("Solo puedes seleccionar números enteros.")
            main()


if __name__=='__main__':
    main()