'''
Author: Fabian Antoyne Garcia Gallego
Problem: 12645 - Water Supply
Credits: ts-list-ady by Carlos Alberto Ramirez Restrepo
'''
from sys import setrecursionlimit 
from sys import stdin
from collections import deque

setrecursionlimit(100000)

n = 1001
m = 100001
pipelines = 0
G = [[] for _ in range(n)]
visited = [False for i in range(n)]
topo = deque()

def topoSAux(v):
    global visited, topo
    visited[v] = True

    for u in G[v]:
        if(not visited[u]):
            topoSAux(u)

    topo.appendleft(v)

def topoS():
    global visited, topo, n
    for i in range(n):
        visited[i] = False
    for i in range(n):
        if(not visited[i]):
            topoSAux(i)

def dfsAux(v):
    global G, visited
    visited[v] = True

    for i in G[v]:
        if(not visited[i]):
            dfsAux(i)

def dfs():
    global visited, topo, pipelines, n
    for i in range(n):
        visited[i] = False
    pipelines = 0
    for i in topo:
        if(not visited[i]):
            #print(i)
            dfsAux(i)
            if(i != 0):
                pipelines += 1

def main():
    global n, m, G, pipelines, topo
    line = stdin.readline().split()
    while(line != []):
        pipelines = 0
        n, m = list(map(int, line))
        n += 1
        #print(n - 1, " ", m)
        for i in range(n):
            G[i].clear()
        for i in range(m):
            u, v = list(map(int, stdin.readline().split()))
            G[u].append(v)
        topo.clear()
        topoS()
        #print(topo)
        dfs()
        print(pipelines)

        line = stdin.readline().split()

main()
