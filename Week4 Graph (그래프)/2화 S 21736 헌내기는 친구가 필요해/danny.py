import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = []
start = ()
directions = [(1,0),(-1,0),(0,1),(0,-1)]
visited = [[False]*M for _ in range(N)]

answer = 0

for i in range(N):
    row = list(input().rstrip())
    for j in range(M):  # 시작점 찾기
        if row[j] == 'I':
            start = (i, j)
    graph.append(row)

def is_Valid(r, c):
    return 0<=r<N and 0<=c<M

queue = deque([start])
visited[start[0]][start[1]] = True

while queue:
    x, y = queue.popleft()
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
            
        if is_Valid(nx, ny):
            if graph[nx][ny] != 'X' and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                if graph[nx][ny] == 'P':
                    answer += 1

print(answer if answer > 0 else 'TT')