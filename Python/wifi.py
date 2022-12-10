'''
Autor: Fabian Antoyne Garcia Gallego
Codigo: 8956118
Ejercicio D: WiFi
'''

from sys import stdin
from math import floor

def check(value, houses, points, h):
    #print(f'value: {value}')
    point = 0.0
    j = 1
    i = 0
    while(j <= points and i < h):
        point = houses[i] + value
        i += 1
        while(i < h and houses[i] <= point):
            i += 1
        j += 1
    if(i == h):
        return True
    else:
        return False

'''
def solve(houses, low, hi, m, n):
    if(low + 1 == hi):
        return floor(10 * (hi/2)) / 10
    else:
        mid = (hi + low)/2
        if(check(mid, houses, n, m)):
            return solve(houses, low, mid, m, n)
        else:
            return solve(houses, mid, hi, n, m)
'''

def main():
    T = int(stdin.readline())
    for i in range(T):
        line = list(map(int, stdin.readline().split()))
        n = line[0]
        m = line[1]
        houses = []
        for j in range(m):
            houses.append(int(stdin.readline()))
        houses.sort()
        #print(houses)
        if(n >= m):
            result = 0.0
        else:
            if(n == 0):
                n = 1
            low = 0.0
            hi = houses[-1]
            while(low + 1 != hi):
                #print(f'{int(hi)} y {int(low)}')
                mid = (int(hi) + int(low))//2
                if(check(float(mid), houses, n, m)):
                    hi = mid
                else:
                    low = mid
            #print(f'{hi}')
            result = hi/2
            #result = floor(10 * result)/10
            #print(f'{result}')
        print(f'{result:.1f}')

main()