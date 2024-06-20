import sys
input = sys.stdin.readline

N = int(input())
A_sum = 0

line = []
for i in range(N) :
    X, A = map(int, input().split())
    line.append([X,A])
    A_sum += A

A_check_halfsum = 0
half_X = 0
line.sort(key= lambda x: x[0])
for X, A in line :
    A_check_halfsum += A
    if A_check_halfsum >= A_sum/2 :
        half_X = X 
        break
    
# 중앙값
print(int(half_X))
