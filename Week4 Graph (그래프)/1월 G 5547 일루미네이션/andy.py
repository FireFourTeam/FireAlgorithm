import sys
input = sys.stdin.readline

n,m = map(int,input().split())

matrix = []

x_y_dct = {}

for i in range(n):
    line = list(map(int,input().split()))
    matrix.append(line)

dx_odd = [1,0,-1,0,1,1]
dy_odd = [1,1,0,-1,-1,0]

dx_even = [0,-1,-1,-1,0,1]
dy_even = [1,1,0,-1,-1,0]

for i in range(n):
    y = i+1
    for j in range(m):
        x = j+1
        ki = str(x)+','+str(y)
        x_y_dct[ki] = [i,j]