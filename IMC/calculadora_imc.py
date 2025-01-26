

def main():
    try:
        print("""
        Calculadora de IMC
        """)
        
        peso = float(input("Ingresa tu peso actual: "))
        
        if peso < 2:
            print("Valor de peso invalido, intenta de nuevo.")
            main()
        
        altura = (int(input("Ingresa tu estatura en cm: ")) / 100)

        imc = peso / (altura * altura)

        if imc < 18.5: print("Tu IMC esta bajo, tienes desnutricion.")

        if 18.5 < imc < 24.9: print("Tu IMC es normal")

        if 25.0 < imc < 29.9: print("Tu IMC esta alto, tienes sobrepeso.")

        if imc >= 30: print("Tu IMC esta muy excedido, tienes obesidad morvida")

    except ValueError:
        print("Debes ingresar valores validos....")


if __name__=='__main__':
    main()