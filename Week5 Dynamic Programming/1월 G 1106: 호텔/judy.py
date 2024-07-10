# 세계적인 호텔 홍보
# 홍보 가능한 도시, 비용, +고객수

# 적어도 C명 고객을 늘리기 위해 투자해야 하는 돈의 최소값
# N : 홍보 도시 수

def minCost(C, data):
    #비용집계 리스트
    end = C + 1000
    dp = [float('inf')] * (end) 
    dp[0] = 0  # 0명의 고객을 얻는데 드는 비용은 0

    # 도시마다 분석
    for cost, plus in data:
        for i in range(plus, end):
            if dp[i - plus] != float('inf'):
                dp[i] = min(dp[i], dp[i - plus] + cost)

    #최소값 계산
    min_cost = float('inf')
    for i in range(C, end):
        min_cost = min(min_cost, dp[i])
    
    return min_cost


# 입력
C, N = map(int, input().split())

data = []
for _ in range(N):
    cost, plus = map(int, input().split())
    data.append((cost, plus))

print(minCost(C, data))
