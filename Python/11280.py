'''
Author: Fabian Antoyne Garcia Gallego
Problem: 11280 - Flying to Fredericton
Credits: bellmanFord by Carlos Alberto Ramirez Restrepo
'''

from sys import stdin

n = 101
G = [[] for _ in range(101)]
citiesNumbers = {}
numbersCities = {}

def bellmanFord(s, queries):
    global n
    #ans = True
    d = [[float('inf') for _ in range(n)] for _ in range(n)]
    p = [-1 for _ in range(n)]

    d[0][0] = 0
    for i in range(1, n):
        for v in range(n):
            d[i][v] = min(d[i][v], d[i - 1][v])
            for (u, weight) in G[v]:
                if d[i][u] > d[i - 1][v] + weight:
                    d[i][u] = d[i - 1][v] + weight
                    p[u] = v
    
    '''u = 0
    while ans and u < len(G):
        i = 0
        while ans and i < len(G[u]):
            v = G[u][i][0]
            weight = G[u][i][1]
            if d[n - 1][v] > d[n - 1][u] + weight:
                ans = False
            i += 1
        u += 1'''

    #print(d)
    #print(p)
    print(f'Scenario #{s + 1}')
    #print(d)
    for q in queries:
        #print(q)
        while(q + 1 >= len(d)):
            q -= 1
        if(d[q + 1][n - 1] != float('inf')):
            print(f'Total cost of flight(s) is ${d[q + 1][n - 1]}')
        else:
            print(f'No satisfactory flights')

def main():
    global n
    s = int(stdin.readline())
    cont = 0
    while(cont != s):
        blank = stdin.readline()
        n = int(stdin.readline())
        for i in range(n):
            G[i].clear()
        citiesNumbers = {}
        numbersCities = {}
        queries = []
        for i in range(n):
            city = str(stdin.readline().strip())
            numbersCities[i] = city
            citiesNumbers[city] = i
        #print(numbersCities)
        #print(citiesNumbers)
        m = int(stdin.readline())
        for i in range(m):
            city1, city2, cost = list(map(str, stdin.readline().split()))
            G[citiesNumbers[city1]].append((citiesNumbers[city2], int(cost)))
        line = list(map(int, stdin.readline().split()))
        for i in range(1, line[0] + 1):
            queries.append(line[i])
        #print(G)
        #print(queries)

        bellmanFord(cont, queries)
        cont += 1
        if(cont != s):
            print()

main()