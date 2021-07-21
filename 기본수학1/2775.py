# 백준 2775번 부녀회장이 퇼테야 브론즈2
# 층과 거주자의 수의 규칙을 찾는 문제
# 못 품 이해안감 ㅠㅠ

T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    P = [x for x in range(1, n + 1)] # 0층 리스트
    for j in range(k): # 층수 만큼 반복
        for y in range(1, n):
            P[y] = P[y] + P[y - 1]
    print(P[-1])

    