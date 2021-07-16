A = []
for i in range(9):
    A.append(int(input()))
M = max(A)
a = A.index(M) # 몇 번째 수인지
print(M)
print(a+1)