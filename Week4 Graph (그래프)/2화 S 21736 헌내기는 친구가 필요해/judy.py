from collections import deque

def bfs(campus, start_x, start_y, N, M):
    queue = deque([(start_x, start_y)])
    visited = [[False] * M for _ in range(N)]
    visited[start_x][start_y] = True
    people_count = 0
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if campus[nx][ny] == 'P':
                    people_count += 1
                if campus[nx][ny] in ['O', 'P']:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    
    return people_count

N, M = map(int, input().split())
campus = []
doyeon = []
for i in range(N):
    line = list(input().strip())
    campus.append(line)
    if 'I' in line:
        doyeon = [i, line.index('I')]

count = bfs(campus, doyeon[0], doyeon[1], N, M)
if count != 0 :
    print(count)
else :
    print("TT")