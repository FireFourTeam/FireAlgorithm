import sys
input = sys.stdin.readline

n = int(input())

dp = [0]*12

dp[0] = 1

for num in range(1,12):
    for i in [1,2,3]:
        if num>=i:
            dp[num] += dp[num-i]

for i in range(n):
    num = int(input())
    print(dp[num])
