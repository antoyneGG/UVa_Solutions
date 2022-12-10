'''
Autor: Fabian Antoyne Garcia Gallego
Codigo: 8956118
Frase de compromiso: "Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
a seguir los más altos estándares de integridad académica." 
'''

from sys import stdin
from collections import deque
from copy import copy, deepcopy

m = 17
n = 4
wallsBoard = []
holes = [[-1, -1] for _ in range(17)]
changeX = [1, 0, -1, 0]
changeY = [0, 1, 0, -1]

'''
Clase Marble: Cada canica del juego ira guardando su posicion en fila y columna.
'''
class Marble:
    def __init__(self, row, column):
        self.row = row
        self.column = column

'''
Clase Move: Esta clase ira guardado el estado del juego, guardando las canicas con sus posiciones, guardando la cantidad
de canicas que han llegado a su destino, guardando el tablero de las canicas y guardando el tablero de los agujeros de
las canicas.
'''
class Move:
    def __init__(self, completed, marbles, marblesBoard, holesBoard):
        self.marbles = marbles
        self.completed = completed
        self.marblesBoard = marblesBoard
        self.holesBoard = holesBoard
        self.moves = 0
        self.contInvalid = 0
        self.illegal = False
        self.onHold = deque()

    '''
    Entrada: Numero que indica direccion hacia la que se deben mover las canicas segun los arreglos de Cambio (change)
    Salida: Ninguna
    Descripcion: Esta funcion se encarga de mover todas las canicas segun el movimiento indicado, claramente siempre y
    cuando la canica que vaya a mover se encuentre dentro del tablero, es decir, no haya llegado a su destino. Para 
    realizar el movimiento, debido a que el movimiento es continuo hasta que llegue a un limite, va a ir verificando
    que no se vaya a salir del tablero, que no vaya a saltarse un agujero, que no vaya a saltarse otra canica y que no 
    vaya a pasar una pared. Si no pudo moverse por una canica que esta adelante la canica que estaba intentando moverse
    se iria a una cola de espera
    '''
    def moveMarbles(self, j):
        global m, n, wallsBoard
        self.contInvalid = 0
        i = 1
        while( i < m + 1 and not self.illegal):
            if(self.marbles[i].row != -1 and self.marbles[i].column != -1):
                nextPlace = copy(self.marbles[i])
                nextPlace.row += changeY[j]
                nextPlace.column += changeX[j]
                while(nextPlace.row != -1 
                and nextPlace.column != -1 
                and nextPlace.row < n 
                and nextPlace.column < n 
                and self.holesBoard[nextPlace.row][nextPlace.column] != 1 
                and not ([self.marbles[i].row, self.marbles[i].column, nextPlace.row, nextPlace.column] in wallsBoard)
                and not ([nextPlace.row, nextPlace.column, self.marbles[i].row, self.marbles[i].column] in wallsBoard)
                and self.marblesBoard[nextPlace.row][nextPlace.column] == 0):
                    self.marblesBoard[self.marbles[i].row][self.marbles[i].column] = 0
                    self.marbles[i].row = nextPlace.row
                    self.marbles[i].column = nextPlace.column
                    self.marblesBoard[self.marbles[i].row][self.marbles[i].column] = i
                    nextPlace.row += changeY[j]
                    nextPlace.column += changeX[j]
                if(nextPlace.row != -1 
                and nextPlace.column != -1 
                and nextPlace.row < n 
                and nextPlace.column < n 
                and not ([self.marbles[i].row, self.marbles[i].column, nextPlace.row, nextPlace.column] in wallsBoard)
                and not ([nextPlace.row, nextPlace.column, self.marbles[i].row, self.marbles[i].column] in wallsBoard)):
                    if(self.holesBoard[nextPlace.row][nextPlace.column] == 1 and holes[i][0] == nextPlace.row and holes[i][1] == nextPlace.column):
                        self.marblesBoard[self.marbles[i].row][self.marbles[i].column] = 0
                        self.marbles[i].row = nextPlace.row
                        self.marbles[i].column = nextPlace.column
                        self.marblesBoard[self.marbles[i].row][self.marbles[i].column] = 0
                        self.holesBoard[self.marbles[i].row][self.marbles[i].column] = 0
                        self.marbles[i].row = -1
                        self.marbles[i].column = -1
                        self.completed += 1
                    elif(self.holesBoard[nextPlace.row][nextPlace.column] == 1):
                        self.illegal = True
                    if(self.marblesBoard[nextPlace.row][nextPlace.column] > 0):
                        self.onHold.append(i)
            else:
                self.contInvalid += 1
            i += 1
    
    def moveOnHold(self, j):
        counter = [False for _ in range(m + 1)]
        while(len(self.onHold) > 0 and not self.illegal):
            i = self.onHold.popleft()
            if(self.marbles[i].row != -1 and self.marbles[i].column != -1):
                nextPlace = copy(self.marbles[i])
                nextPlace.row += changeY[j]
                nextPlace.column += changeX[j]
                while(nextPlace.row != -1 
                and nextPlace.column != -1 
                and nextPlace.row < n 
                and nextPlace.column < n 
                and self.holesBoard[nextPlace.row][nextPlace.column] != 1 
                and not ([self.marbles[i].row, self.marbles[i].column, nextPlace.row, nextPlace.column] in wallsBoard)
                and not ([nextPlace.row, nextPlace.column, self.marbles[i].row, self.marbles[i].column] in wallsBoard)
                and self.marblesBoard[nextPlace.row][nextPlace.column] == 0):
                    self.marblesBoard[self.marbles[i].row][self.marbles[i].column] = 0
                    self.marbles[i].row = nextPlace.row
                    self.marbles[i].column = nextPlace.column
                    self.marblesBoard[self.marbles[i].row][self.marbles[i].column] = i
                    nextPlace.row += changeY[j]
                    nextPlace.column += changeX[j]
                if(nextPlace.row != -1 
                and nextPlace.column != -1 
                and nextPlace.row < n 
                and nextPlace.column < n 
                and not ([self.marbles[i].row, self.marbles[i].column, nextPlace.row, nextPlace.column] in wallsBoard)
                and not ([nextPlace.row, nextPlace.column, self.marbles[i].row, self.marbles[i].column] in wallsBoard)):
                    if(self.holesBoard[nextPlace.row][nextPlace.column] == 1 and holes[i][0] == nextPlace.row and holes[i][1] == nextPlace.column):
                        self.marblesBoard[self.marbles[i].row][self.marbles[i].column] = 0
                        self.marbles[i].row = nextPlace.row
                        self.marbles[i].column = nextPlace.column
                        self.marblesBoard[self.marbles[i].row][self.marbles[i].column] = 0
                        self.holesBoard[self.marbles[i].row][self.marbles[i].column] = 0
                        self.marbles[i].row = -1
                        self.marbles[i].column = -1
                        self.completed += 1
                    elif(self.holesBoard[nextPlace.row][nextPlace.column] == 1):
                        self.illegal = True
                    if(self.marblesBoard[nextPlace.row][nextPlace.column] > 0 and counter[i] == 0):
                        counter[i] += 1
                        self.onHold.append(i)
    
    def checkInvalids(self):
        if(self.contInvalid == m):
            self.illegal = True

