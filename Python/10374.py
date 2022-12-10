'''
Autor: Fabian Antoyne Garcia Gallego
Ejercicio numero 10374 de uVa: Election
Resumen de la solucion aplicada: Se genera un diccionario para cada caso. Cada diccionario va a tener como llaves
los nombres de los candidatos, y estas llaves van a tener almacenadas una lista, la cual va a contener el nombre
del partido y la cantidad de votos del candidato. Entonces finalmente recorriendo y analizando este diccionario
se puede encontrar al ganador, en caso de que lo haya, y se podria mostrar su respectivo partido.
'''

from sys import stdin

def main():
    T = int(stdin.readline())
    for i in range(T):
        tie = False
        winner = ''
        election = {}
        space = stdin.readline()
        n = int(stdin.readline())
        for j in range(n * 2):
            if(j % 2 == 0):
                name = str(stdin.readline().rstrip('\n\r'))
            else:
                election[name] = []
                election[name].append(str(stdin.readline().rstrip('\n\r')))
                election[name].append(0)
        m = int(stdin.readline())
        for j in range(m):
            name = str(stdin.readline().rstrip('\n\r'))
            if(name in election.keys()):
                election[name][1] += 1
        votes = 0
        for key in election.keys():
            if(election[key][1] > votes):
                votes = election[key][1]
                winner = election[key][0]
                tie = False
            elif(election[key][1] == votes):
                tie = True
        if(tie):
            print("tie")
        else:
            print(winner)
        if(i != T - 1):
            print()

main()