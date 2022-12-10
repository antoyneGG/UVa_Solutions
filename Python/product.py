'''
Autor: Fabian Antoyne Garcia Gallego
Codigo: 8956118
Ejercicio B: Maximum Sub-sequence Product
'''

from sys import stdin

def solve(A, N):
    ans = 0
    if(N != 0):
        tabB = [None for _ in range(N)]
        tabW = [None for _ in range(N)]
        tabB[0] = A[0]
        tabW[0] = A[0]
        ans = A[0]
        for i in range(1, N):
            tabB[i] = max(A[i], tabB[i - 1] * A[i], tabW[i - 1] * A[i])
            tabW[i] = min(A[i], tabB[i - 1] * A[i], tabW[i - 1] * A[i])
        #print(tabB)
        #print(tabW)
        for i in range(N):
            ans = max(tabB[i], tabW[i], ans)
    return ans
    
def main():
    A = []
    for line in stdin:
        for integer in line.split():
            #print(integer)
            if(int(integer) == -999999):
                print(solve(A, len(A)))
                A = []
            else:
                A.append(int(integer))
            
    return 0

main()