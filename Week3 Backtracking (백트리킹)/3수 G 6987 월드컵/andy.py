import sys
from itertools import combinations
input = sys.stdin.readline

def dfs(idx):
    global teams,possible
    if possible:
        return
    if idx == len(lst):
        hab = 0
        for team in teams:
            hab += sum(team)
        if not hab:
            possible = True
        
        return

    for i in [(0,2),(1,1),(2,0)]:
        team1 = lst[idx][0]
        team2 = lst[idx][1]

        if teams[team1][i[0]] and teams[team2][i[1]]:
            teams[team1][i[0]] -= 1
            teams[team2][i[1]] -= 1
            dfs(idx + 1)
            teams[team1][i[0]] += 1
            teams[team2][i[1]] += 1

for i in range(4):
    line = list(map(int,input().split()))
    teams = [[] for i in range(6)]
    possible = False
    for i in range(0,len(line),3):
        win,draw,lose = line[i:i+3]
        teams[i//3] = [win,draw,lose]
    
    lst = list(combinations([0,1,2,3,4,5],2))

    dfs(0)

    if possible:
        print(1,end=" ")
    else:
        print(0,end=" ")
    