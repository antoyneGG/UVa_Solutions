'''
Autor: Fabian Antoyne Garcia Gallego
Codigo: 8956118
Ejercicio A: Angry Birds
'''

from sys import stdin

def select(c1, c2):
    #print(f'c1: {c1} - c2: {c2}')
    if(c1[1] + c2[2] < c2[1] + c1[3]):
        ans = c1
        ans[1] += c2[2]
        ans[2] += c2[2]
        ans[3] += c2[3]
    elif(c1[1] + c2[2] > c2[1] + c1[3]):
        ans = c2
        ans[1] += c1[3]
        ans[2] += c1[2]
        ans[3] += c1[3]
    else:
        if(c1[0] < c2[0]):
            ans = c1
            ans[1] += c2[2]
            ans[2] += c2[2]
            ans[3] += c2[3]
        else:
            ans = c2
            ans[1] += c1[3]
            ans[2] += c1[2]
            ans[3] += c1[3]
    return ans
    

def bids(M, low, hi):
    if(low + 1 == hi):
        ans = [M[low][0], 0, 0, 0]
        if(M[low][1] == "P"):
            ans[2] += 1
        else:
            ans[3] += 1
    else:
        mid = low + ((hi - low)>>1)
        c1 = bids(M, low, mid)
        c2 = bids(M, mid, hi)
        ans = select(c1, c2)
        #print(ans)
    return ans

def merge(P, C, n, m):
    r, l = 0, 0
    M = [0 for _ in range(n + m)]
    for i in range(n + m):
        if(l == m):
            M[i] = (P[r], "P")
            r += 1
        elif(r == n):
            M[i] = (C[l], "C")
            l += 1
        else:
            if(P[r] <= C[l]):
                M[i] = (P[r], "P")
                r += 1
            else:
                M[i] = (C[l], "C")
                l += 1
    return M  

def main():
    T = int(stdin.readline())
    while(T != 0):
        line = list(map(int, stdin.readline().split()))
        np, nc = line[0], line[1]
        P = list(map(int, stdin.readline().split()))
        C = list(map(int, stdin.readline().split()))
        P.sort()
        C.sort()
        #print(f'{np}: {P}')
        #print(f'{nc}: {C}')
        M = merge(P, C, np, nc)
        #print(M)
        if(np > 0 and nc > 0):
            ans = bids(M, 0, np + nc)
            if(ans[0] == M[0][0] and ans[0] == C[0] and ans[0] != P[0]):
                ans[0] = 0
        elif(np > 0):
            ans = [P[-1], 0, 0, 0]
        elif(nc > 0):
            ans = [C[0], 0, 0, 0]
            if(ans[0] == M[0][0] and ans[0] == C[0]):
                ans[0] = 0
        else:
            ans = [0, 0, 0, 0]
        print(f'{ans[0]} {ans[1]}')
        T -= 1
    return 0
    
main()