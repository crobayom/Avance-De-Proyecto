# Astucia Naval
#### Cristian Eduardo Robayo Martinez
#### Carlos David Pinto Guzman


## Definicion de la Alternativa: 

La alternativa que elegimos es de caracter libre y propositiva, mantenemos el orden anterior continuando con juegos; En este caso, el conocido juego de estrategia, nuestra idea es replicarlo (dentro de lo posible) lo mas identico al original, es decir, 4 tableros (2 para las posiciones de los barcos y 2 para los intentos de hundirlos), con la posibilidad de el propio jugador ubicar sus barcos cual si fuera en el juego fisico (en cualquier lugar siempre y cuando este orientado vertical y horizontalmente y este dentro de los limites del tablero) 

## Algoritmos Reconocidos


## 1. La creación de matrices:
Los ocho tableros se crean como matrices de cuatro por cuatro, como en este caso los son los dos tableros de A y los dos tableros de B, en el que se hubicaran los barcos.
   
```
tableroA = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
tableroB = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
```


## 2. Validación de carecteres: 
se utiliza el condicional While para que el usuario elija un valor dentro de ese rango, de lo contrario, se pedirá que introdusca otro valor.

```
while orientacion > 2 or orientacion < 1:
    orientacion = int(input("¿Qué orientación prefiere? 1. Vertical 2. Horizontal: "))
    if orientacion > 2 or orientacion < 1:
        print("La opción que eligió no está dentro de las válidas, inténtelo de nuevo")
```


## 3. Posición inicial de los barcos:

### Diagramas Respectivos



## Solucion Preliminar

