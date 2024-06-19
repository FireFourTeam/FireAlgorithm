import sys

input = sys.stdin.readline

n,t = map(int,input().split())

carrot = []

for i in range(n):
    a,b = map(int,input().split())
    carrot.append((a,b))

carrot.sort(key=lambda x:(x[1],x[0]))

eat = 0

for i in range(n-1,-1,-1):
    t -= 1
    eat += carrot[i][0] + carrot[i][1] * t

print(eat)