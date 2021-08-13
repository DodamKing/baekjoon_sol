# 좌표 정렬하기2 실버2
# 좌표를 다른 순서로 정렬하는 문제

# import sys
# n = int(input())
# pair_list = []
# for _ in range(n):
#     x, y = map(int, sys.stdin.readline().split())
#     pair_list.append((x, y))
# pair_list.sort(key=lambda i:(i[1], i[0]))
# for i in range(n):
#     print(pair_list[i][0], pair_list[i][1])

from operator import itemgetter
import sys
n = int(input())
pair_list = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    pair_list.append((x, y))
pair_list.sort(key=itemgetter(1,0))
for i in range(n):
    print(pair_list[i][0], pair_list[i][1])