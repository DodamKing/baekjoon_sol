# 백준 1978번 소수 찾기 실버4
# 2부터 x-1까지 모두 나눠서 x가 소수인지 판별하는 문제 1

N = int(input())
numbers = list(map(int, input().split()))
count = 0
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
for i in numbers:
    sosu(i)
    if sosu(i) == True:
        count = count + 1
print(count)