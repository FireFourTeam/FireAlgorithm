

###### 틀린 풀이입니다. ########

import sys
input = sys.stdin.readline

ans = []

for i in range(4):
    lst = list(map(int,input().split()))

    teams = []

    w,d,l = 0,0,0

    for i in range(0,len(lst),3):
        sub_lst = lst[i:i+3]

        tmp = min(w,sub_lst[2])
        w -= tmp
        sub_lst[2] -= tmp

        tmp = min(d,sub_lst[1])
        d -= tmp
        sub_lst[1] -= tmp

        tmp = min(l,sub_lst[0])
        l -= tmp
        sub_lst[0] -= tmp

        w += sub_lst[0]
        d += sub_lst[1]
        l += sub_lst[2]

    tmp = min(w,l)
    w -= tmp
    l -= tmp

    if w or d or l:
        ans.append(0)
    else:
        ans.append(1)

print(*ans)

###### 틀린 풀이입니다. ########