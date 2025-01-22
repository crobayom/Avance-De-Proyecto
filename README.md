# Odissey

```python
def matris (nfilas:int, ncolumnas:int) -> None:
    matriz=[]
    filas=[]
    for i in range(nfilas):
        for j in range(ncolumnas):    
            filas.append(int(input("Ingrese: ")))
        matriz.append(filas)
        filas=[]
        print(matriz)


if __name__=="__main__":
    nfilas:int=int(input("Ingrese la cantidad de filas de la matriz: "))
    ncolumnas:int=int(input("Ingrese el cantidad de columnas de la matriz: "))
    matris(nfilas, ncolumnas)
```
