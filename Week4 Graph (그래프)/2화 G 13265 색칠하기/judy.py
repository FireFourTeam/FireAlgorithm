from collections import deque

t = int(input())  

test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    test_cases.append((n, m, edges))

def seperate(n, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    color = [0] * (n + 1)  # 0: 미방문, 1: 색1, -1: 색2

    # BFS를 통해 그래프 그룹 2개로 분할
    for start in range(1, n + 1):
        if color[start] == 0:  # 아직 방문하지 않은 노드
            queue = deque([start])
            color[start] = 1
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] == 0:  # 방문하지 않은 노드
                        color[neighbor] = -color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]: # 같은 색상으로 인접한 경우
                        return "impossible"
    return "possible"

for n, m, edges in test_cases:
    print(seperate(n, edges))
