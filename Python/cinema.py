from sys import stdin

def inInterval(x, a, b):
    if(int(x[1:]) > int(a[1:]) and int(x[1:]) < int(b[1:]) and x[0] == a[0]):
        ans = True
    else:
        ans = False
    return ans

def solve(ocup, group, p, z):
    intervals = []
    last = ('_', None)
    for seat in ocup:
        if(seat[1] == '+'):
            last = seat
        else:
            if(seat[0][0] == last[0][0]):
                if(int(seat[0][1:]) - int(last[0][1:]) - 2 >= 0):
                    intervals.append([last[0], seat[0], int(seat[0][1:]) - int(last[0][1:]) - 2])
    #print(ocup)
    #print(group)
    #print(intervals)
    s = 0
    i = 0
    problem = False
    while(s < z and i < len(intervals) and not problem):
        while(s < z and i < len(intervals) and intervals[i][1][0] != group[s][0]):
            if(intervals[i][1][0] < group[s][0]):
                i += 1
            elif(intervals[i][1][0] > group[s][0]):
                s += 1
        while(i < len(intervals) and s < z and int(intervals[i][1][1:]) < int(group[s][1:]) and intervals[i][1][0] == group[s][0]):
            i += 1
        if(i < len(intervals) and s < z and inInterval(group[s], intervals[i][0], intervals[i][1])):
            #print(f'seat {group[s]} in interval {intervals[i]}')
            if(intervals[i][2] > 0):
                intervals[i][2] -= 1
                #print(intervals[i])
            elif(intervals[i][2] == 0):
                problem = True
        s += 1
    #print(group[s])
    #print(f'{i} {len(intervals)}')
    #print(f'{intervals[i]}')
    if(problem):
        ans = False
    else:
        ans = True
    return ans

def main():
    R, C = map(int, stdin.readline().split())
    while(R != 0 and C != 0):
        P = int(stdin.readline())
        ocup = []
        for i in range(P):
            pos, dir = map(str, stdin.readline().split())
            ocup.append((pos, dir))
        Z = int(stdin.readline())
        group = []
        for i in range(Z):
            pos = stdin.readline().strip()
            group.append(pos)
        ocup.sort(key=lambda seat: (seat[0][0], int(seat[0][1:])))
        group.sort(key=lambda seat: (seat[0], int(seat[1:])))
        #print(f'{R} {C}')
        if(solve(ocup, group, P, Z)):
            print("YES")
        else:
            print("NO")

        R, C = map(int, stdin.readline().split())
    return 0

main()