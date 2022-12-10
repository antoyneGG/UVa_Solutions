'''
█ Problema 11646 - Athletics Track
'''

from sys import stdin
import math

eps = 1e-8

def perimeter(value, a, b):
    lenght = value
    width = (lenght/a)*b
    d = math.sqrt(lenght**2 + width**2)
    r = d/2
    O = math.acos((r**2 + r**2 - width**2)/(2*r*r))
    longA = r * O
    perim = longA*2 + lenght*2
    return perim

def main():
    cont = 1
    line = stdin.readline().split()
    while(line != []):
        a, b = float(line[0]), float(line[2])
        l = 0.0
        h = 400.0
        while( h - l > eps):
            mid = (l + h)/2
            per = perimeter(mid, a, b)
            if(per > 400):
                h = mid
            else:
                l = mid
        print(f'Case {cont}: {mid} {(mid/a)*b}')
        cont += 1
        line = stdin.readline().split()
    return 0

main()