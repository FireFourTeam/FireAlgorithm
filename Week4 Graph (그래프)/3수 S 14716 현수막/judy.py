from collections import deque

M, N = map(int, input().split())
graph = []

for _ in range(M):
    row = list(map(int, input().split()))
    graph.append(row)

directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]

def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
    visited[start_y][start_x] = True
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[ny][nx] and graph[ny][nx] == 1:
                queue.append((nx, ny))
                visited[ny][nx] = True

visited = [[False] * N for _ in range(M)]
count = 0

for i in range(M):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            bfs(j, i) 
            count += 1

print(count)
