# 백준 2231번 분해합 브론즈2
# 모든 경우를 시도하여 N의 생성자를 구하는 문제

N = int(input())
con = 1
con_list = []

while con <= N:
    sum = 0
    for i in str(con):
        sum = sum + int(i)
    if N == con + sum:
        con_list.append(con)
    con += 1

if len(con_list) == 0:
    print(0)        
else:
    print(min(con_list))


sangsungja = 0
for i in range(1, N + 1):
    digit_list = list(map(int, str(i)))
print(sum(digit_list))
#     hap = sum(digit_list)
#     if N == i + hap:
#         sangsungja = i
# print(sangsungja)