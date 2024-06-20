import sys
input = sys.stdin.readline

n,cut = map(int,input().split())

rolls = list(map(int,input().split()))

tens = []

others = []

for i in range(n):
    if not rolls[i]%10:
        tens.append(rolls[i])
    else:
        others.append(rolls[i])

tens.sort()

ten_cnt = 0

for i in range(len(tens)):
    slice_cnt = min(tens[i]//10 - 1,cut)
    if slice_cnt == tens[i]//10-1:
        ten_cnt += slice_cnt + 1
    else:
        ten_cnt += slice_cnt
    cut -= slice_cnt

for i in range(len(others)):
    slice_cnt = min(others[i]//10,cut)
    ten_cnt += slice_cnt
    cut -= slice_cnt
    
print(ten_cnt)