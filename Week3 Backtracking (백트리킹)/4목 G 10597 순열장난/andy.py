import sys,heapq

input = sys.stdin.readline

def dfs(idx,prev,dct,cnt):
    global ans
    if ans != None:
        return
    
    if idx == len(lst):
        num = 1
        while(1):
            if num in dct.keys():
                num+=1
            else:
                break
        if num == cnt:
            ans = 1
            for ki in dct.keys():
                print(ki)
        return
    
    if prev != None:
        new_num = int(str(prev)+str(lst[idx]))
        if new_num not in dct.keys():
            dct[new_num] = 1
        else:
            return
        dfs(idx+1,None,dct,cnt+1)
        del dct[new_num]
    elif int(lst[idx]) == 0:
        return
    elif int(lst[idx]) not in dct.keys():
        dct[int(lst[idx])] = 1
        dfs(idx+1,None,dct,cnt+1)
        del dct[int(lst[idx])]

        if idx<len(lst)-1:
            dfs(idx+1,lst[idx],dct,cnt)

lst = list(input().strip())

dct = {}

ans = None

dfs(0,None,dct,0)