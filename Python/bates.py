'''
Autor: Fabian Antoyne Garcia Gallego
Codigo: 8956118
Ejercicio A: Helping Fill Bates
'''

from sys import stdin

def binarySearch(A, low, hi, x):
    if(low + 1 == hi):
        #print(f'low {low}')
        if(A[low] > x):
            return A[low]
        else:
            if(hi != len(A)):
                return A[hi]
            else:
                return -1
    else:
        mid = low + ((hi - low)>>1)
        if(A[mid] <= x):
            return binarySearch(A, mid, hi, x)
        else:
            return binarySearch(A, low, mid, x)

def main():
    S = stdin.readline().strip()
    alphabet = {
                'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [], 'h': [], 'i': [], 'j': [],
                'k': [], 'l': [], 'm': [], 'n': [], 'o': [], 'p': [], 'q': [], 'r': [], 's': [], 't': [],
                'u': [], 'v': [], 'w': [], 'x': [], 'y': [], 'z': [], 'A': [], 'B': [], 'C': [], 'D': [],
                'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [],
                'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [],
                'Y': [], 'Z': []
            }
    for i in range(len(S)):
        alphabet[S[i]].append(i)
    #print(S)
    #print(alphabet)
    T = int(stdin.readline())
    for i in range(T):
        X = stdin.readline().strip()
        prev = -1
        j = 0
        match = True
        first = -1
        last = -1
        while(j < len(X) and match):
            if(X[j] in S):
                prev = binarySearch(alphabet[X[j]], 0, len(alphabet[X[j]]), prev)
                #print(alphabet[X[j]])
                #print(prev)
                if(j == 0):
                    first = prev
                if(j == len(X) - 1):
                    last = prev
            else:
                prev = -1
            if(prev == -1):
                match = False
            j += 1
        if(match):
            print(f'Matched {first} {last}')
        else:
            print("Not matched")
    return 0

main()