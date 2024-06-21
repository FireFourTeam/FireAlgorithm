import sys

input = sys.stdin.readline

wants = list(map(int,input().split()))

coup = list(map(int,input().split()))

full = 0

# 0 = 치킨, 1 = 힀짜 , 2 = 햄버거
for i in range(len(wants)):
    use = min(wants[i],coup[i])
    full += use
    wants[i] -= use
    coup[i] -= use

for i in range(len(wants)-1):
    if coup[i]:
        make = coup[i]//3
        coup[i] -= make * 3

        coup[i+1] += make

    if wants[i+1]:
        use = min(wants[i+1],coup[i+1])
        coup[i+1] -= use
        full += use

print(full)