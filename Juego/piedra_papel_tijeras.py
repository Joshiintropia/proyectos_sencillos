import random

    # 1 = papel G pieda P tijera
    # 2 = piedra G tijera P papel
    # 3 = tijera G papel P piedra

opciones = [
    {"id":1, "eleccion":"Papel", "icono":"\U0000270B", "jugador": ""},
    {"id":2, "eleccion":"Piedra", "icono":"\U0001F44A", "jugador": ""},
    {"id":3, "eleccion":"Tijeras", "icono":"\U0001F596", "jugador": ""}
]

def pPt():
    eleccion = random.choice(opciones)
    eleccion["jugador"] = "Computadora"
    #print(eleccion)
    return eleccion


def comprobarGanador(comp, user):
    if user["id"] == 1 and comp["id"] == 2:
        print(f"\n{user["jugador"]}: {user["icono"]} VS {comp["jugador"]}: {comp["icono"]}")
        return user
    elif user["id"] == 2 and comp["id"] == 3:
        print(f"\n{user["jugador"]}: {user["icono"]} VS {comp["jugador"]}: {comp["icono"]}")
        return user
    elif user["id"] == 3 and comp["id"] == 1:
        print(f"\n{user["jugador"]}: {user["icono"]} VS {comp["jugador"]}: {comp["icono"]}")
        return user
    else:
        print(f"\n{user["jugador"]}: {user["icono"]} VS {comp["jugador"]}: {comp["icono"]}")
        return comp


def main():
    print("Bienvenido al juego de Piedra, Papel o Tijeras\n")

    user_name = input("Antes de comenzar ingresa tu nombre: ").upper()

    while True:
        print("""
        Selecciona una opcion
              1) Papel \U0000270B
              2) Piedra \U0001F44A
              3) Tijeras \U0001F596
              4) Dejar de jugar
            """)
        try:
            user = int(input("Selecciona una opcion del menu: "))
            
            if user == 4:
                exit()

            user = opciones[user - 1]

            user["jugador"] = user_name
            #print(user)

            comp = pPt()

            if comp["id"] == user["id"]:
                print(f"Usuario: {user["icono"]} VS Computadora: {comp["icono"]}")
                print("\nUff!!! Han empatado, intenta de nuevo...")
                continue

            ganador = comprobarGanador(user=user, comp=comp)
            print(f"\nFELICIDADES el ganador es: {ganador['jugador']}")
            break 
        
        except ValueError:
            print("Debes seleccionar una opcion del menu.")


if __name__=='__main__':
    main()