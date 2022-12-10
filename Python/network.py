'''
Autor: Fabian Antoyne Garcia Gallego
Codigo: 8956118
Ejercicio C: Corporative Network
Ejemplo de conjuntos disyuntos tomados del pseudo-codigo de la presentacion del profesor Carlos Ramirez
'''

from sys import stdin

n = 20100
f = [0 for _ in range(n)]
#r = [0 for _ in range(n)]
dist = [0 for _ in range(n)]

def makeSet(v):
    f[v], dist[v] = v, 0

def findSet(v):
    if(v == f[v]):
        return v
    else:
        f[v] = findSet(f[v])
        return f[v]

def findDist(v):
    #print(f'hijo: {v} padre: {f[v]}')
    if(v == f[v] or f[v] == f[f[v]]):
        return dist[v]
    else:
        dist[v] = dist[v] + findDist(f[v])
        findSet(v)
        return dist[v]

def unionSet(u, v):
    #u, v = findSet(u), findSet(v)
    if(u != v):
        f[v] = u
        dist[v] = abs(u - v) % 1000

def main():
    T = int(stdin.readline())
    while(T > 0):
        n = int(stdin.readline())
        n += 1
        for i in range(1, n):
            makeSet(i)
        #print(f[:n])
        line = stdin.readline().strip().split()
        while(line[0] != 'O'):
            #print(line)
            comm = line[0]
            x = int(line[1])
            if(comm == 'E'):
                print(findDist(x))
            else:
                y = int(line[2])
                unionSet(y, x)
                #print(f[1:n])
                #print(dist[1:n])
            line = stdin.readline().strip().split()
        
        T -= 1
    return 0

main()