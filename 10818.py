import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split())[:N])

print(min(A), max(A))

