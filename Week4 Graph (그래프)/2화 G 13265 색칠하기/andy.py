import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

for i in range(n):
    node,edge = map(int,input().split())

    my_adj = [[] for i in range(node+1)]

    visit = [0]*(node+1)

    possible = True

    idx = 0

    for i in range(edge):
        a,b = map(int,input().split())
        my_adj[a].append(b)
        my_adj[b].append(a)
    
    for i in range(1,node+1):
        if visit[i] == 0:
            visit[i] = "R"
            qu = deque()
            qu.append((i,"R"))
            
            while(qu):
                node,color = qu.popleft()

                for next_node in my_adj[node]:
                    if visit[next_node] == 0:
                        visit[next_node] = "R" if color == "B" else "B"
                        qu.append((next_node,visit[next_node]))
                    elif visit[next_node] == visit[node]:
                        possible = False
    
    if possible:
        print("possible")
    else:
        print("impossible")

    