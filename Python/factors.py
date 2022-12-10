'''
Autor: Fabian Antoyne Garcia Gallego
Codigo: 8956118
Ejercicio B: Small Factors
'''

from sys import stdin

def binarySearch(M, m, low, hi):
    if(low + 1 == hi):
        if(M[low] >= m):
            return M[low]
        else:
            return M[low + 1]
    else:
        mid = low + ((hi - low)>>1)
        if(M[mid] == m):
            return M[mid]
        elif(M[mid] > m):
            return binarySearch(M, m, low, mid)
        else:
            return binarySearch(M, m, mid, hi)

def generate():
    M = []
    for i in range(32):
        for j in range(32):
            a = 2**i * 3**j
            if(a <= 2**31):
                M.append(a)
    return M

def main():
    M = generate()
    M.sort()
    #print(M)
    m = int(stdin.readline())
    while(m != 0):
        print(binarySearch(M, m, 0, len(M)))
        m = int(stdin.readline())
    return 0

main()