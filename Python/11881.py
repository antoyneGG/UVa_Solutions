'''
█ Problema 11881 - Internal Rate of Return
'''

from sys import stdin

eps = 1e-6

def irr(IRR, values, T):
    ans = 0
    for i in range(T+1):
        ans += (values[i]/((1+IRR)**i))
    return ans

def main():
    T = int(stdin.readline())
    while(T):
        found = False
        cf = [float(x) for x in stdin.readline().strip().split()]
        l = -1
        h = 0
        for i in range(T+1):
            h = max(h, cf[i])
        #print(f'({l} - {h})')
        while(h - l > eps):
            mid = (l + h)/2
            npv = irr(mid, cf, T)
            if(npv > 0):
                l = mid
            else:
                h = mid
            #print(f'({l} - {h})')
        print("%.2lf"%(mid))
        T = int(stdin.readline())
    return 0

main()