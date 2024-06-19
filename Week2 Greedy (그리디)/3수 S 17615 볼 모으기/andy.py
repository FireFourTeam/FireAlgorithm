import sys

input = sys.stdin.readline

def check(start,end,stride):

    move = 0

    is_cut = False

    for i in range(start,end,stride):
        if arr[i] == color:
            if is_cut:
                move += 1
        else:
            is_cut = True
    return move

n = int(input())

arr = list(input())

min_move = sys.maxsize

for color in ["R","B"]:
    min_move = min(min_move,check(0,n,1)) # 왼쪽으로 color볼을 모음
    min_move = min(min_move,check(n-1,-1,-1)) # 오른쪽으로 color볼을 모음

print(min_move)