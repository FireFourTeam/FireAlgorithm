from collections import deque

def dfs(graph, v, visited):
    # 스택 재귀호출
    visited[v] = True
    print(v, end=' ')
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start):
    # 큐 
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True


N, M, V = map(int, input().split())

# 인접 리스트 (가중치 없음) (정점, 다음 노드)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    
    # 양방향 간선
    graph[a].append(b)
    graph[b].append(a)

# 결과
visited = [False] * (N + 1)
dfs(graph, V, visited)
print("")
bfs(graph, V)
