A = [[None, 1, None], [0, 2, 5], [1, None, 3], [1, 4, None], [3, None, None], [0, 6, 12], [5, None, 7], [5, None, 8], [5, 9, 11], [8, None, 10], [8, None, None], [5, None, None], [0, 13, None], [12, None, None]]
values = [5, 3, 7, 2, 4, 1, 3, 8, 5, 11, 14, 16, 4, 2]
names = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]
for i in range(len(A)):
    print(f'Node {i}:\nParent: {A[i][0]}\nChild: {A[i][1]}\nSibling: {A[i][2]}\n')

ind = []

def phi(A, v, last, mem):
    if((v, last) in mem.keys()):
        ans, indList = mem[(v, last)]
    elif(v == None):
        ans, indList = 0, []
    elif(last != A[v][0]):
        temp1, list1 = phi(A, A[v][1], v, mem)
        temp2, list2 = phi(A, A[v][2], v, mem)
        a = values[v] + temp1 + temp2
        temp3, list3 = phi(A, A[v][1], last, mem)
        temp4, list4 = phi(A, A[v][2], last, mem)
        b = temp3 + temp4
        ans = max(a, b)
        if(ans == a):
            indList = list1 + list2 + [v]
        else:
            indList = list3 + list4
    else:
        print("ola")
        temp1, list1 = phi(A, A[v][1], last, mem)
        temp2, list2 = phi(A, A[v][2], last, mem)
        ans = temp1 + temp2
        indList = list1 + list2
    mem[(v, last)] = ans, indList
    return ans, indList

mem = {}
result, listaF = phi(A, 0, -1, mem)
print(result)
print(listaF)

suma = 0
for i in listaF:
    suma += values[i]
print(suma)

owo = (4, 5)
ewe = (1, 1)
print(owo + ewe)