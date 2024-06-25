import sys
input = sys.stdin.readline

# 입력
stoku = []
for i in range(9):
    row = list(str(input()).strip().split())
    stoku.append(row)
# print(stoku)

# 스토쿠 뒤집기
stoku_ud = [[stoku[row][col] for row in range(9)] for col in range(9)]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 없는 수 찾기
left_row = []  # row에 없는 수
left_col = []  # col에 없는 수

for row in stoku:
    left_row.append(set(numbers) - set(row) - {0})
        
for col in stoku_ud:
    left_col.append(set(numbers) - set(col) - {0})

stoku_isec = [[[] for _ in range(9)] for _ in range(9)]

# 각 칸에 들어갈 수 있는 수
for i in range(9):
    for j in range(9):
        if stoku[i][j] == 0:  
            stoku_isec[i][j] = left_row[i].intersection(left_col[j])

print(stoku_isec)
