N,e,w,s,n = map(int, input().split())

percent = [e/100,w/100,s/100,n/100] # 0보다 크거나 100보다 작은 자연수

visited = [[0 for r in range(2*N+1)] for c in range(2*N+1)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def backtracking(count, x,y):
    if count==N:
        return 1
    
    visited[x][y] = 1 # 시작점
    total_per = 0

    for i in range(len(directions)):
        dx, dy = directions[i]
        next_x = x+dx
        next_y = y+dy
        if visited[next_x][next_y]: #방문한 경우 
            continue
        total_per += backtracking(count+1,next_x,next_y)*percent[i] # 방향과 퍼센티지의 순서를 맞춰야 하는 이유
    visited[x][y] = 0
    return total_per

print(backtracking(0,N,N))