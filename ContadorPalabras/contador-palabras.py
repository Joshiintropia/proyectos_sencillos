


def main():
    frase = input("Ingresa la frase o palabra: ")
    contarPalabras = len(frase.split(" "))
    frase = "".join(frase)
    contarCaracteres = len(frase)
    print(f"La frase tiene {contarPalabras} palabras y {contarCaracteres} caracteres")


if __name__=='__main__':
    main()