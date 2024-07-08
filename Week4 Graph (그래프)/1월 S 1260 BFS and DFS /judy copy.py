# 그래프를 DFS로 탐색한 결과와, BFS로 탐색한 결과를 출력하는 프로그램
# 방문할 수 있는 노드가 여러개인 경우, 번호가 적은 것을 먼저 방문

# 정점개수(N), 간선 개수(M)
# 간선 - 간선

from collections import deque

N, M, V = map(int, input().split())
# N : 노드 수
# M : 간선 수
# V : 탐색 시작할 번호

graph = [[] for _ in range(N + 1)] # 인접리스트
for _ in range(M):
    a, b = map(int, input().split()) # 간선 정보
    # 양방향 간선
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1) # 방문 노드 기록용, 노드 = i

def dfs(graph, V):
    visited[V] = True  # 시작점에 방문
    print(V, end='') # 방문한 곳 출력
    for i in sorted(graph[V]): # 방문한 곳 중 연결된 노드에
        if not visited[i]: # 방문한 노드가 아니면
            dfs(graph, i)
            
def bfs(graph, V):
    visited = [False]*len(graph)
    q = deque([V])
    visited[V] = True
    
    while q:
        node = q.popleft()
        print(node, end='')
        for i in sorted(graph[node]):
            if not visited[i]:
                q.append(i)
                visited[i] = True
    

dfs(graph, V)
bfs(graph, V)