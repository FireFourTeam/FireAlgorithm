import sys,copy
from itertools import combinations
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

matrix = []

empty = []
virus = []

max_safe = -1

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(n):
    line = list(map(int,input().split()))
    matrix.append(line)

for i in range(n):
    for j in range(m):
        if not matrix[i][j]:
            empty.append(m*i+j)
        elif matrix[i][j] == 2:
            virus.append((i,j))

for xyz in combinations(empty,3):

    infected = 0

    visit = [[0]*m for i in range(n)]

    for i in xyz:
        x,y = i//m,i%m

        matrix[x][y] = 1

    qu = deque(copy.deepcopy(virus))

    while(qu):
        x,y = qu.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visit[nx][ny] and not matrix[nx][ny]:
                visit[nx][ny] = 1
                infected += 1
                qu.append((nx,ny))
    
    max_safe = max(max_safe,(len(empty)-3)-infected)

    for i in xyz:
        x,y = i//m,i%m

        matrix[x][y] = 0

print(max_safe)