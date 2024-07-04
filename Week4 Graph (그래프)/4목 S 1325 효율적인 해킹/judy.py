from sys import stdin, stdout
from collections import deque, defaultdict

N, M = map(int, stdin.readline().split())

# 인접리스트
graph = defaultdict(list)

for _ in range(M):
    A, B = map(int, stdin.readline().split())
    graph[B].append(A)  # B를 해킹하면 A도 해킹 가능

def bfs(start):
    queue = deque([start])
    visited = [False] * (N + 1)
    visited[start] = True
    count = 0
    while queue:
        node = queue.popleft()
        count += 1
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return count

# 최대 해킹 수
max_cnt = 0
com_list = []

for i in range(1, N + 1):
    if i in graph:
        curr_cnt = bfs(i)
        if curr_cnt > max_cnt:
            max_cnt = curr_cnt
            com_list = [i]
        elif curr_cnt == max_cnt:
            com_list.append(i)

stdout.write(' '.join(map(str, sorted(com_list))) + '\n')
