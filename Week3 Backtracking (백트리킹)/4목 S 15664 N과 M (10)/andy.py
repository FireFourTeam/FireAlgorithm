import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int,input().split())

lst = list(map(int,input().split()))

lst.sort()

dct = {}

for combi in combinations(lst,m):
    if combi not in dct.keys():
        dct[combi] = 1
        print(*combi)
    