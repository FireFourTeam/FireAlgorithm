import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

matrix = []

cnt = 0

for i in range(n):
    line = list(input().strip())
    matrix.append(line)

qu = deque()

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'I':
            qu.append((i,j))

while(qu):
    x,y = qu.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
    
        if 0<=nx<n and 0<=ny<m and (matrix[nx][ny] == 'O' or matrix[nx][ny] == 'P'):
            if matrix[nx][ny] == 'P':
                cnt += 1
            
            matrix[nx][ny] = 'X'
            qu.append((nx,ny))

print(cnt if cnt else 'TT')