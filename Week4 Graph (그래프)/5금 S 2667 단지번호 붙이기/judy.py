# 입력
N = int(input())
apt = []
for _ in range(N):
    apt.append(list(map(int, input().strip())))

count = 0
dan_cnt = [0]

# 계산
# 0 또는 1
def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if apt[x][y] == 1:
        apt[x][y] = 0
        dan_cnt[-1] += 1
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False

for i in range(N):
    for j in range(N):
        if dfs(i, j):
            count += 1
            dan_cnt.append(0)
dan_cnt.sort()
del dan_cnt[0]

# 출력
# 총 단지수
# 각 단지내 집의 수를 오름차순, 한 줄에 하나씩
print(count)
if count > 0:
    for cnt in dan_cnt:
        print(cnt)


