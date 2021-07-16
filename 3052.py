A = []
B = []
for i in range(10):
    A.append(input())
for j in A:
    B.append(int(j) % 42)
print(len(set(B))) #set은 집합 중복 허용 X