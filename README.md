# Astucia Naval
#### Cristian Eduardo Robayo Martinez
#### Carlos David Pinto Guzman


## Definicion de la Alternativa: 

La alternativa que elegimos es de caracter libre y propositiva, mantenemos el orden anterior continuando con juegos; En este caso, el conocido juego de estrategia, nuestra idea es replicarlo (dentro de lo posible) lo mas identico al original, es decir, 4 tableros (2 para las posiciones de los barcos y 2 para los intentos de hundirlos), con la posibilidad de el propio jugador ubicar sus barcos cual si fuera en el juego fisico (en cualquier lugar siempre y cuando este orientado vertical y horizontalmente y este dentro de los limites del tablero) 

## Algoritmos Reconocidos


## 1. La creación de matrices:
Los ocho tableros se crean como matrices de cuatro por cuatro, como en este caso los son los dos tableros de __A__ y los dos tableros de __B__ , en el que se hubicaran los barcos.
   
```python
tableroA = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
tableroB = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
```


## 2. Validación de carecteres: 
se utiliza el condicional __While__ para que el usuario elija un valor dentro de ese rango, de lo contrario, se pedirá que introdusca otro valor.

```python
while orientacion > 2 or orientacion < 1:
    orientacion = int(input("¿Qué orientación prefiere? 1. Vertical 2. Horizontal: "))
    if orientacion > 2 or orientacion < 1:
        print("La opción que eligió no está dentro de las válidas, inténtelo de nuevo")
```


## 3. Posición inicial de los barcos:
El usuario introduce las coordenadas del barco y se verifica que el valor esté dentro del rango de la matriz (1-4), para luego actualizar el tablero marcado con un 1.

```python
while primera_posicion < 1 or primera_posicion > 4:
    primera_posicion = int(input("Ingrese el lugar donde pondrá inicialmente su submarino (en el eje vertical): "))
while segunda_posicion < 1 or segunda_posicion > 4:
    segunda_posicion = int(input("Ingrese el lugar donde pondrá inicialmente su submarino (en el eje horizontal): "))
tableroA[primera_posicion - 1][segunda_posicion - 1] = 1
```


## 4. Posición consecutiva de los barcos:
se utiliza __fabs__ y __ads__ para garantizar la primera posicón del barco, con la segunda posición (vertical u horizontal)
con diferencias absolutas.

```python
if orientacion == 1:  # Vertical
    while fabs(primera_posicion - primera_posicion_siguiente) != 1:
        primera_posicion_siguiente = int(input("Ingrese el lugar donde pondrá consecutivamente su submarino (en el eje vertical): "))
    tableroA[primera_posicion_siguiente - 1][segunda_posicion - 1] = 1
if orientacion == 2:  # Horizontal
    while abs(segunda_posicion - segunda_posicion_siguiente) != 1:
        segunda_posicion_siguiente = int(input("Ingrese el lugar donde pondrá consecutivamente su submarino (en el eje horizontal): "))
    tableroA[primera_posicion - 1][segunda_posicion_siguiente - 1] = 1
```



## 5. Limpieza de la consola:

Utilizamos __system("cls")__ para limpiar la pantalla despues de cada turno.

```python
system("cls")
```
se repite el mismo procedimiento con el jugador dos, en el tablero __B__


## 6. Turnos de ataque:
se inicia con las matricez __tableroA1__ y __tableroB1__ para registrar los ataques durante la partida.

```python
tableroA1 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
tableroB1 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
```


### Diagramas Respectivos

## N°1 creación de matrices.

   https://app.diagrams.net/#G1IgsWVnjGFtp7gWwPxUwFyPQ81WmGyWrx#%7B%22pageId%22%3A%226BqPHSdggr4rniQLIDKM%22%7D

   https://drive.google.com/file/d/1IgsWVnjGFtp7gWwPxUwFyPQ81WmGyWrx/view?usp=drive_link

## N° 2 Validación de caracteres.

https://app.diagrams.net/#G1IgsWVnjGFtp7gWwPxUwFyPQ81WmGyWrx#%7B%22pageId%22%3A%22-vL5OHhv7YS65zEQdmQu%22%7D

## N°3 Posición inicial de los barcos.

https://app.diagrams.net/#G1IgsWVnjGFtp7gWwPxUwFyPQ81WmGyWrx#%7B%22pageId%22%3A%228ytgzqPscw4pmnxwvf8O%22%7D

## N°4 Posición consecutiva de los barcos.

https://app.diagrams.net/#G1IgsWVnjGFtp7gWwPxUwFyPQ81WmGyWrx#%7B%22pageId%22%3A%22jDEkvbeky_YqCtiKYqmT%22%7D

##

## Solucion Preliminar


```python
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
```

