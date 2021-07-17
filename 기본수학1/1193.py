# 백준 1193 분수찾기 브론즈2
# 분수의 순서에서 규칙을 찾는 문제

X = int(input())
n = 1
sum = 1
while X > sum:
    n =  n + 1
    sum = sum + n
     
if n % 2 == 0:
    a = n - (sum - X)
    b = sum - X + 1
else:
    a = sum - X + 1
    b = n - (sum - X)    
print(str(a) + '/' + str(b))



# 1              1
# 1 2            2 1
# 3 2 1          1 2 3
# 1 2 3 4        4 3 2 1
# 5 4 3 2 1      1 2 3 4 5
# 1 2 3 4 5 6    6 5 4 3 2 1