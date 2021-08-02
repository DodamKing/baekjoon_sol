# 백준 10870번 피보나치 수 5 브론즈2
# 피보차니 수 역시 단순 for문으로도 구할 수 있지만, 학습을 위해 재귀를 써 봅시다.

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

n = int(input())
print(fib(n))