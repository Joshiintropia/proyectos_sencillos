from secrets import choice
import os
from listas import lista_palabras, vida1,vida2,vida3,vida4,vida5,vida6,vida0

def limpiarPantalla():
    os.system('clear')

def saludar(vidas):
    print(f"""
            BIENVENIDOS AL JUEGO DEL AHORCADO
            **********************************
            El objetivo es encontrar las letras
            de la palabra, antes de que se te
            acaben las vidas ({vidas})
        """)
    
def palabraSecreta():
    palabra_secreta = choice(lista_palabras)
    return palabra_secreta.upper()


def mostrarVidas(vidas):
    match vidas:
        case 0:
            print(vida0)
        case 1:
            print(vida1)
        case 2:
            print(vida2)
        case 3:
            print(vida3)
        case 4:
            print(vida4)
        case 5:
            print(vida5)
        case 6:
            print(vida6)


def adivinarPalabra(palabra, lista_adivinada):
    palabra_secreta = ""

    for letra in palabra:
        if letra in lista_adivinada:
            palabra_secreta += " " + letra + " "
        else:
            palabra_secreta += " - "
    
    print(f"""
                {palabra_secreta}
        """)


def main():
    vidas = 6
    lista_adivinada = []
    palabra_secreta = palabraSecreta()

    while True:
        limpiarPantalla()
        saludar(vidas)
        mostrarVidas(vidas)
        adivinarPalabra(palabra_secreta, lista_adivinada)
        
        if vidas == 0:
            saludar(vidas)
            limpiarPantalla()
            print(vida0)
            print(f"""
                    PERDISTE!
               La palabra era {palabra_secreta}
                """)
            break

        letra = input("Selecciona una letra para empezar: ").upper()

        if letra.isdigit():
            print("Solo puedes seleccionar letras y no numeros...")
            

        if letra in palabra_secreta:
            lista_adivinada.append(letra)
            if set(palabra_secreta) == set(lista_adivinada):
                limpiarPantalla()
                mostrarVidas(vidas)
                print(f"""
                    -------------
                      {palabra_secreta}
                    **************
                    ¡¡HAS GANADO!!
                    **************
                    """)
                break
        else:
            vidas -= 1
            print(f"""
                La letra == {letra} ==
            NO se encuentra en la palabra
                Intenta de nuevo
                """)
            _ = input("Presiona cualquier tecla para continuar...")


if __name__=='__main__':
    main()