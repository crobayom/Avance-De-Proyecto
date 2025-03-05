from math import fabs
from os import system
from time import sleep

maximo = 10

# Función para inicializar los tableros
def inicio_tableros(maximo, tableroA, tableroB, tableroA1, tableroB1):
    for i in range(maximo):
        for j in range(maximo):
            tableroA.append([0] * maximo)
            tableroA1.append([0] * maximo)
            tableroB.append([0] * maximo)
            tableroB1.append([0] * maximo)
    for i in range(maximo):
        print(tableroA[i])
    print("")
    for i in range(maximo):
        print(tableroA1[i])
    print("")
    for i in range(maximo):
        print(tableroB[i])
    print("")
    for i in range(maximo):
        print(tableroB1[i])
    print("")

# Función para colocar los barcos en el tablero
def colocar_barco(tableroA, tamano):
    orientacion = 11
    while orientacion > 2 or orientacion < 1:
        orientacion = int(input(f"¿Qué orientación prefiere para el barco de tamaño {tamano}? 1. Vertical 2. Horizontal: "))
        if orientacion > 2 or orientacion < 1:
            print("La opción que eligió no está dentro de las válidas, inténtelo de nuevo")

    primera_posicion = int(input("Ingrese la posición inicial del barco (en el eje vertical): "))
    segunda_posicion = int(input("Ingrese la posición inicial del barco (en el eje horizontal): "))

    # Validación para asegurarse de que el barco no se salga del tablero ni se solape
    while (primera_posicion < 1 or primera_posicion > maximo or segunda_posicion < 1 or segunda_posicion > maximo or 
           not es_posicion_valida(tableroA, primera_posicion, segunda_posicion, tamano, orientacion)):
        print("La ubicación que elegiste no es válida. Asegúrate de que el barco quepa en el tablero y no se solape.")
        primera_posicion = int(input("Ingrese la posición inicial del barco (en el eje vertical): "))
        segunda_posicion = int(input("Ingrese la posición inicial del barco (en el eje horizontal): "))

    if orientacion == 1:  # Vertical
        for i in range(tamano):
            tableroA[primera_posicion - 1 + i][segunda_posicion - 1] = 1
    elif orientacion == 2:  # Horizontal
        for i in range(tamano):
            tableroA[primera_posicion - 1][segunda_posicion - 1 + i] = 1

    # Mostrar el tablero con el barco colocado
    for i in range(maximo):
        print(tableroA[i])

# Función que valida que un barco no se solape ni se salga del tablero
def es_posicion_valida(tableroA, primera_posicion, segunda_posicion, tamano, orientacion):
    if orientacion == 1:  # Vertical
        if primera_posicion + tamano - 1 > maximo:
            return False  # El barco se sale del tablero
        for i in range(tamano):
            if tableroA[primera_posicion - 1 + i][segunda_posicion - 1] == 1:
                return False  # El barco se solapa con otro
    elif orientacion == 2:  # Horizontal
        if segunda_posicion + tamano - 1 > maximo:
            return False  # El barco se sale del tablero
        for i in range(tamano):
            if tableroA[primera_posicion - 1][segunda_posicion - 1 + i] == 1:
                return False  # El barco se solapa con otro
    return True

# Función para colocar todos los barcos de un jugador
def ubicacion_barcos(tableroA):
    # Barcos de tamaño 5, 4, 3, 3 y 2
    tamaños = [5, 4, 3, 3, 2]
    for tamano in tamaños:
        colocar_barco(tableroA, tamano)

