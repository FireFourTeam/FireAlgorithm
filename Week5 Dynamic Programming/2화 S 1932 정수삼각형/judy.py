n = int(input())
dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1):
        left = dp[i-1][j-1] if j > 0 else 0  # 왼쪽 대각선 위
        right = dp[i-1][j] if j < i else 0   # 바로 위
        dp[i][j] += max(left, right)         # 최대값을 현재 위치에 추가

print(max(dp[-1]))
