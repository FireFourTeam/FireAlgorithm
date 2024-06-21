import sys
input = sys.stdin.readline

N = int(input())
A_sum = 0

# 일직선 마을 = line
line = []
for i in range(N) : # 입력과 전체 사람 수 구하기
    X, A = map(int, input().split())
    line.append([X,A])
    A_sum += A

A_check_halfsum = 0 # 사람들 절반넘어가는 것 측정 변수
half_X = 0 # 결과 위치

line.sort(key= lambda x: x[0]) #이런 문제 특 : 순서대로 안줌
for X, A in line :
    A_check_halfsum += A
    if A_check_halfsum >= A_sum/2 : #처음으로 절반 넘어가는 것
        half_X = X 
        break
    
# 중앙값
print(int(half_X))

# 질량 중심이 아닌 이유.. ㅠ