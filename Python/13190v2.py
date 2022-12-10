'''
Autor: Fabian Antoyne Garcia Gallego
Ejercicio numero 13190 de uVa: Rockabye Tobby
Resumen de la solucion aplicada: Se utiliza el modulo heapQueue para crear usar una lista como cola de 
prioridad, y en esta se ingresan listas que contienen el momento de la medicina, su prioridad, su nombre y su 
frecuencia. Entonces a medida que se va avanzando en la cola de prioridad extrayendo cada medicina en cada mo-
mento indicado, esta misma medicina se va actualizando a su siguiente momento segun su respectiva frecuencia
e ingresandola a la cola de prioridad de manera que se vuelva a organizar segun su momento, o en caso de igualdad
con otras medicinas, por prioridad.
'''

from sys import stdin
from heapq import heappush, heappop

def main():
    T = int(stdin.readline())
    for i in range(T):
        n, k = list(map(int, stdin.readline().split()))
        medicines = []
        for j in range(n):
            name, frecuency = list(stdin.readline().split())
            frecuency = int(frecuency)
            heappush(medicines, [frecuency, j, name, frecuency])
        for j in range(k):
            item = heappop(medicines)
            print(f'{item[0]} {item[2]}')
            item[0] += item[3]
            heappush(medicines, item)


main()