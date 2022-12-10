'''
Author: Fabian Antoyne Garcia Gallego
Problem: 11749 - Poor Trade Advisor
Credits: dfs-list-ady by Carlos Alberto Ramirez Restrepo
'''

from sys import stdin

cities = 0
maxCities = 0
n = 500
G = [[] for _ in range(n)]
visited = [False for _ in range(n)]

def dfsAux(u):
    global cities, G
    visited[u] = True
    cities += 1
    #print(u, " -> ", end="")
    for v in G[u]:
        if(not visited[v]):
            dfsAux(v)

def dfs():
    global n, cities, maxCities
    for i in range(n):
        visited[i] = False
    
    for i in range(n):
        if(not visited[i]):
            cities = 0
            dfsAux(i)
            #print()
            if(cities > maxCities):
                maxCities = cities
            #print(cities)

def main():
    global n, G, maxCities
    n, m = list(map(int, stdin.readline().split()))
    while(n != 0 and m != 0):
        max = float('-inf')
        maxCities = 2
        for i in range(n):
            G[i].clear()
        for i in range(m):
            u, v, val = list(map(int, stdin.readline().split()))
            u -= 1
            v -= 1
            if(val > max):
                max = val
                edges = []
            if(val == max):
                edges.append([u,v,val])
        if(n > 2 and m > 1):
            while(edges != []):
                G[edges[-1][0]].append(edges[-1][1])
                G[edges[-1][1]].append(edges[-1][0])
                edges.pop()
            #print(max)
            #print(G)
            dfs()
        print(maxCities)

        n, m = list(map(int, stdin.readline().split()))
        

main()