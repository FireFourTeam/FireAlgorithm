import sys
input = sys.stdin.readline

n,group = map(int,input().split())

line = list(map(int,input().split()))

gaps = []

for i in range(1,len(line)):
    gaps.append(line[i] - line[i-1])

gaps.sort()

for i in range(group-1):
    gaps.pop()

print(sum(gaps))