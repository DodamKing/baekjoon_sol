# 백준 2581번 소수 실버5
# 2부터 x-1까지 모두 나눠서 x가 소수인지 판별하는 문제2

M = int(input())
N = int(input())
sosu_list = []

def sosu(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

for i in range(M, N + 1):
    if sosu(i) == True:
        sosu_list.append(i)

if sosu_list == []:
    print(-1)
else:
    print(sum(sosu_list))
    print(min(sosu_list))