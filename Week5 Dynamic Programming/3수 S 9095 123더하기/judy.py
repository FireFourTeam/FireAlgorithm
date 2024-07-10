
# 1, 2, 3의 합으로 나타낼 수 있는 방법

# 1 = 1

# 2 = 1 + 1
# 2 = 2

# 3 = 1 + 1 + 1
# 3 = 1 + 2
# 3 = 3

# 4 = 1 + 3
# 5 = 2 + 3
# 6 = 3 + 3


n = int(input())
numbers = [int(input()) for _ in range(n)]

max_n = max(numbers)
dp = [0] * (max_n + 1)
dp[0] = 1 

if max_n >= 1:
    dp[1] = 1
if max_n >= 2:
    dp[2] = 2
if max_n >= 3:
    dp[3] = 4

for i in range(4, max_n + 1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for n in numbers:
    print(dp[n])


