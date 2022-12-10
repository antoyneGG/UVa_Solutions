'''
Autor: Fabian Antoyne Garcia Gallego
Codigo: 8956118
Codigo de honor: Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
a seguir los más altos estándares de integridad académica.
'''

# Entrada: Un arreglo A[0...N), una cantidad de vueltas c, una capacidad maxima por vuelta L, el tamaño N de la 
# cola y el diccionario mem donde se almacenaran los resultados ya calculados.
# Salida: El numero maximo de ganancias que se puede obtener durante las c vueltas de la atraccion.
# Objetivo: Esta funcion basicamente aplica el algoritmo solucion que se ideo, el cual consiste en que si ya se
# sabe cuanto se gana en una vuelta en donde se conoce cual es el primer grupo en ingresar se toma este valor del
# diccionario y tambien se toma cual es el siguiente grupo a ingresar despues de dicha vuelta, si esto no se
# encuentra ya calculado se procede a calcular recorriendo la lista de grupos desde el primer grupo que esta por
# ingresar hasta que la capacidad lo permita, se va calculando cuanto se recauda en dicha vuelta y se guarda esto
# junto con el ultimo grupo que no pudo ingresar.
def phiIt2(A, c, L, N, mem):
    ans = 0
    n = 0
    while(c > 0): #Ciclo que recorre todas las vueltas del dia
        if(n in mem.keys()): #Se revisa si ya se conoce el resultado de la vuelta que comenzaria con el grupo de personas en n
            subAns, newN = mem[n]
            ans += subAns
            n = newN
            c -= 1
        else:
            cant = 0
            i = n #Se guarda una copia de donde comienza la vuelta
            l = L #Se guarda una copia de la capacidad maxima para ir evaluando cuantos grupos de personas pueden ir en esta vuelta
            subAns = 0
            while(l - A[i] >= 0 and cant != N): #Ciclo que agrega grupos de personas mientras no se pase el limite
                subAns += A[i]
                l -= A[i]
                i += 1
                cant += 1
                if(i == N): i = 0 #Se le da la vuelta completa a la cola
            mem[n] = (subAns, i) #Se guarda el resultado para la vuelta que comienza con el grupo de personas en n
            ans += subAns
            n = i #Se pasa al ultimo grupo de personas que no alcanzo a ingresar
            c -= 1
    return ans

# Funcion que se encarga de recibir los datos de entrada del problema para enviarlos hacia la funcion de solucion.
def main():
    L, c, n = [int(i) for i in input().split()]
    A = []

    for _ in range(n):
        pi = int(input())
        A.append(pi)

    mem = {} #Se reinicia la memoria para cada ejecucion
    print(phiIt2(A, c, L, n, mem))

main()