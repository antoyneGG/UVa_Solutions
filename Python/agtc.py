'''
Autor: Fabian Antoyne Garcia Gallego
Codigo: 8956118
Ejercicio A: AGTC
'''


from sys import stdin

def phi(x, y, n, m, mem):
    if((n, m) in mem.keys()):
        ans = mem[(n, m)]
    elif(n == 0):
        ans = m
    elif(m == 0):
        ans = n
    else:
        if(x[n - 1] == y[m - 1]):
            ans = phi(x, y, n - 1, m - 1, mem)
        else:
            ans = 1 + min(phi(x, y, n - 1, m - 1, mem), phi(x, y, n - 1, m, mem), phi(x, y, n, m - 1, mem))
        mem[(n, m)] = ans
    return ans

def main():
    line1 = stdin.readline().split()
    line2 = stdin.readline().split()
    while(line2 != []):
        N = int(line1[0])
        M = int(line2[0])
        x = list(line1[1])
        y = list(line2[1])
        #print(f'Tamanio {N}: {x}')
        #print(f'Tamanio {M}: {y}')
        mem = {}
        print(phi(x, y, N, M, mem))
        
        line1 = stdin.readline().split()
        line2 = stdin.readline().split()
    return 0

main()