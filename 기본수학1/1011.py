# 백준 1011 Fly me to the Alpha Centauri 실버1
# 거리에 따른 장치 사용 횟수를 출력하는 문제
# 못품ㅜㅠ

import math

T = int(input())

for i in range(T):
    x, y = map(int, input().split())
    d = y - x # 거리
    count = 0
    
    rd = math.floor(math.sqrt(d)) # 루트거리 floor는 내림
    sd = rd **2 #루트거리 제곱

    if d < 4: # 거리가 1, 2, 3 이면 횟수는 그냥 카운트를 찍어냄
        print(d)
    else: # 규칙 찾기가 까다롭다 구글링 해서 규칙 찾아서 간신히 이해만 함 ㅠㅠ
        if d > rd + sd:
            count = 2 * rd + 1
        elif sd < d <= rd + sd:
            count = 2 * rd
        elif d == sd:
            count = 2 * rd -1
        print(count)