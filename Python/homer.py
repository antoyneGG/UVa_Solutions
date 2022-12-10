'''
Autor: Fabian Antoyne Garcia Gallego
Codigo: 8956118
Ejercicio A: Homer Simpson
'''

from sys import stdin, setrecursionlimit
setrecursionlimit(10000)

def newMax(tup1, tup2):
    if(tup1[1] < tup2[1]):
        return tup1
    elif(tup1[1] > tup2[1]):
        return tup2
    else:
        if(tup1[0] >= tup2[0]):
            return tup1
        else:
            return tup2

def phiHomer(m, n, t, mem):
    if(t in mem.keys()):
        ans = mem[t]
        return ans
    if(t < n and t < m):
        mem[t] = (0, t)
        return (0, t)
    else:
        if(t >= n and t >= m):
            ans = tuple([sum(x) for x in zip((1, 0), newMax(phiHomer(m, n, t - n, mem), phiHomer(m, n, t - m, mem)))])
        elif(t >= n):
            ans = tuple([sum(x) for x in zip((1, 0), phiHomer(m, n, t - n, mem))])
        else:
            ans = tuple([sum(x) for x in zip((1, 0), phiHomer(m, n, t - m, mem))])
        mem[t] = ans
        return ans

def main():
    line = stdin.readline()
    while(line != ""):
        line = list(map(int, line.split()))
        m, n, t = line[0], line[1], line[2]
        mem = {}
        ans = phiHomer(m, n, t, mem)
        if(ans[1] == 0):
            print(f'{ans[0]}')
        else:
            print(f'{ans[0]} {ans[1]}')
        
        line = stdin.readline()
    return 0

'''
tup1 = (17, -2)
tup2 = (18, -1)
print(newMax(tup1, tup2))
print(tuple([sum(x) for x in zip(tup1, tup2)]))
'''

main()