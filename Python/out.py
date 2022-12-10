'''
Autor: Fabian Antoyne Garcia Gallego
Codigo: 8956118
Ejercicio B: 23 Out of 5
'''

from sys import stdin

found = False

def yield23(A, value, cont):
    global found
    ans = False
    #print(f'{value} - {A}')
    if(cont == 0):
        if(value == 23):
            found = True
            ans = True
    elif((value < 0 and value + sum(A) >= 23) or (value > 0 and value - sum(A) <= 23) or value == 0):
        i = 0
        while(i < 5 and not found):
            if(A[i] != 0 and not found):
                number = A[i]
                A[i] = 0
                j = 0
                while(j < 3 and not found):
                    if(j == 0 and not found):
                        ans = yield23(A, value + number, cont - 1)
                    elif(j == 1 and not found):
                        ans = yield23(A, value - number, cont - 1)
                    elif(j == 2 and not found):
                        ans = yield23(A, value * number, cont - 1)
                    j += 1
                A[i] = number
            i += 1
    return ans


def main():
    global found
    fiveTup = list(map(int, stdin.readline().split()))
    while(sum(fiveTup) > 0):
        found = False
        #print(fiveTup)
        
        i = 0
        while(i < 5 and not found):
            number = fiveTup[i]
            fiveTup[i] = 0
            yield23(fiveTup, number, 4)
            fiveTup[i] = number
            i += 1
        
        if(found):
            print("Possible")
        else:
            print("Impossible")
        
        fiveTup = list(map(int, stdin.readline().split()))
    return 0

main()