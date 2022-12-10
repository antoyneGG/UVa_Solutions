'''
Author: Fabian Antoyne Garcia Gallego
Problem: 383 - Shipping Routes
Credits: bfs-list-ady by Carlos Alberto Ramirez Restrepo
'''

from sys import stdin
from collections import deque

m = 30
G = [[] for _ in range(30)]
visited = [False for _ in range(30)]

def bfsAux(u, D):
    legs = 1
    next = -1
    found = False
    nextFound = False
    queue = deque()
    queue.append(u)
    visited[u] = True
    while(len(queue) != 0 and not found):
        nextFound = False
        v = queue.popleft()
        if(v == next):
            legs += 1
        for i in range(len(G[v])):
            w = G[v][i]
            if(w == D):
                found = True
            elif(visited[w] == False):
                if(not nextFound):
                    next = w
                    nextFound = True
                queue.append(w)
                visited[w] = True
    if(found):
        return legs
    else:
        return 0

def bfs(u, D):
    for i in range(m):
        visited[i] = False
    return bfsAux(u, D)

def main():
    global G, visited, m
    T = int(stdin.readline())
    print("SHIPPING ROUTES OUTPUT")
    print()
    for t in range(T):
        m, n, p = list(map(int, stdin.readline().split()))
        values = list(map(str, stdin.readline().split()))
        warehouses = {}
        for i in range(m):
            G[i].clear()
            warehouses[values[i]] = i
        for i in range(n):
            w1, w2 = list(map(str, stdin.readline().split()))
            G[warehouses[w1]].append(warehouses[w2])
            G[warehouses[w2]].append(warehouses[w1])
        print(f'DATA SET  {t + 1}')
        print()
        for i in range(p):
            shipping_route = stdin.readline().split()
            #print(bfs(warehouses[shipping_route[1]], warehouses[shipping_route[2]]))
            minimumLegs = bfs(warehouses[shipping_route[1]], warehouses[shipping_route[2]])
            if(minimumLegs == 0):
                print("NO SHIPMENT POSSIBLE")
            else:
                print(f'${(100 * int(shipping_route[0])) * minimumLegs}')
        print()
    print("END OF OUTPUT")

main()