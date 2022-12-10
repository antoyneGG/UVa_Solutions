'''
Autor: Fabian Antoyne Garcia Gallego
Codigo: 8956118
Ejercicio D: Untangle them All!
'''


from sys import stdin

def findInd(a, low, hi, x):
    while(low + 1 != hi):
        mid = low + ((hi - low) >> 1)
        if(a[mid] > x):
            hi = mid
        else:
            low = mid
    return hi

def lis(a):
    ans = [a[0][1]]
    for i in range(1, len(a)):
        if(ans[-1] <= a[i][1]):
            ans.append(a[i][1])
        else:
            ans[findInd(ans, -1, len(ans) - 1, a[i][1])] = a[i][1]
    return len(ans)

def sol(A):
    A.sort()
    x = lis(A)
    A.sort(reverse = True)
    y = lis(A)
    return (x, y)

def main():
    N = int(stdin.readline())
    while(N != 0):
        top = list(map(int, stdin.readline().split()))
        bot = list(map(int, stdin.readline().split()))
        A = []
        for i in range(N):
            A.append((top[i], bot[i]))
        ans = sol(A)
        print(f'{ans[0]} {ans[1]}')
        
        
        N = int(stdin.readline())
    
    return 0

main()