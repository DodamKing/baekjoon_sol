# 백준 1436 영화감독 숌 실버5
# N번째 종말의 수가 나올 때까지 차례대로 시도하는 문제

# def solution(n):
#     if n == 1:
#         return 666
#     elif 2 <= n <= 6:
#         return int(str(n-1) + '666')
#     elif 7 <= n <= 16:
#         return int('666' + str(n-7))
#     elif 17 <= n <= 25:
#         return int(str(n-10) + '666')
#     elif 26 <= n <= 35:
#         return int('1666'+ str(n-26))

# for i in range(1, 36):
#     print(solution(i))



N = int(input())
n = 665
count = 0
while count < N:
    n += 1
    if str(n).find('666') >= 0:
        count += 1
print(n)
