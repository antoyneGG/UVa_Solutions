'''
Author: Fabian Antoyne Garcia Gallego
Problem: 1229 - Sub-Dictionary
Credits: tarjan2 and dfs-list-ady by Carlos Alberto Ramirez Restrepo
'''

from sys import stdin

n, t, numSCC = 101, 0, 0
G = [[] for _ in range(101)]
visited, low = [0 for _ in range(101)], [-1 for _ in range(101)]
inStack = [False for _ in range(101)]
incidency = [0 for _ in range(101)]
stack, sccNodes = [], []
subDictionary = []

def dfsAux(u):
    visited[u] = 1
    if(u not in subDictionary):
        subDictionary.append(u)

    for v in G[u]:
        if(visited[v] == -1):
            dfsAux(v)

def dfs():
    global n
    for i in range(n):
        visited[i] = -1
    
    for i in subDictionary:
        if(visited[i] == -1):
            dfsAux(i)

def tarjanAux(u):
    global G, t, numSCC
    t += 1
    visited[u], low[u] = t, t
    stack.append(u)
    inStack[u] = True

    for i in G[u]:
        incidency[i] += 1
        if(visited[i] == -1):
            tarjanAux(i)
            low[u] = min(low[u], low[i])
        elif(inStack[i]):
            low[u] = min(low[u], visited[i])
    
    if(low[u] == visited[u]):
        sccNodes.append([])
        numSCC += 1
        while(stack[-1] != u):
            a = stack.pop()
            inStack[a] = False
            sccNodes[numSCC - 1].append(a)
        
        a = stack.pop()
        inStack[a] = False
        sccNodes[numSCC - 1].append(a)


def tarjan():
    global n
    for i in range(n):
        low[i], visited[i] = -1, -1
        inStack[i] = False
        incidency[i] = 0
    
    for i in range(n):
        if(visited[i] == -1):
            tarjanAux(i)

def main():
    global n, numSCC, sccNodes, subDictionary
    n = int(stdin.readline())
    while(n != 0):
        values = []
        for i in range(n):
            G[i].clear()
        for i in range(n):
            words = list(map(str, stdin.readline().split()))
            for j in range(len(words)):
                if(words[j] not in values):
                    values.append(words[j])
                if(j != 0):
                    G[values.index(words[0])].append(values.index(words[j]))
        numSCC = 0
        sccNodes.clear()
        subDictionary.clear()

        tarjan()

        for i in sccNodes:
            if(len(i) > 1):
                for j in i:
                    subDictionary.append(j)

        dfs()

        print(len(subDictionary))

        subDictionary.sort(key=lambda x: values[x])
        for i in range(len(subDictionary)):
            print(values[subDictionary[i]], end='')
            if(i != len(subDictionary) - 1):
                print(" ", end='')
        print()
        n = int(stdin.readline())


main()