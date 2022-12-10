'''
Autor: Fabian Antoyne Garcia Gallego
Codigo: 8956118
Ejercicio B: The Monkey and the Oiled Bamboo
'''

from sys import stdin

def binarySearch(M, k, n):
    if(k < M[0]):
        tempk = 1
    else:
        tempk = 0
    for i in range(n):
        if(i != n - 1):
            if(M[i + 1] - M[i] > k):
                if((M[i + 1] - M[i]) <= k + tempk):
                    tempk = k + tempk + 1
                else:
                    tempk = (M[i + 1] - M[i])
                return tempk
            elif(M[i + 1] - M[i] == k):
                k -= 1
                tempk += 1
    return k + tempk

def monkey(M, init, n):
    k = init
    found = False
    while(not found):
        #print(k)
        sumK = binarySearch(M, k, n)
        if(k == sumK):
            found = True
        else:
            k = sumK
    return k

def main():
    T = int(stdin.readline())
    i = 0
    while(i < T):
        n = int(stdin.readline())
        rungs = list(map(int, stdin.readline().split()))
        if(n > 1):
            if(rungs[0] >= rungs[1] - rungs[0]):
                init = rungs[0] - 1
            else:
                init = rungs[1] - rungs[0]
            print(f'Case {i + 1}: {monkey(rungs, init, n)}')
        else:
            print(f'Case {i + 1}: {rungs[0]}')
        #print(rungs)
        i += 1
    return 0

main()