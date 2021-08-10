# 백준 2231번 분해합 브론즈2
# 모든 경우를 시도하여 N의 생성자를 구하는 문제

N = int(input())

## 처음코드
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


## 간결한 코드
sangsungja = 0
for i in range(1, N + 1):
    digit_list = [int(j) for j in str(i)]
    hap = sum(digit_list)
    if N == i + hap:
        sangsungja = i
        break
print(sangsungja)