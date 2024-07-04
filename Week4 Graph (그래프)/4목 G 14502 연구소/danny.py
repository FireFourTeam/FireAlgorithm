import sys
from collections import deque, Counter
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

virus, empty = [], []
answer = 0

for r in range(n):
    for c in range(m):
        if board[r][c] == 0:
            empty.append([r,c])
        elif board[r][c] == 2:
            virus.append([r,c])

# print('virus: ',virus)
# print('empty: ', empty)

def in_range(next_r, next_c):
    return 0 <= next_r < n and 0<= next_c < m

def bfs():
    global answer
    tmp = [board[i][:] for i in range(n)]
    queue = deque(virus)

    while queue:
        r, c = queue.popleft()
        for dr, dc in [[-1, 0], [1, 0], [0, 1], [0,-1]]:
            next_r, next_c = r+dr, c+dc
            if in_range(next_r, next_c):
                if tmp[next_r][next_c] == 0:
                    tmp[next_r][next_c] = 2
                    queue.append((next_r, next_c))

    count = Counter([])
    for row in tmp:
        count += Counter(row)
    answer = max(answer, count[0])
    return

for new_wall in combinations(empty, 3):
    row, col = [], []
    for r, c in new_wall:
        row.append(r)
        col.append(c)
        if board[r][c] != 0:
            break

    else:
        for i in range(3):
            board[row[i]][col[i]] = 1

        bfs()
        for i in range(3):
            board[row[i]][col[i]] = 0

print(answer)