'''
Autor: Fabian Antoyne Garcia Gallego
Codigo: 8956118
Ejercicio D: Wedding Shopping
'''

from sys import stdin

def phiMem(A, n, m, mem):
    ans = float('-inf')
    if((n, m) in mem.keys()):
        ans = mem[(n, m)]
    elif(n == 0):
        best = float('-inf')
        for i in range(len(A[n])):
            if(m - A[n][i] >= 0 and A[n][i] > best):
                best = A[n][i]
        ans = best
        mem[(n, m)] = ans
    else:
        for i in range(len(A[n])):
            if(m - A[n][i] > 0):
                ans = max(A[n][i] + phiMem(A, n - 1, m - A[n][i], mem), ans)
        mem[(n, m)] = ans
    return ans

def main():
    N = int(stdin.readline())
    while(N != 0):
        line1 = list(map(int, stdin.readline().split()))
        M, C = line1[0], line1[1]
        A = []
        for i in range(C):
            line2 = list(map(int, stdin.readline().split()))
            A.append(line2[1:])
        #print(A)
        mem = {}
        ans = phiMem(A, C - 1, M, mem)
        if(ans > 0):
            print(ans)
        else:
            print("no solution")
        
        N -= 1
    return 0

main()