money = int(input())

flag = 0
while money > 0:
    if money % 5 == 0:
        flag += money//5
        break
    else:
        money -= 2
        flag += 1

if money < 0:
    print(-1)
else:
    print(flag)
