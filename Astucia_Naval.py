from math import fabs
from os import system
from time import sleep

# tamaño del tablero
maximo = 10

# función para inicializar los tableros de juego con los valores del usuario
def inicio_tableros(maximo, tableroA, tableroB, tableroA1, tableroB1):
    # llenamos todos los tableros con 0 (vacío)
    for i in range(maximo):
        for j in range(maximo):
            tableroA.append([0] * maximo)
            tableroA1.append([0] * maximo)
            tableroB.append([0] * maximo)
            tableroB1.append([0] * maximo)

# función para colocar un barco en el tablero
def colocar_barco(tableroA, tamano):
    # pedimos la orientación del barco (vertical u horizontal, 1 o 2)
    orientacion = 11
    while orientacion > 2 or orientacion < 1:
        orientacion = int(input("¿Qué orientación prefiere para el barco de tamaño " + str(tamano) + "? 1. Vertical 2. Horizontal: "))
        if orientacion > 2 or orientacion < 1:
            print("La opción que eligió no está dentro de las válidas, inténtelo de nuevo")

    # pedimos la posición inicial del barco
    primera_posicion = int(input("Ingrese la posición inicial del barco (en el eje vertical): "))
    segunda_posicion = int(input("Ingrese la posición inicial del barco (en el eje horizontal): "))

    # validamos que la posición sea válida para el barco (no se salga ni se sobreponga con otros barcos)
    while (primera_posicion < 1 or primera_posicion > maximo or segunda_posicion < 1 or segunda_posicion > maximo or 
           not es_posicion_valida(tableroA, primera_posicion, segunda_posicion, tamano, orientacion)):
        print("La ubicación que elegiste no es válida. Asegúrate de que el barco quepa en el tablero y no se solape.")
        primera_posicion = int(input("Ingrese la posición inicial del barco (en el eje vertical): "))
        segunda_posicion = int(input("Ingrese la posición inicial del barco (en el eje horizontal): "))

    # colocamos el barco en el tablero según la orientación
    # condicional para vertical
    if orientacion == 1:  
        for i in range(tamano):
            tableroA[primera_posicion - 1 + i][segunda_posicion - 1] = 1
    # condicional para horizontal
    elif orientacion == 2:  
        for i in range(tamano):
            tableroA[primera_posicion - 1][segunda_posicion - 1 + i] = 1

    # mostramos el tablero con el barco colocado
    for i in range(maximo):
        print(tableroA[i])

# función que valida que un barco no se sobreponga ni que se salga del tablero
def es_posicion_valida(tableroA, primera_posicion, segunda_posicion, tamano, orientacion):
    # conidcional para vertical
    if orientacion == 1:  
        # verificamos que el barco quepa en el tablero
        if primera_posicion + tamano - 1 > maximo:
            # el barco se sale del tablero, devuelve falso
            return False  
        # verificamos que no se sobreponga con otro barco
        for i in range(tamano):
            if tableroA[primera_posicion - 1 + i][segunda_posicion - 1] == 1:
                # el barco se sobrepone con otro, regresa falso
                return False  
    # condicional para horizontal
    elif orientacion == 2:  
        # verificamos que el barco quepa en el tablero
        if segunda_posicion + tamano - 1 > maximo:
            # el barco se sale del tablero, devuelve falso
            return False  
        # verificamos que no se sobroponga con otro barco
        for i in range(tamano):
            if tableroA[primera_posicion - 1][segunda_posicion - 1 + i] == 1:
                # el barco se sobrepone a otro, regresa falso
                return False  
    return True

# función para colocar todos los barcos de un jugador
def ubicacion_barcos(tableroA):
    # tamaños de los barcos (5, 4, 3, 3, 2) (porta aviones, buque, crucero, submarino, lancha)
    tamanos = [5, 4, 3, 3, 2]
    # colocamos cada barco de los tamaños indicados
    for tamano in tamanos:
        colocar_barco(tableroA, tamano)

