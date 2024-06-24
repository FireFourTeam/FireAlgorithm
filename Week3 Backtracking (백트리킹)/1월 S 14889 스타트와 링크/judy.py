import itertools
import sys
input = sys.stdin.readline

# 팀 조합
n = int(input())
people_list = list(range(n))
team_list = list(itertools.combinations(people_list, int(n/2)))

    
score_list = [ ]
total_score = 0

# 팀 스코어 입력받기
for j in range(n):
    list_ = list(map(int, input().split()))
    total_score += sum(list_)
    score_list.append(list_)

            
result = total_score #차이
for teamA in team_list:
    team_scoreA = 0
    for i, j in list(itertools.combinations(teamA, 2)):
        team_scoreA += score_list[i][j] + score_list[j][i]
    
    team_scoreB = 0
    teamB = list(set(people_list) - set(teamA))
    for i, j in list(itertools.combinations(teamB, 2)):
        team_scoreB += score_list[i][j] + score_list[j][i]
    
    result = min(result, abs(team_scoreA - team_scoreB))
    
print(result)