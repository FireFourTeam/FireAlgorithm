from collections import deque

def bfs(x, y): # graph[x][y] == 1 일때 들어와서 연결된 모든 1을 0으로 만들고 다음 글자 탐색
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
directions = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            bfs(i, j)
            answer += 1
print(answer)