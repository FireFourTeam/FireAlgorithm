import sys
input = sys.stdin.readline

n,lim = map(int,input().split())

items = ["none"]

for i in range(n):
    w,v = map(int,input().split())
    items.append((w,v))

dp = [[0]*(lim+1) for i in range(n+1)]

for i in range(1,len(items)):
    w,v = items[i]
    for j in range(len(dp[0])):
        if j>=w:
            dp[i][j] = max(dp[i][j],dp[i-1][j-w] + v)
        
        dp[i][j] = max(dp[i][j],dp[i-1][j],dp[i][j-1])

print(dp[-1][-1])