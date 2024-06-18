import sys

input = sys.stdin.readline


####### 배열 자료구조를 이용한 풀이 ##############

n = int(input())

balloon = list(map(int,input().split()))

check = [0]*(max(balloon)+1)

cnt = 0

for i in balloon:
    if check[i]:
        check[i] -= 1
    else:
        cnt += 1

    if i-1>0:
        check[i-1] += 1

print(cnt)
###########################################



####### 딕셔너리 자료구조를 이용한 풀이 ###########
import sys

input = sys.stdin.readline

n = int(input())

balloon = list(map(int,input().split()))

dct = {}

cnt = 0

for i in balloon:
    if i in dct.keys() and dct[i]:
        dct[i] -= 1
    else:
        cnt += 1

    if i-1>0:
        if i-1 in dct.keys():
            dct[i-1] += 1
        else:
            dct[i-1] = 1

print(cnt)
##########################################