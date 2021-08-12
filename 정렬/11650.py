# 좌표 정렬하기 실버5
# 좌표를 정렬하는 문제
import sys

N = int(input())
pair_list = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    pair_list.append((x, y))
pair_list.sort()
for i in range(len(pair_list)):
    print(pair_list[i][0], pair_list[i][1])