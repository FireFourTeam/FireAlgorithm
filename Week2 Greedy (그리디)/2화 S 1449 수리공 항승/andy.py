import sys

input = sys.stdin.readline

end = -100

cnt = 0

n,l = map(int,input().split())

holes = list(map(int,input().split()))

holes.sort()

for i in holes:
    if end < i + 0.5:
        if end > i - 0.5:
            end += l
        else:
            end = (i-0.5) + l
        cnt += 1

print(cnt)