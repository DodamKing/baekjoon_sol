# 소인수분해 실버4
# N을 소인수분해하는 문제

N = int(input())
i = 2

if N == 1:
    print()
else:
    while N != 1:
        if N % i == 0:
            N = N / i
            print(i) 
        else: 
            i = i + 1
