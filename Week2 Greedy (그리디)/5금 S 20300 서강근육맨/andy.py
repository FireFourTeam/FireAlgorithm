import sys
input = sys.stdin.readline

n = int(input())

gears = list(map(int,input().split()))

gears.sort()

max_loss = -1

if n%2:
    max_loss = gears[-1]
    gears.pop()

for i in range(n//2):
    left = gears[i]
    right = gears[-(i+1)]
    
    max_loss = max(max_loss,left+right)

print(max_loss)