if __name__ == "__main__":
    # bienvenida y reglas del juego
    print("Bienvenid@s sean al juego de astucia naval")
    print("Este consta de varias reglas de juego, que serán mostradas a continuación: ")
    print("Cada jugador tendrá dos tableros, uno para las posiciones de sus barcos y otro para los lugares donde atacará")
    print("Luego de ubicar sus barcos, cada jugador tendrá la oportunidad de derribar los del rival")
    print("Esto lo hará a partir de ataques a posiciones donde cree que estará el rival, y se le informará si impactó o no")
    print("Cuando todos los cuadrantes de un barco sean impactados, este se hundirá")
    print("El objetivo es que el rival se quede sin barcos mientras que tú los conserves")
    print("Decidan bien, buena suerte")   
    print("\n")
    
    # inicializamos los tableros
    tableroA = []
    tableroB = []
    tableroA1 = []
    tableroB1 = []
    
    # Inicializamos los tableros de ambos jugadores con sus valores
    inicio_tableros(maximo, tableroA, tableroA1, tableroB, tableroB1)

    # turno del jugador 1 para colocar sus barcos
    print("Es tu turno jugador 1")
    # colocamos los barcos del jugador 1
    ubicacion_barcos(tableroA)  

    # tiempo para que el cambio de turnos
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

    # turno del jugador 2 para colocar sus barcos
    print("Es tu turno jugador 2")
    # colocamos los barcos del jugador 2
    ubicacion_barcos(tableroB)  

    # tiempo para que el cambio de turnos
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

    # variables para verificar si ambos jugadores aún tienen barcos
    existencia1 = True
    existencia2 = True

    print("Hora de atacar")

    # mientras ambos jugadores tengan barcos, siguen jugando ("tengan 1'os en su tablero")
    while existencia1 and existencia2:
        # turno del jugador 1 para atacar
        # inicio de variables en falso para al final cambiar en caso de que sea necesario
        existencia2 = False
        existencia1 = False


        # muestra de tableros inicial
        print("Jugador 1, es tu turno")
        print("Este es tu tablero de barcos hasta el momento: ")
        for i in range(maximo):
            print(tableroA[i])
        print("Este es tu tablero de ataque hasta el momento: ")
        for i in range(maximo):
            print(tableroA1[i])

        # pedimos las posicion para el ataque
        primera_posicion = int(input("Ingrese el lugar donde quiera atacar (en el eje vertical): "))
        segunda_posicion = int(input("Ingrese el lugar donde quiera atacar (en el eje horizontal): "))
        
        # verificamos si el ataque fue exitoso
        if tableroB[primera_posicion - 1][segunda_posicion - 1] == 1: 
            tableroB[primera_posicion - 1][segunda_posicion - 1] = 6
            tableroA1[primera_posicion - 1][segunda_posicion - 1] = 2
            print("Buen trabajo, le diste")
        else: 
            tableroA1[primera_posicion - 1][segunda_posicion - 1] = 1
            print("Mejor suerte la próxima")

        # mostramos el tablero de ataques del jugador 1
        for i in range(maximo):
            print(tableroA1[i])

        # tiempo para el cambio de turnos
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

        # turno del jugador 2 para atacar
        print("Es tu turno, jugador 2")
        print("Este es tu tablero de barcos hasta el momento: ")
        for i in range(maximo):
            print(tableroB[i])
        print("Este es tu tablero de ataque hasta el momento: ")
        for i in range(maximo):
            print(tableroB1[i])

        # pedimos la posicion del ataque
        primera_posicion = int(input("Ingrese el lugar donde quiera atacar (en el eje vertical): "))
        segunda_posicion = int(input("Ingrese el lugar donde quiera atacar (en el eje horizontal): "))
        
        # verificamos si el ataque fue éxitoso
        if tableroA[primera_posicion - 1][segunda_posicion - 1] == 1: 
            tableroA[primera_posicion - 1][segunda_posicion - 1] = 6
            tableroB1[primera_posicion - 1][segunda_posicion - 1] = 2
            print("Buen trabajo, le diste")
        else: 
            tableroB1[primera_posicion - 1][segunda_posicion - 1] = 1
            print("Mejor suerte la próxima")            

        # mostramos el tablero de ataques del jugador 2
        for i in range(maximo):
            print(tableroB1[i])

        # comprobamos si aún quedan barcos en alguno de los tableros
        for i in range(maximo):
            if 1 in tableroA[i]: existencia1 = True
            if 1 in tableroB[i]: existencia2 = True
        
        # tiempo para que ambos jugadores se preparen para el siguiente turno (y no vean el otro tablero)
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

    # mensaje final del juego dependiendo del resultado (picaro si es empate)
    if not existencia1 and not existencia2:
        print("¡Felicidad, es un empate! ¿Quieren desempatar? Jueguen de nuevo.")
    elif not existencia1:
        print("Bien hecho jugador 2, ¡ganaste!")
    elif not existencia2:
        print("Bien hecho jugador 1, ¡ganaste!")
