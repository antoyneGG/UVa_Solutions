'''
Autor: Fabian Antoyne Garcia Gallego
Codigo: 8956118
Ejercicio C: Tree Painting
'''

from sys import stdin

G = [[] for _ in range(10000)]
visited = [False for _ in range(10000)]
colored = [False for _ in range(10000)]
depth = [(-1, 0) for _ in range(10000)]
f = [-1 for _ in range(10000)]

def dfsColor(v, k):
    global G, visited, colored, f
    #print(f[v])
    visited[v] = True
    if(k == 0):
        colored[v] = True
    else:
        if(not colored[f[v]] and f[v] != -1):
            if(dfsColor(f[v], k - 1)):
                colored[v] = True
    if(colored[v]):
        ans = True
    else:
        ans = False
    return ans

def dfsAux(v):
    global G, visited, f, depth
    depth[v] = (v, depth[f[v]][1] + 1)
    visited[v] = True
    
    for u in G[v]:
        if(not visited[u]):
            f[u] = v
            dfsAux(u)

def dfs(N, k):
    global G, visited, colored, f, depth
    ans = 0
    for i in range(N):
        visited[i] = False
        colored[i] = False
        depth[i] = (-1, 0)
        f[i] = -1
    dfsAux(0)
    ordDepth = sorted(depth[:N], reverse=True, key=lambda x: x[1])
    #print(ordDepth)
    #print(f[:N])
    #print(k)
    for i in range(N):
        visited[i] = False
    for nodes in ordDepth:
        if(nodes[1] >= k and not colored[nodes[0]]):
            #print(nodes)
            if(dfsColor(nodes[0], k)):
                #print("por q")
                ans += 1
    return ans

    

def main():
    global G
    line = stdin.readline()
    while(line != ""):
        N, M, k = map(int, line.split())
        for i in range(N):
            G[i].clear()
        for i in range(M):
            lis = list(map(int, stdin.readline().split()))
            G[lis[0]] = lis[1:]
        #print(G[:N + 1])
        print(dfs(N, k))
        
        line = stdin.readline()
    
    return 0

main()