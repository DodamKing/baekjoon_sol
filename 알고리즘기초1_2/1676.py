# 팩토리얼 0의 개수 실버 4

n = int(input())
f = 1
factorial = []
count = 0
for i in range(1, n+1):
    f = f * i
# print(f)
for j in str(f):
    factorial.append(j)
# print(factorial)
while True:
    if factorial[-1] == '0':
        factorial.pop(-1)
        count += 1
        # print(factorial)
    else:
        break
# print(factorial)
print(count)

# print(n//5 + n//25 + n//125)