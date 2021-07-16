def d(n):
    a = sum(map(int, str(n)))
    return n + a

A = set()
B = set()

for n in range(10001):
    A.add(n)
    B.add(d(n))

result = sorted(list(A - B))
for i in result:
    print(i)