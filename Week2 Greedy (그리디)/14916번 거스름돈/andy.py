import sys 

input = sys.stdin.readline

n = int(input())

dp = [sys.maxsize] * (n+1)

dp[0] = 0

for i in range(1,n+1):
    for coin in [2,5]:
        if i>=coin:
            dp[i] = min(dp[i],dp[i-coin]+1)

if(dp[i] == sys.maxsize):
    print(-1)
else:
    print(dp[i])