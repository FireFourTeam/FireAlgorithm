import sys
input = sys.stdin.readline

n,k = map(int,input().split())

money = [0]*(k+1)

money[0] = 1

coins = []

for i in range(n):
    coin = int(input())
    coins.append(coin)

coins.sort()

for i in range(1,len(money)):
    for coin in coins:
        if i>= coin:
            money[i] += money[i-coin]
            
print(money[k])