""" 
오전 오리
당근 : N개
T일
오리는 당근의 맛을 충분히 높이기 위해 항상 N이상인 T일 동안 재배

당근 맛 : wi
영양제 T개 : 당근 맛 + pi
당근 자리에 없으면 심고 있으면 영양제 준다
N이상인 T일 동안 재배

오후 토끼
하루에 당근 먹거나, 먹지 않거나 / 당근의 맛 합 최대

T일 동안 토끼가 먹을 수 있는 당근의 맛 합 최대값


N+1개의 줄
N(1 ≤ N ≤ 200,000)과 T(N ≤ T ≤ 100,000,000)
당근 i의 wi와 pi

당근 2개 2일
(3, 4) (1, 2)
3 1
7 3


"""

import heapq

def max_carrot_taste(N, T, carrots):
    max_taste = 0
    pq = []
    reset_pq = []

    # 첫날에는 당근을 모두 심는다
    for i in range(N):
        wi, pi = carrots[i]
        heapq.heappush(pq, (-wi, wi, pi, i, 0))  # 최대 힙 -
        # pq = [(-3, 3, 4, 0, 0), (-1, 1, 2, 1, 0)]
        
    # T일 동안
    for day in range(T):
        # 오전 : 당근에 영양제, 다시 심어진 당근 제외
        new_pq = []
        while pq:
            _, current_wi, pi, index, days_sown = heapq.heappop(pq)
            if days_sown == 0:
                current_wi += pi  # 영양제
            new_pq.append((-current_wi, current_wi, pi, index, days_sown + 1))
        pq = new_pq
        
        # 오후 : 토끼냠냠 
        if pq:
            _, tastiest_wi, pi, index, _ = heapq.heappop(pq)
            max_taste += tastiest_wi
            # 먹은 당근을 다시 심음
            heapq.heappush(reset_pq, (-carrots[index][0], carrots[index][0], carrots[index][1], index, 0))

        # 다시 심은 당근을 pq로 이동
        while reset_pq:
            heapq.heappush(pq, heapq.heappop(reset_pq))

    return max_taste


N, T = map(int, input().split())
carrots = [tuple(map(int, input().split())) for _ in range(N)]

print(max_carrot_taste(N, T, carrots))
