'''
Autor: Fabian Antoyne Garcia Gallego
Codigo: 8956118
Ejercicio A: Boggle Blitz
'''

from sys import stdin

legals = set()

def nextPos(r, c, N):
    if(c == N):
        ans = (r + 1, 0)
    else:
        ans = (r, c + 1)
    return ans

def isValid(word, char):
    #print(f'{word} vs {char}')
    if(word[-1] < char):
        ans = True
    else:
        ans = False
    return ans

def blitz(A, N, r, c, cont, word):
    global legals
    #print(word)
    if(cont >= 3 and cont <= N*N):
        legals.add(word)
    for i in range(r - 1, r + 2):
        for j in range(c - 1, c + 2):
            if((i, j) != (r, c) and i >= 0 and j >= 0 and i < N and j < N):
                if(isValid(word, A[i][j])):
                    blitz(A, N, i, j, cont + 1, word + A[i][j])
    return 0
    

def main():
    global legals
    T = int(stdin.readline())
    while(T > 0):
        blank = stdin.readline()
        N = int(stdin.readline())
        boggle = []
        legals = set()
        for i in range(N):
            boggle.append(stdin.readline().strip())
        for i in range(N):
            for j in range(N): 
                blitz(boggle, N, i, j, 1, boggle[i][j])
        
        legals = list(legals)
        legals.sort(key=lambda x: (len(x), x))
        for w in legals:
            print(w)
        
        if(T != 1):
            print()
        
        T -= 1
    return 0

main()