if __name__ == "__main__":
    print("Bienvenid@s sean al juego de astucia naval")
    print("Este consta de varias reglas de juego, que serán mostradas a continuación: ")
    print("Cada jugador tendrá dos tableros, uno para las posiciones de sus barcos y otro para los lugares donde atacará")
    print("Luego de ubicar sus barcos, cada jugador tendrá la oportunidad de derribar los del rival")
    print("Esto lo hará a partir de ataques a posiciones donde cree que estará el rival, y se le informará si impactó o no")
    print("Cuando todos los cuadrantes de un barco sean impactados, este se hundirá")
    print("El objetivo es que el rival se quede sin barcos mientras que tú los conserves")
    print("Hay que tener cuidado pues los barcos pueden ser colocados en la misma posición que otros y el juego no lo restringirá")
    print("Pero por el hecho de que puedas hacerlo no significa que sea lo ideal, pues si encuentras una posición con todos los barcos 1 impacto tendrá el valor de 5")
    print("")
    print("Decidan bien, buena suerte")   
    print("\n")
    
    tableroA = []
    tableroB = []
    tableroA1 = []
    tableroB1 = []
    
    # Inicializamos los tableros
    inicio_tableros(maximo, tableroA, tableroA1, tableroB, tableroB1)

    print("Es tu turno jugador 1")
    ubicacion_barcos(tableroA)  # Colocamos los barcos del jugador 1

    print("5")
    sleep(1)
    print("4")
    sleep(1)
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    system("cls")

    print("Es tu turno jugador 2")
    ubicacion_barcos(tableroB)  # Colocamos los barcos del jugador 2

    print("5")
    sleep(1)
    print("4")
    sleep(1)
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    system("cls")

    existencia1 = True
    existencia2 = True

    print("Hora de atacar")

    while existencia1 and existencia2:
        # Jugador 1 ataca
        existencia2 = False
        existencia1 = False

        print("Jugador 1, es tu turno")
        print("Este es tu tablero de barcos hasta el momento: ")
        for i in range(maximo):
            print(tableroA[i])
        print("Este es tu tablero de ataque hasta el momento: ")
        for i in range(maximo):
            print(tableroA1[i])

        primera_posicion = int(input("Ingrese el lugar donde quiera atacar (en el eje vertical): "))
        segunda_posicion = int(input("Ingrese el lugar donde quiera atacar (en el eje horizontal): "))
        
        if tableroB[primera_posicion - 1][segunda_posicion - 1] == 1: 
            tableroB[primera_posicion - 1][segunda_posicion - 1] = 6
            tableroA1[primera_posicion - 1][segunda_posicion - 1] = 2
            print("Buen trabajo, le diste")
        else: 
            tableroA1[primera_posicion - 1][segunda_posicion - 1] = 1
            print("Mejor suerte la próxima")

        for i in range(maximo):
            print(tableroA1[i])

        print("5")
        sleep(1)
        print("4")
        sleep(1)
        print("3")
        sleep(1)
        print("2")
        sleep(1)
        print("1")
        system("cls")

        # Jugador 2 ataca
        print("Es tu turno, jugador 2")
        print("Este es tu tablero de barcos hasta el momento: ")
        for i in range(maximo):
            print(tableroB[i])
        print("Este es tu tablero de ataque hasta el momento: ")
        for i in range(maximo):
            print(tableroB1[i])

        primera_posicion = int(input("Ingrese el lugar donde quiera atacar (en el eje vertical): "))
        segunda_posicion = int(input("Ingrese el lugar donde quiera atacar (en el eje horizontal): "))
        
        if tableroA[primera_posicion - 1][segunda_posicion - 1] == 1: 
            tableroA[primera_posicion - 1][segunda_posicion - 1] = 6
            tableroB1[primera_posicion - 1][segunda_posicion - 1] = 2
            print("Buen trabajo, le diste")
        else: 
            tableroB1[primera_posicion - 1][segunda_posicion - 1] = 1
            print("Mejor suerte la próxima")            

        for i in range(maximo):
            print(tableroB1[i])

        # Comprobar si existen barcos
        for i in range(maximo):
            if 1 in tableroA[i]: existencia1 = True
            if 1 in tableroB[i]: existencia2 = True
        
        print("5")
        sleep(1)
        print("4")
        sleep(1)
        print("3")
        sleep(1)
        print("2")
        sleep(1)
        print("1")
        system("cls")

    if not existencia1 and not existencia2:
        print("¡Felicidad, es un empate! ¿Quieren desempatar? Jueguen de nuevo.")
    elif not existencia1:
        print("Bien hecho jugador 2, ¡ganaste!")
    elif not existencia2:
        print("Bien hecho jugador 1, ¡ganaste!")
