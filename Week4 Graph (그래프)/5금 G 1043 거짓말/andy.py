import sys
from collections import deque
input = sys.stdin.readline

n,party = map(int,input().split())

knows = list(map(int,input().split()))

qu = deque()

cnt = 0

for node in knows[1:]:
    qu.append(node)

party_arr = [[] for i in range(party)]

individual_party = [[] for i in range(n+1)]

visit = [0]*(n+1)

for i in knows[1:]:
    visit[i] = 1

for i in range(party):
    lst = list(map(int,input().split()))
    party_arr[i] = lst[1:]
    for node in party_arr[i]:
        individual_party[node].append(i)

while(qu):
    node = qu.popleft()

    for my_party in individual_party[node]:
        for friend in party_arr[my_party]:
            if not visit[friend]:
                visit[friend] = 1
                qu.append(friend)

for i in range(len(party_arr)):
    lie = True
    for node in party_arr[i]:
        if visit[node]:
            lie = False
    
    if lie:
        cnt += 1

print(cnt)