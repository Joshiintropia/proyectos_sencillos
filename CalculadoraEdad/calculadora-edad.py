from datetime import datetime

def calculadoraEdad(año_nac, mes_nac):
    fecha_actual = datetime.now().strftime("%Y-%m").split("-")
    año_act, mes_act, *otro = fecha_actual
    año_dif = int(año_act) - int(año_nac)
    if int(mes_act) < int(mes_nac): año_dif -= 1
    print(f"Tienes {año_dif} años")



def main():
    max, min = 2025, 1924
    try:
        año_nac = input("Ingresa tu año de nacimiento: ")
        if not len(año_nac) == 4 or not año_nac.isdigit():
            print("El año de nacimiento es incorrecto")
            main()
        if int(año_nac) <= min or int(año_nac) >= max:
            print("El año de nacimiento es incorrecto.")
            main()      
        mes_nac = int(input("Ingresa el número del mes de nacimiento: "))
        if mes_nac < 0 or mes_nac > 12:
            print("El mes de nacimiento es incorrecto")
            main()
    except ValueError as ve:
        print("Solo puedes ingresar número enteros")
        main()
    
    calculadoraEdad(año_nac, mes_nac)



if __name__ == '__main__':
    main()