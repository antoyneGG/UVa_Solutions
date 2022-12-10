'''
Autor: Fabian Antoyne Garcia Gallego
Codigo: 8956118
Ejercicio A: K-Smallest Sums
'''

from sys import stdin
from heapq import heappop, heappush

def smallest(matrix, k):
    matrix[0].sort()
    ans = matrix[0]
    for i in range(1, k):
        matrix[i].sort()
        pqueue = []
        top = 0
        j = 0
        temp = ans
        ans = []
        impr = True
        while(j < k):
            r = 0
            if(impr and (len(pqueue) == 0 or matrix[i][j] + temp[r] < top)):
                while(r < k):
                    heappush(pqueue, matrix[i][j] + temp[r])
                    r += 1
                top = matrix[i][j] + temp[r - 1]
                #print(f'suma iiiilegal: {matrix[i][j] + temp[r]}')
                #print(pqueue)
                #print(pqueue[-1])
                #print(f'los mejores son: {temp} y se salta con {matrix[i][j]}')
            else:
                impr = False
                        
            #print("pequenio: ", pqueue[0])
            #print("grande: ", pqueue[-1])
            #print("cola: ", pqueue)
            ans.append(heappop(pqueue))
            #print("cola: ", pqueue)
            #print(f'temporal: {temp} y ans: {ans}')
            #print("este es ans: ", ans)
            j += 1
        #print("sali de fila: ", ans)
        #print(pqueue)    
    return ans

def main():
    k = int(stdin.readline())
    while(k != ''):
        k = int(k)
        matrix = [ list(map(int, stdin.readline().split())) for _ in range(k) ]
        #print(matrix)
        print(' '.join(list(map(str, smallest(matrix, k)))))

        k = stdin.readline()

main()
