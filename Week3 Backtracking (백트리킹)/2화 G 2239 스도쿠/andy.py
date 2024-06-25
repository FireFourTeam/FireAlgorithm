import sys
input = sys.stdin.readline

def dfs(i,j):
    global zero,row,col,sub_square,ans

    if ans != None:
        return
    
    if not zero:
        ans = 1
        for i in range(len(matrix)):
            word = ''
            for j in range(len(matrix[i])):
                word += str(matrix[i][j])
            print(word)
        return
    
    group = 3*(i//3) + j//3

    next_x,next_y = None,None

    for x in range(i,9):
        for y in range(9):
            if not matrix[x][y] and not (x==i and y==j):
                next_x,next_y = x,y
                break
        if next_x != None:
            break

    for num in range(1,10):
        if not row[i][num] and not col[j][num] and not sub_square[group][num]:
            row[i][num] = 1
            col[j][num] = 1
            sub_square[group][num] = 1
            matrix[i][j] = num
            zero -= 1
            
            dfs(next_x,next_y)
                        
            row[i][num] = 0
            col[j][num] = 0
            sub_square[group][num] = 0
            matrix[i][j] = 0
            zero += 1


matrix = []

for i in range(9):
    line = list(map(int,list(input().strip())))
    matrix.append(line)

row = [[0]*10 for i in range(9)]

col = [[0]*10 for i in range(9)]

sub_square = [[0]*10 for i in range(9)]

ans = None

zero = 0

init_x,init_y = None,None

for i in range(9):
    for j in range(9):
        if matrix[i][j]:
            row[i][matrix[i][j]] = 1
            col[j][matrix[i][j]] = 1
            group = 3*(i//3) + j//3
            sub_square[group][matrix[i][j]] = 1
        else:
            zero += 1
            if init_x == None:
                init_x,init_y = i,j


dfs(init_x,init_y)