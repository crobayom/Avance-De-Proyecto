from math import fabs
from os import system
from time import sleep

maximo=4

if __name__=="__main__":
    print("Bienvenid@s sean al juego de astucia naval")
    print("Este consta de varias reglas de juego, que seran mostradas a continuacion: ")
    print("Cada jugador tendra su oportunidad ")    
    print("\n")
    tableroA=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    tableroB=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(maximo):
        print(tableroA[i])
    print("\n")
    for i in range(maximo):
        print(tableroB[i])
    print("\n") 

    print ("Es tu turno jugador 1")

    orientacion:int=11
    while orientacion>2 or orientacion<1:
        orientacion=int(input("¿Que orientacion prefiere? 1. Vertical 2. Horizontal: "))
        if orientacion>2 or orientacion<1:
            print("La opcion que elegio no esta dentro de las validas, intentelo de nuevo")

    primera_posicion:int=11
    while primera_posicion <1 or primera_posicion >maximo:
        primera_posicion=int(input("Ingrese el lugar donde pondra inicialmente su submarino (en el eje vertical): "))
        if primera_posicion <1 or primera_posicion >maximo:
            print("El valor que ingreso no esta dentro del rango permitido, intentelo de nuevo")
    segunda_posicion:int=11
    while segunda_posicion <1 or segunda_posicion >maximo:
        segunda_posicion=int(input("Ingrese el lugar donde pondra inicialmente su submarino (en el eje horizontal): "))
        if segunda_posicion <1 or segunda_posicion >maximo:
            print("El valor que ingreso no esta dentro del rango permitido, intentelo de nuevo")
    tableroA[primera_posicion-1][segunda_posicion-1]=1

    for i in range(maximo):
        print(tableroA[i])

    if orientacion==1:
        primera_posicion_siguiente:int=11
        while primera_posicion_siguiente <1 or primera_posicion_siguiente>maximo or fabs(primera_posicion-primera_posicion_siguiente)!=1 or primera_posicion==primera_posicion_siguiente:
            primera_posicion_siguiente=int(input("Ingrese el lugar donde pondra consecutivamente su submarino (en el eje vertical): "))
            if primera_posicion_siguiente <1 or primera_posicion_siguiente >maximo or primera_posicion==primera_posicion_siguiente:
                print("El valor que ingreso no esta dentro del rango permitido, intentelo de nuevo")
            if fabs(primera_posicion-primera_posicion_siguiente)!=1:
                print("El barco no puede estar tan lejos del inicio, intentelo de nuevo")
        tableroA[primera_posicion_siguiente-1][segunda_posicion-1]=1


    if orientacion==2:
        segunda_posicion_siguiente:int=11
        while segunda_posicion_siguiente<1 or segunda_posicion_siguiente >maximo or abs(segunda_posicion-segunda_posicion_siguiente)!=1:
            segunda_posicion_siguiente=int(input("Ingrese el lugar donde pondra consecutivamente su submarino (en el eje horizontal): "))
            if segunda_posicion_siguiente <1 or segunda_posicion_siguiente >maximo or abs(segunda_posicion-segunda_posicion_siguiente)!=1:
                print("El valor que ingresaste no esta dentro del rango permitido, intentelo de nuevo")
        tableroA[primera_posicion-1][segunda_posicion_siguiente-1]=1
        
    for i in range(maximo):
        print(tableroA[i])

    sleep(3)

    system("cls")

    print ("Es tu turno jugador 2")

    orientacion:int=11
    while orientacion>2 or orientacion<1:
        orientacion=int(input("¿Que orientacion prefiere? 1. Vertical 2. Horizontal: "))
        if orientacion>2 or orientacion<1:
            print("La opcion que elegio no esta dentro de las validas, intentelo de nuevo")

    primera_posicion:int=11
    while primera_posicion <1 or primera_posicion >maximo:
        primera_posicion=int(input("Ingrese el lugar donde pondra inicialmente su submarino (en el eje vertical): "))
        if primera_posicion <1 or primera_posicion >maximo:
            print("El valor que ingreso no esta dentro del rango permitido, intentelo de nuevo")

    segunda_posicion:int=11
    while segunda_posicion <1 or segunda_posicion >maximo:
        segunda_posicion=int(input("Ingrese el lugar donde pondra inicialmente su submarino (en el eje horizontal): "))
        if segunda_posicion <1 or segunda_posicion >maximo:
            print("El valor que ingreso no esta dentro del rango permitido, intentelo de nuevo")
    tableroB[primera_posicion-1][segunda_posicion-1]=1

    for i in range(maximo):
        print(tableroB[i])

    if orientacion==1:
        primera_posicion_siguiente:int=11
        while primera_posicion_siguiente <1 or primera_posicion_siguiente >maximo or fabs(primera_posicion-primera_posicion_siguiente)!=1 or primera_posicion==primera_posicion_siguiente:
            primera_posicion_siguiente=int(input("Ingrese el lugar donde pondra consecutivamente su submarino (en el eje vertical): "))
            if primera_posicion_siguiente <1 or primera_posicion_siguiente >maximo or fabs(primera_posicion-primera_posicion_siguiente)!=1 or primera_posicion==primera_posicion_siguiente:
                print("El valor que ingreso no esta dentro del rango permitido, intentelo de nuevo")
        tableroB[primera_posicion-1][segunda_posicion-1]=1


    if orientacion==2:
        segunda_posicion_siguiente:int=11
        while segunda_posicion_siguiente<1 or segunda_posicion_siguiente >maximo or abs(segunda_posicion-segunda_posicion_siguiente)!=1 or segunda_posicion==segunda_posicion_siguiente:
            segunda_posicion_siguiente=int(input("Ingrese el lugar donde pondra consecutivamente su submarino (en el eje horizontal): "))
            if segunda_posicion_siguiente <1 or segunda_posicion_siguiente >maximo or abs(segunda_posicion-segunda_posicion_siguiente)!=1 or segunda_posicion==segunda_posicion_siguiente:
                print("El valor que ingresaste no esta dentro del rango permitido, intentelo de nuevo")
        tableroB[primera_posicion-1][segunda_posicion_siguiente-1]=1
        
    for i in range(maximo):
        print(tableroB[i])

    sleep(3)

    system("cls")

    existencia1:bool=1
    existencia2:bool=1

    print("Hora de atacar")

    tableroA1=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    tableroB1=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    while existencia1==1 and existencia2==1:
        existencia2=False
        existencia1=False

        print("Jugador 1, es tu turno")
        print("Este es tu tablero hasta el momento: ")
        for i in range(maximo):
            print(tableroA[i])


        primera_posicion:int=11
        while primera_posicion <1 or primera_posicion >maximo:
            primera_posicion=int(input("Ingrese el lugar donde quiera atacar (en el eje vertical): "))
            if primera_posicion <1 or primera_posicion >maximo:
                print("El valor que ingreso no esta dentro del rango permitido, intentelo de nuevo")

        segunda_posicion:int=11
        while segunda_posicion <1 or segunda_posicion >maximo:
            segunda_posicion=int(input("Ingrese el lugar donde quiera atacar (en el eje horizontal): "))
            if segunda_posicion <1 or segunda_posicion >maximo:
                print("El valor que ingreso no esta dentro del rango permitido, intentelo de nuevo")
        
        if tableroB[primera_posicion-1][segunda_posicion-1]==1: 
            tableroB[primera_posicion-1][segunda_posicion-1]=6
            tableroA1[primera_posicion-1][segunda_posicion-1]=2
            print("Buen trabajo, le diste")
        else: 
            tableroA1[primera_posicion-1][segunda_posicion-1]=1
            print("Mejor suerte la proxima")

        for i in range (maximo):
            print(tableroA1[i])

        print ("Es tu turno, jugador 2")

        print("Este es tu tablero hasta el momento: ")
        for i in range(maximo):
            print(tableroB[i])

        primera_posicion:int=11
        while primera_posicion <1 or primera_posicion >maximo:
            primera_posicion=int(input("Ingrese el lugar donde quiera atacar (en el eje vertical): "))
            if primera_posicion <1 or primera_posicion >maximo:
                print("El valor que ingreso no esta dentro del rango permitido, intentelo de nuevo")

        segunda_posicion:int=11
        while segunda_posicion <1 or segunda_posicion >maximo:
            segunda_posicion=int(input("Ingrese el lugar donde quiera atacar (en el eje horizontal): "))
            if segunda_posicion <1 or segunda_posicion >maximo:
                print("El valor que ingreso no esta dentro del rango permitido, intentelo de nuevo")
        
        if tableroA[primera_posicion-1][segunda_posicion-1]==1: 
            tableroA[primera_posicion-1][segunda_posicion-1]=6
            tableroB1[primera_posicion-1][segunda_posicion-1]=2
            print("Buen trabajo, le diste")
        else: 
            tableroB1[primera_posicion-1][segunda_posicion-1]=1
            print("Mejor suerte la proxima")            

        for i in range (maximo):
            print(tableroB1[i])

        for i in range(maximo):
            if 1 in tableroA[i]: existencia1=True
            if 1 in tableroB[i]: existencia2=True
    if existencia1!=True and existencia2!=True:
        print("Felicidad, es un empate, quieren desempatar? Jueguemos de nuevo")
    elif existencia1!=True:
        print("Bien hecho jugador 2, ganaste")
    elif existencia2!=True:
        print("Bien hecho jugador 1, ganaste")