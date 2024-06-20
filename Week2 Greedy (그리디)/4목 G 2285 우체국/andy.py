import sys
input = sys.stdin.readline

n = int(input())

villages = []

total_cnt = 0

total_cost = 0

for i in range(n):
    x,cnt = map(int,input().split())
    total_cnt += cnt
    villages.append((x,cnt))

villages.sort()

leftest_x = villages[0][0]

for i in range(n):
    total_cost += abs(leftest_x - villages[i][0]) * villages[i][1] # 제일 왼쪽 마을에 우물 지었을 때 비용 계산 = total_cost 초기화 작업

previous_x = villages[0][0] # 가장 최근에 처리한 x를 저장하는 변수

left_cnt = 0 # 현재의 마을 기준으로 왼쪽에 있는 주민 수

min_val = total_cost

build_x = villages[0][0]

for i in range(len(villages)):
    x = villages[i][0]   #현재 마을의 x
    cnt = villages[i][1] # 현재 마을 주민수
    move = x-previous_x # 이전 최근 마을에서 현재 마을까지 거리
    right_cnt = total_cnt - left_cnt #오른쪽 주민수

    total_cost += left_cnt * move # 우물을 땡겨온 거리 만큼 왼쪽 주민 수 입장에서는 move 만큼 멀어짐
    total_cost -= right_cnt * move # 반대로 오른쪽 주민 수 입장에서는 move 만큼 가까워짐

    left_cnt += cnt # 다음 i 기준에서는 현재 x 마을의 주민들이 왼쪽이 되므로 cnt를 + 함

    if min_val > total_cost:
        min_val = total_cost
        build_x = x
    
    previous_x = x

print(build_x)