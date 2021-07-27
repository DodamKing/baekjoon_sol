# 백준 1929번 소수 구하기 실버2
# 에라토스테네스의 체로 풀어 봅시다.

import math

M, N = map(int, (input().split()))
sosu_list = []

def sosu_Era(x):
    factor = int(math.sqrt(x))
    if x == 1:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    
    for i in range(3, factor + 1):
        if x % i == 0:
            return False
    return True

for i in range(M, N + 1):
    if sosu_Era(i) == True:
        sosu_list.append(i)

for j in sosu_list:
    print(j)