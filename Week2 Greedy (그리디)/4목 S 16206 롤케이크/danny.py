n, m = map(int, input().split())   # n: 롤케이크 개수, m: 자를 수 있는 최대 횟수
lengths = list(map(int, input().split()))   # 롤케이크 길이

# 10의 배수 여부에 따라 정렬, 10의 배수가 우선
lengths = sorted(lengths, key=lambda x: (x % 10, x))

cuts = 0   # 사용한 자르기 횟수
cakes = 0  # 잘라서 만든 롤케이크 개수

# 롤케이크 자르기
for length in lengths:
    flag = True
    while length >= 10:
        if length == 10:
            cakes += 1
            length -= 10
        else:
            length -= 10
            cakes += 1
            cuts += 1
            if cuts == m:
                if length == 10:
                    cakes += 1
                print(cakes)
                flag = False
        if flag == False :
            break
    if flag == False :
        break
        
    

print(cakes)