def bfs(initial):
    global wallsBoard, m
    queue = deque()
    queue.append(initial)
    comparator = []
    impossible = float('inf')
    comparator.append(initial.marblesBoard)
    while(len(queue) > 0):
        initial = queue.popleft()
        for j in range(4):
            mov = deepcopy(initial)
            mov.onHold = deque()
            mov.illegal = False
            mov.moveMarbles(j)
            mov.moveOnHold(j)
            mov.checkInvalids()
            if(not mov.illegal):
                mov = Move(mov.completed, mov.marbles, mov.marblesBoard, mov.holesBoard)
                if(mov.marblesBoard not in comparator):
                    mov.moves = initial.moves + 1
                    queue.append(mov)
                    comparator.append(mov.marblesBoard)
                if(mov.completed == m):
                    return mov.moves
    
    return impossible
                   
                    


def main():
    global m, n, wallsBoard
    cont = 1
    line = list(map(int, stdin.readline().split()))
    n, m, w = line[0], line[1], line[2]
    while( n != 0 or m != 0 or w != 0 ):
        marblesBoard = [[0 for _ in range(n)] for _ in range(n)]
        holesBoard = [[0 for _ in range(n)] for _ in range(n)]
        wallsBoard = []
        marbles = [Marble(-1, -1) for _ in range(m + 1)]
        mov = Move(0, marbles, marblesBoard, holesBoard)
        for i in range(m):
            line = list(map(int, stdin.readline().split()))
            mov.marblesBoard[line[0]][line[1]] = i + 1
            mov.marbles[i + 1].row = line[0]
            mov.marbles[i + 1].column = line[1]
        for i in range(m):
            line = list(map(int, stdin.readline().split()))
            mov.holesBoard[line[0]][line[1]] = 1
            holes[i + 1][0] = line[0]
            holes[i + 1][1] = line[1]
        for i in range(w):
            line = list(map(int, stdin.readline().split()))
            wallsBoard.append(line)
        
        result = bfs(mov)

        if(result != float('inf')):
            print("Case " + str(cont) + ": " + str(result) + " moves")
        else:
            print("Case " + str(cont) + ": impossible")
        print()

        cont += 1

        line = list(map(int, stdin.readline().split()))
        n, m, w = line[0], line[1], line[2]

main()
