import sys
from itertools import combinations
input = sys.stdin.readline

numberlist = []
while True:
    templist = list(map(int, input().split()))
    if templist == [0]:
        break
    k = templist[0]
    S = templist[1:]
    numberlist.append([k, S])

results = []
# 문자열로 바꾸어서 출력
for idx, (k, S) in enumerate(numberlist):
    combi = list(combinations(S, 6)) # 조합
    case_result = []
    for com in combi:
        case_result.append(' '.join(map(str, com)))
    results.append('\n'.join(case_result))
    if idx < len(numberlist) - 1:
        results.append('') # 테스트 케이스 사이 엔터

print('\n'.join(results))
