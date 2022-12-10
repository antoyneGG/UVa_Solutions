'''
Author: Fabian Antoyne Garcia Gallego
Problem: 10731 - Test
Credits: tarjan2 by Carlos Alberto Ramirez Restrepo
'''

from sys import stdin

numAlpha = { 
    0 : 'A',
    1 : 'B',
    2 : 'C',
    3 : 'D',
    4 : 'E',
    5 : 'F',
    6 : 'G',
    7 : 'H',
    8 : 'I',
    9 : 'J',
    10 : 'K',
    11 : 'L',
    12 : 'M',
    13 : 'N',
    14 : 'O',
    15 : 'P',
    16 : 'Q',
    17 : 'R',
    18 : 'S',
    19 : 'T',
    20 : 'U',
    21 : 'V',
    22 : 'W',
    23 : 'X',
    24 : 'Y',
    25 : 'Z'
}

alphaNum = { 
    'A' : 0,
    'B' : 1,
    'C' : 2,
    'D' : 3,
    'E' : 4,
    'F' : 5,
    'G' : 6,
    'H' : 7,
    'I' : 8,
    'J' : 9,
    'K' : 10,
    'L' : 11,
    'M' : 12,
    'N' : 13,
    'O' : 14,
    'P' : 15,
    'Q' : 16,
    'R' : 17,
    'S' : 18,
    'T' : 19,
    'U' : 20,
    'V' : 21,
    'W' : 22,
    'X' : 23,
    'Y' : 24,
    'Z' : 25
}

G = [[] for _ in range(26)]
visited, low = [0 for _ in range(26)], [-1 for _ in range(26)]
inStack = [False for _ in range(26)]
n, t, numScc = int(), 0, 0
sccNodes, stack = [], []
questions = []

def tarjanAux(v):
    global t, numScc
    t += 1
    visited[v], low[v] = t, t
    stack.append(v)
    inStack[v] = True

    for i in G[v]:
        if(visited[i] == -1):
            tarjanAux(i)
            low[v] = min(low[v], low[i])
        elif(inStack[i]):
            low[v] = min(low[v], visited[i])
    
    if(low[v] == visited[v]):
        sccNodes.append([])
        numScc += 1
        while(stack[-1] != v):
            a = stack.pop()
            inStack[a] = False
            sccNodes[numScc - 1].append(a)
        
        a = stack.pop()
        inStack[a] = False
        sccNodes[numScc - 1].append(a)

def tarjan():
    for i in range(26):
        low[i], visited[i] = -1, -1
        inStack[i] = False
    
    for i in questions:
        if( visited[i] == -1):
            tarjanAux(i)

def main():
    global numScc
    n = int(stdin.readline())
    while(n != 0):
        questions.clear()
        for i in range(26):
            G[i].clear()
        for i in range(n):
            values = list(map(str, stdin.readline().split()))
            u = values[5]
            for j in range(5):
                if(values[j] != u):
                    G[alphaNum[u]].append(alphaNum[values[j]])
                if(alphaNum[values[j]] not in questions):
                    questions.append(alphaNum[values[j]])
        #print(G)
        tarjan()
        #print(sccNodes)
        for i in sccNodes:
            if(len(i) > 1):
                i.sort()
        sccNodes.sort()
        #print(sccNodes)
        for i in sccNodes:
            for j in range(len(i)):
                print(numAlpha[i[j]], end='')
                if(j != len(i) - 1):
                    print(" ", end='')
            print()
        sccNodes.clear()
        numScc = 0
        n = int(stdin.readline())
        if(n != 0):
            print()

main()