'''
Autor: Fabian Antoyne Garcia Gallego
Codigo: 8956118
Ejercicio C: All Walks of length n from the first node
'''

from sys import stdin

adj = []
visited = []
walks = []

def walk(v, n, N, path, dis):
    global adj, walks, visited
    if(dis == n):
        walks.append(path)
    else:
        for i in range(N):
            if(adj[v][i] == 1 and visited[i] == 0):
                visited[v] = 1
                newPath = list(path)
                newPath.append(i + 1)
                walk(i, n, N, newPath, dis + 1)
                visited[v] = 0
    

def main():
    global adj, visited, walks
    line = "-9999"
    while(line == "-9999"):
        v, n = map(int, stdin.readline().split())
        adj.clear()
        visited.clear()
        walks.clear()
        for i in range(v):
            adj.append(list(map(int, stdin.readline().split())))
            visited.append(0)
        
        walk(0, n, v, [1], 0)
        
        if(len(walks) > 0):
            for w in walks:
                print('(' + ','.join(list(map(str, w))) + ')')
        else:
            print(f'no walk of length {n}')
        
        '''
        for i in adj:
            print(i)
        '''
        
        line = stdin.readline().strip()
        if(line == "-9999"):
            print()
            
    return 0

main()