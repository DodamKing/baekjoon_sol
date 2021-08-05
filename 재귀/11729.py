# 백준 11729번 하노이 탑 이동 순서 실버2
# 재귀적인 패턴을 재귀함수로 찍는 문제2

def count(N):
    if N == 1:
        return 1
    else:
        return (count(N-1) * 2 + 1) 

def hanoi(N, A, C, B):
    if N == 1:
        print(A, C) # 한 개 일 땐 A에서 C로 옮긴다
    else:
        hanoi(N-1, A, B, C) # n-1개를 A에서 B로 C를 거쳐 옮겨라
        print(A, C) # 가장 큰 원판을 A에서 C로 옮겨라
        hanoi(N-1, B, C, A) # 이동된 n-1개의 원판을 B에서 C로 A를 거쳐서 옮겨
    

N = int(input())
print(count(N))  # 2**n-1
hanoi(N, 1, 3, 2)