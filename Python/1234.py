'''
Author: Fabian Antoyne Garcia Gallego
Problem: 1234 - RACING
Credits: prim by Carlos Alberto Ramirez Restrepo
'''

from sys import stdin
from heapq import heappop, heappush

n = 10000
G = [[] for _ in range(10000)]
d = [0 for _ in range(10000)]

def prim():
    global n
    queue = []
    visited = [False for _ in range(n)]
    for i in range(n):
        d[i] = float("-inf")
    
    total = 0
    d[1] = 0
    heappush(queue, (0, 1))
    while(len(queue) > 0):
        weight, u = heappop(queue)
        weight *= -1
        visited[u] = True
        #print(f'llegue a {u}')
        if(weight == d[u]):
            total += weight

            for(v, weightAux) in G[u]:
                if(not visited[v] and weightAux > d[v]):
                    d[v] = weightAux
                    heappush(queue, (d[v] * -1, v))
    print(total)
    return total

def main():
    global n
    c = int(stdin.readline())
    for t in range(c):
        line = list(map(int, stdin.readline().split()))
        n, m = line[0], line[1]
        n += 1
        suma = 0
        for i in range(n):
            G[i].clear()

        for i in range(m):
            line = list(map(int, stdin.readline().split()))
            x, y, weight = line[0], line[1], line[2]
            G[x].append((y, weight))
            G[y].append((x, weight))
            suma += weight
        print(suma)
        print(suma - prim())
        



main()