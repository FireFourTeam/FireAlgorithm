import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

matrix = []

x_y_dct = {}

for i in range(m):
    line = list(map(int,input().split()))
    matrix.append(line)

dx_even = [1,0,-1,0,1,1]
dy_even = [1,1,0,-1,-1,0]

dx_odd= [0,-1,-1,-1,0,1]
dy_odd= [1,1,0,-1,-1,0]

for i in range(m):
    y = i+1
    for j in range(n):
        x = j+1
        ki = str(x)+','+str(y)
        x_y_dct[ki] = [i,j]

qu = deque()

for i in range(1,n+1):
    ki = str(i)+','+str(1)
    ki2 = str(i)+','+str(m)
    x,y = x_y_dct[ki]
    x2,y2 = x_y_dct[ki2]
    if not matrix[x][y]:
        matrix[x][y] = 2
        qu.append((i,1))

    if not matrix[x2][y2]:
        matrix[x2][y2] = 2
        qu.append((i,m))

for i in range(2,m):
    ki = str(1)+','+str(i)
    ki2 = str(n)+','+str(i)
    
    x,y = x_y_dct[ki]
    x2,y2 = x_y_dct[ki2]

    if not matrix[x][y]:
        matrix[x][y] = 2
        qu.append((1,i))

    if not matrix[x2][y2]:
        matrix[x2][y2] = 2
        qu.append((n,i))
    
while(qu):
    x,y = qu.popleft()

    origin_x,origin_y = x_y_dct[str(x)+','+str(y)]

    if origin_x%2:

        arr_x = dx_odd
        arr_y = dy_odd

    else:
        arr_x = dx_even
        arr_y = dy_even

    for i in range(6):
        nx = x + arr_x[i]
        ny = y + arr_y[i]

        ki = str(nx)+','+str(ny)

        if ki in x_y_dct.keys():
            origin_nx,origin_ny = x_y_dct[ki]
            if not matrix[origin_nx][origin_ny]:
                matrix[origin_nx][origin_ny] = 2
                qu.append((nx,ny))

hab = 0

for ki in x_y_dct.keys():
    org_x,org_y = x_y_dct[ki]
    x,y = map(int,ki.split(','))
    if matrix[org_x][org_y] != 1:
        continue
    
    plus = 6

    if org_x%2:

        arr_x = dx_odd
        arr_y = dy_odd

    else:
        arr_x = dx_even
        arr_y = dy_even
    
    for i in range(6):
        nx = x + arr_x[i]
        ny = y + arr_y[i]

        ki2 = str(nx)+','+str(ny)

        if ki2 in x_y_dct.keys():
            origin_nx,origin_ny = x_y_dct[ki2]
            if matrix[origin_nx][origin_ny] == 2:
                continue
            else:
                plus -= 1

    hab += plus

print(hab)