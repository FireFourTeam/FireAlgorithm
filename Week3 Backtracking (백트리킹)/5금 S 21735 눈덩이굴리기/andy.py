import sys
input = sys.stdin.readline

def backTrack(idx,time,hab):
    global max_hab

    if idx == n-1 or time == m:
        max_hab = max(max_hab,hab)
        return
    
    if time+1<=m:
        if idx+1<n:
            backTrack(idx+1,time+1,hab+lst[idx+1])
        if idx+2<n:
            backTrack(idx+2,time+1,hab//2+lst[idx+2])

n,m = map(int,input().split())

lst = list(map(int,input().split()))

max_hab = 0

backTrack(-1,0,1)

print(max_hab)