'''
╪Problema 11995 - I Can Guess the Data Structure!
'''

from sys import stdin
from collections import deque
from heapq import heappop, heappush

def main():
    n = int(stdin.readline())
    while(n != ""):
        n = int(n)
        lifo = True
        fifo = True
        prioQ = True
        error = False
        stack = deque()
        queue = deque()
        priorityQ = []
        for i in range(n):
            y, x = map(int, stdin.readline().split())
            if(y == 1):
                stack.append(x)
                queue.append(x)
                priorityQ.append(x)
            elif(x in stack and x in queue and x in priorityQ):
                if(y == 2 and not error):
                    if(prioQ and x != max(priorityQ)):
                        prioQ = False
                    if(lifo and x != stack[-1]):
                        lifo = False
                    if(fifo and x != queue[0]):
                        fifo = False
                    if(fifo and lifo):
                        stack.pop()
                        queue.popleft()
                    elif(fifo):
                        queue.popleft()
                    elif(lifo):
                        stack.pop()
                    priorityQ.remove(x)
            else:
                error = True

        if((not lifo and not fifo and not prioQ) or error):
            print("impossible")
        elif((lifo and fifo and prioQ) or (lifo and fifo) or (lifo and prioQ) or (fifo and prioQ)):
            print("not sure")
        elif(lifo):
            print("stack")
        elif(fifo):
            print("queue")
        elif(prioQ):
            print("priority queue")

        n = stdin.readline()

    return 0

main()