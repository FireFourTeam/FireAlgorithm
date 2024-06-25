import sys
from itertools import combinations

input = sys.stdin.readline

def add(combi):
    a,b = combi[0],combi[1]
    return matrix[a][b]+matrix[b][a]

n = int(input())

matrix = []

gap = sys.maxsize

for i in range(n):
    line = list(map(int,input().split()))
    matrix.append(line)

for combi in combinations([i for i in range(n)],n//2):
    teamA = 0
    teamB = 0
    for sub_combi in combinations(combi,2):
        teamA += add(sub_combi)
    
    combi2 = []

    for i in range(n):
        if i not in combi:
            combi2.append(i)
    
    for sub_combi2 in combinations(combi2,2):
        teamB += add(sub_combi2)
    
    gap = min(gap,abs(teamA-teamB))

print(gap)