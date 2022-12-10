'''
Author: Fabian Antoyne Garcia Gallego
Problem: 12376 - As Long as I Learn, I Live
Credits: dfs-list-ady by Carlos Alberto Ramirez Restrepo
'''

from sys import stdin

n = 101
sum = 0
last = 0
G = [[] for _ in range(n)]
visited = [False for _ in range(n)]
values = []

def dfsAux(u):
    global visited, n, values, sum, last
    visited[u] = True
    sum += values[u]
    v = 0
    max = 0
    for i in G[u]:
        if(values[i] > max):
            max = values[i]
            v = i
    last = u
    if(v != 0):
        dfsAux(v)

def dfs():
    global visited, n
    for i in range(n):
        visited[i] = False
    dfsAux(0)

def main():
    global G, n, values, sum, last
    T = int(stdin.readline())
    for t in range(T):
        line = stdin.readline()
        n, m = map(int, stdin.readline().split())
        for i in range(n):
            G[i].clear()
        values = list(map(int, stdin.readline().split()))
        for i in range(m):
            u, v = map(int, stdin.readline().split())
            G[u].append(v)
        sum = 0
        dfs()
        print(f'Case {t + 1}: {sum} {last}')        

main()