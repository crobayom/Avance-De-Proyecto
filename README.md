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

#### N°1 creación de matrices.
#### N° 2 Validación de caracteres.
#### N°3 Posición inicial de los barcos.

https://drive.google.com/drive/folders/1pBN8QKg-8Vz7DXRBARyeN_0zb8beR5JW?usp=sharing

#### N°4 Existencia de barcos

https://drive.google.com/file/d/1YcSZ9uppXao64HunNIpZPWw5Zftk6-qg/view?usp=sharing

## Solucion Preliminar

En el archivo adjuntado
    elif existencia1!=True:
        print("Bien hecho jugador 2, ganaste")
    elif existencia2!=True:
        print("Bien hecho jugador 1, ganaste")
```

