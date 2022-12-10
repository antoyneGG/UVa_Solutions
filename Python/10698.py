'''
Autor: Fabian Antoyne Garcia Gallego
Ejercicio numero 10698 de uVa: Football Sort
Resumen de la solucion aplicada: Para cada tabla de clasificacion se crea un diccionario, el cual tendra como 
llaves los nombres de los equipos, y cada llave correspondera a una lista con 7 posiciones, las cuales contendran
la siguiente informacion del respectivo equipo:
Pos 0: Posicion en la tabla
Pos 1: Puntos
Pos 2: Diferencia de goles
Pos 3: Goles a favor
Pos 4: Partidos jugados
Pos 5: Goles en contra
Pos 6: Porcentaje en cuanto a la puntuacion
Y con esta informacion se realiza el respectivo ordenamiento para la tabla de clasificacion final una vez se termino
de ingresar la informacion de los partidos, teniendo en cuenta el ordenamiento extra alfabetico para aquellos
equipos que empaten en las otras 3 condiciones (puntos, diferencia de goles, goles a favor).
'''

from sys import stdin

def main():
    nTeams, games = list(map(int, stdin.readline().split()))
    while(nTeams != 0 or games != 0):
        teams = {}
        sort_equals = False
        equals = False
        cont = 1
        lastKey = ''
        for i in range(nTeams):
            teams[stdin.readline().rstrip('\r\n')] = [0]*7
        for j in range(games):
            game = stdin.readline().split()
            teamL = game[0]
            teamR = game[4]
            goalsL = int(game[1])
            goalsR = int(game[3])
            if(teamL in teams.keys()):
                teams[teamL][1] += 3 if goalsL > goalsR else 1 if goalsL == goalsR else 0
                teams[teamL][4] += 1
                teams[teamL][3] += goalsL
                teams[teamL][5] += goalsR
                teams[teamL][2] = teams[teamL][3] - teams[teamL][5]
                teams[teamL][6] = float((teams[teamL][1] * 100)/(teams[teamL][4] * 3))

            if(teamR in teams.keys()):
                teams[teamR][1] += 3 if goalsR > goalsL else 1 if goalsL == goalsR else 0
                teams[teamR][4] += 1
                teams[teamR][3] += goalsR
                teams[teamR][5] += goalsL
                teams[teamR][2] = teams[teamR][3] - teams[teamR][5]
                teams[teamR][6] = float((teams[teamR][1] * 100)/(teams[teamR][4] * 3))

        sorted_teams = dict(sorted(teams.items(), key=lambda x: (x[1][1], x[1][2], x[1][3] ), reverse=True))

        for key in sorted_teams:
            if(cont == 1):
                sorted_teams[key][0] = 1
            elif(sorted_teams[key][1] == sorted_teams[lastKey][1] and sorted_teams[key][2] == sorted_teams[lastKey][2] and sorted_teams[key][3] == sorted_teams[lastKey][3]):
                sorted_teams[key][0] = sorted_teams[lastKey][0]
            else:
                sorted_teams[key][0] = cont
            cont += 1
            lastKey = key
        keyList = list(sorted_teams.keys())

        for x in range(len(keyList)):
            if(x != len(keyList) - 1):
                if(sorted_teams[keyList[x]][0] == sorted_teams[keyList[x + 1]][0] and not equals):
                    start = x
                    equals = True
                elif(sorted_teams[keyList[x]][0] != sorted_teams[keyList[x + 1]][0] and equals):
                    end = x + 1
                    equals = False
                    sort_equals = True
            elif(equals):
                end = x + 1
                equals = False
                sort_equals = True
            if(sort_equals):
                keyList[start:end] = sorted(keyList[start:end], key = str.lower)
                sort_equals = False

        for x in range(len(keyList)):
            print(f'{str(sorted_teams[keyList[x]][0])+"." if sorted_teams[keyList[x]][0] != sorted_teams[keyList[x - 1]][0] or x == 0 else "":>3}{keyList[x]:>16}{sorted_teams[keyList[x]][1]:>4}{sorted_teams[keyList[x]][4]:>4}{sorted_teams[keyList[x]][3]:>4}{sorted_teams[keyList[x]][5]:>4}{sorted_teams[keyList[x]][2]:>4}{"{:.2f}".format(sorted_teams[keyList[x]][6]) if sorted_teams[keyList[x]][4] != 0 else "N/A":>7}')
        nTeams, games = list(map(int, stdin.readline().split()))
        if(nTeams != 0 or games != 0):
            print()
    
    
main()