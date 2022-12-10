'''
Autor: Fabian Antoyne Garcia Gallego
Codigo: 8956118
Ejercicio B: The Bus Driver Problem
'''

from sys import stdin

def solve(m, a, n, d, r):
    m.sort()
    a.sort(reverse=True)
    ans = 0
    for i in range(n):
        charge = 0
        charge += ((m[i] + a[i]) - d) * r
        if(charge >= 0):
            ans += charge
        #print(ans)
    return ans

def main():
    n, d, r = map(int, stdin.readline().split())
    while(n != 0 and d != 0 and r != 0):
        morning = list(map(int, stdin.readline().split()))
        afternoon = list(map(int, stdin.readline().split()))
        #print(morning)
        #print(afternoon)
        
        print(solve(morning, afternoon, n, d, r))
        
        n, d, r = map(int, stdin.readline().split())
    return 0

main()