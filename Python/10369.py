'''
Author: Fabian Antoyne Garcia Gallego
Problem: 10369 - Artic Network
Credits: prim by Carlos Alberto Ramirez Restrepo
'''

from sys import stdin
from heapq import heappop, heappush
import math

p = 500
G = [[] for _ in range(500)]

def prim(s, satellites):
    global p
    queue = []
    d = [0 for _ in range(p)]
    father = [-1 for _ in range(p)]
    visited = [False for _ in range(p)]
    for i in range(p):
        d[i] = float("inf")

    total = 0
    cont = 0
    d[s] = 0
    heappush(queue, (0, s))
    while(len(queue) > 0):
        weight, u = heappop(queue)
        visited[u] = True
        #print(f'({weight}, {u})')
        if(weight == d[u]):
            total += weight
            '''cont += 1
            print(f'Cont: {cont} con {weight}')
            if(cont == satellites):
                print(weight)'''
            for(v, weightAux) in G[u]:
                if(not visited[v] and weightAux < d[v]):
                    father[v] = u
                    d[v] = weightAux
                    heappush(queue, (d[v], v))
    #print(total)
    #print(father)
    d.sort(reverse=True)
    #print(d)
    print(f'{d[satellites - 1]:.2f}')
    return total

def main():
    global p
    n = int(stdin.readline())
    while(n != 0):
        s, p = list(map(int, stdin.readline().split()))
        for i in range(p):
            G[i].clear()

        coordinates = []
        for i in range(p):
            x, y = list(map(int, stdin.readline().split()))
            coordinates.append([x, y])
            #d = abs(math.sqrt(((x2-x1)**2)+((y2-y1)**2)))
        
        #coordinates.sort(key= lambda x: [x[1], x[0]])
        #print(coordinates)
        for c1 in range(p):
            for c2 in range(c1, p):
                d = abs(math.sqrt(((coordinates[c2][0] - coordinates[c1][0])**2)+((coordinates[c2][1] - coordinates[c1][1])**2)))
                G[c1].append((c2, d))
                G[c2].append((c1, d))
        

        #print(G)
        prim(0, s)
        n -= 1


main()