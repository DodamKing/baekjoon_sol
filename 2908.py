# 상수
# 숫자를 뒤집어서 비교하는 문제

A = []
B = []
a, b = map(int, input().split())
for i in str(a):
    A.append(i)
for j in str(b):
    B.append(j)
A.reverse()
B.reverse()

result_A = int(''.join(A))
result_B = int(''.join(B))
if result_A > result_B:
    print(result_A)
else:
    print(result_B)

# 위에 코드가 너무 지저분하다
# 컴팩트한 코드를 가져온다

x, y = input().split()
x = int(x[::-1]) # 숫자를 뒤집는 방법
y = int(y[::-1])

print(x) if x > y else print(y)