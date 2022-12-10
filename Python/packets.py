from sys import stdin
from heapq import heapify, heappop, heappush

sizes = [1, 4, 9, 16, 25, 36]
ocup = [1, 4, 9, 36, 36, 36]


def pack(l):
    ans = 0
    for i in range(5, -1, -1):
        #print(i)
        if(i == 5):
            t = 0
            ans += l[i]
            l[i] = 0
        elif(i == 4):
            ans += l[i]
            l[0] -= 11 * l[i]
            l[i] = 0
        elif(i == 3):
            t = 0
            ans += l[i]
            if(l[i] >= l[1] // 5):
                l[i] -= l[1] // 5
                l[1] = l[1] % 5
            else:
                l[1] -= l[i] * 5
                l[i] = 0
            if(l[i] > 0):
                t += 20 * l[i]
                l[i] = 0
                t -= l[1] * 4
                l[1] = 0
                l[0] -= t 
        elif(i == 2):
            t = 0
            if(l[i] >= 4):
                ans += l[i] // 4
                l[i] = l[i] % 4
            if(l[i] > 0):
                if(l[i] == 3):
                    if(l[1] >= 1):
                        l[1] -= 1
                        t = 5
                    else:
                        t = 9
                elif(l[i] == 2):
                    if(l[1] >= 3):
                        l[1] -= 3
                        t = 6
                    else:
                        t = 18 - l[1] * 4
                        l[1] = 0
                else:
                    if(l[1] >= 5):
                        l[1] -= 5
                        t = 7
                    else:
                        t = 27 - l[1] * 4
                        l[1] = 0
                ans += 1
                l[i] = 0
                l[0] -= t
        elif(i == 1):
            t = 0
            if(l[i] >= 9):
                ans += l[i] // 9
                l[i] = l[i] % 9
            if(l[i] > 0):
                t = 36
                t -= l[i] * 4
                ans += 1
                l[0] -= t
        elif(i == 0):
            if(l[i] >= 36):
                ans += l[i] // 36
                l[i] = l[i] % 36
            if(l[i] > 0):
                ans += 1
        #print(ans)
                    
    #print(l)
    return ans

def main():
    packets = list(map(int, stdin.readline().split()))
    while(sum(packets) > 0):
        #print(packets)
        #l = [sizes[x] * packets[x] for x in range(6)]
        #print(sum([sizes[x] * packets[x] for x in range(6)]))
        print(pack(packets))

        packets = list(map(int, stdin.readline().split()))

    return 0

main()