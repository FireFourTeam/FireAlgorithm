import sys

input = sys.stdin.readline

lst = input().strip()

n = len(lst)

max_num = n if n<=9 else 9 + (n-9)//2

arr = []

done = False

def dfs(idx):
    global arr,done
    if done:
        return
    if idx == len(lst):
        done = True
        print(*arr)
        return
    
    if lst[idx] != '0' and lst[idx] not in arr and int(lst[idx])<=max_num:
        arr.append(lst[idx])
        dfs(idx+1)
        arr.pop()
    
    if lst[idx] != '0' and idx+1 < len(lst) and lst[idx:idx+2] not in arr and int(lst[idx:idx+2])<=max_num:
        arr.append(lst[idx:idx+2])
        dfs(idx+2)
        arr.pop()

dfs(0)