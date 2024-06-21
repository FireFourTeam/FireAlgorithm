# 차례대로 학생을 포함/비포함 시키면서 최소 비용을 찾는다. O(n)
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
babies_tall = list(map(int, input().split())) #tall

def func():
    if K==1 : 
        print(0)
        return
        
    # [LBaby, idx, RBaby, idx, gap]
    chart = []
    for idx, baby in enumerate(babies_tall) :
        if idx == (len(babies_tall)-1) :
            break
        chart.append([babies_tall[idx], idx, babies_tall[idx+1], idx+1, babies_tall[idx+1]-babies_tall[idx]])

    chart.sort(key= lambda x: (-x[4], -x[2]))

    cost = 0
    cost_chart = [] # k-1개
    for i in range(K-1) :
        cost_chart.append(chart[i])
        cost += chart[i][0] #left
        cost -= chart[i][2] #right

    cost_chart.sort(key= lambda x: x[0])

    # 첫번째 구분선 왼쪽이 첫 아이가 아니라면, 첫번째 아이를 빼줘야함
    if cost_chart[0][1] != 0 :
        cost -= babies_tall[0]
    # 첫번째 구분선 왼쪽이 첫 아이라면, 더해야 하는데, 이미 더했으므로 놔둠.
    else :
        cost -= babies_tall[0]
    # 마지막 구분선 오른쪽이 마지막 아이가 아니라면, 마지막 아이를 더해줘야함

    if K>=2 and (cost_chart[K-2][3] != (len(babies_tall)-1)) :
        pass
    # 마지막 구분선 오른쪽이 마지막 아이라면, 빼지 않고 더해야함
    else :
        cost += babies_tall[len(babies_tall)-1]
        
    print(cost)
    return

func()