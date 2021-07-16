N = int(input())
count = 0
for i in range(1, N + 1):
    A = list(map(int, str(i)))
    if i < 100:
        count = count + 1
    elif A[1] - A[0] == A[2] - A[1]:
        count = count + 1

print(count)