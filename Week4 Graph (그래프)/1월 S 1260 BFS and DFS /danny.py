import sys
from collections import deque

N,M,V = map(int, sys.stdin.readline().split())

arr = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)
# 정점이 여러개인 경우, 작은 수부터 거치기 때문에 Sort
for i in arr:
    i.sort()

# print(arr)

def dfs(node):
    visited[node] = True
    print(node,end=" ")
    for next_node in arr[node]:
        if visited[next_node] == False:
            dfs(next_node)


def bfs(node):
    queue = deque([node])
    visited[node]=True
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for next_node in arr[node]:
            if visited[next_node] == False:
                visited[next_node] = True
                queue.append(next_node)


visited = [False for _ in range(N+1) ]
dfs(V)
print()
visited = [False for _ in range(N+1)]
bfs(V)