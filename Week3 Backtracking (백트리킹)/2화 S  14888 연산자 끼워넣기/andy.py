import sys
input = sys.stdin.readline

def dfs(idx,hab):
    
    global max_hab,min_hab

    if idx == n:
        max_hab = max(max_hab,hab)
        min_hab = min(min_hab,hab)
        return
    
    if calc[0]:
        calc[0] -= 1
        dfs(idx+1,hab+nums[idx])
        calc[0] += 1

    if calc[1]:
        calc[1] -= 1
        dfs(idx+1,hab-nums[idx])
        calc[1] += 1

    if calc[2]:
        calc[2] -= 1
        dfs(idx+1,hab*nums[idx])
        calc[2] += 1

    if calc[3]:
        calc[3] -= 1
        if hab<0:
            dfs(idx+1,-(abs(hab)//nums[idx]))
        else:
            dfs(idx+1,hab//nums[idx])
        calc[3] += 1

n = int(input())

nums = list(map(int,input().split()))

# +,-,*,/
calc = list(map(int,input().split()))

max_hab = -sys.maxsize
min_hab = sys.maxsize

dfs(1,nums[0])

print(max_hab)
print(min_hab)