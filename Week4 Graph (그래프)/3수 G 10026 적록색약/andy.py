import sys
from collections import deque
input = sys.stdin.readline

def grouping():
    cnt = 0
    visit = [[0]*n for i in range(n)]

    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                visit[i][j] = 1
                qu = deque()
                qu.append((i,j))

                while(qu):
                    x,y = qu.popleft()
                    for idx in range(4):
                        nx = x + dx[idx]
                        ny = y + dy[idx]
                        if 0<=nx<n and 0<=ny<n:
                            if matrix[nx][ny] == matrix[x][y] and not visit[nx][ny]:
                                visit[nx][ny] = 1
                                qu.append((nx,ny))

                cnt += 1
    
    return cnt

n = int(input())

matrix = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(n):
    line = list(input().strip())
    matrix.append(line)

normal = grouping()

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'R':
            matrix[i][j] = 'G'

red_eye = grouping()

print(normal,red_eye)