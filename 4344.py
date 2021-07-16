C = int(input())
for i in range(C):
    A = list(map(int, input().split()))
    s = sum(A)
    N = A[0]
    real_sum = s - N
    ever = real_sum / N
    count = 0
    for j in A:
        if j > ever and A.index(j) != 0:
            count = count + 1
        result = count / N * 100
    print('{0:.3f}%'.format((result)))