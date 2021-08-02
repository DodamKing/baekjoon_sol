# 백준 10872번 팩토리얼 브론즈3
# 팩토리얼은 단순 for문으로도 구할 수 있지만 학습을 위해 재귀를 써 봅시다.

def f(N):
    if N == 0 or N == 1:
        return 1
    return N * f(N-1)

N = int(input())

print(f(N))