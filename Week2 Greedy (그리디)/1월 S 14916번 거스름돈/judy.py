# 주디

def func(n):
    coin5_cnt = n // 5 # 5원 동전 최대한 많이 사용하기
    coin_left = n % 5 # 남은 금액
    
    while coin5_cnt >= 0:
        if coin_left % 2 == 0 :
            coin2_cnt = coin_left // 2
            return coin5_cnt + coin2_cnt
        coin5_cnt -= 1
        coin_left += 5
    return -1

n = int(input())
        
print(func(n))