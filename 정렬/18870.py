# 좌표 압축 실버2
# 만약 정확한 값이 필요 없고 값의 대소 관계만 필요하다면, 모든 수를 0 이상 N 미만의 수로 바꿀 수 있습니다.

import sys
n = int(input())
coord_list = [i for i in map(int, sys.stdin.readline().split())]
coord_list1 = list(set(coord_list))
coord_list1.sort()
# compression_list = []
# print(coord_list)
# print(coord_list1)
# for j in coord_list:
#     count = 0
#     for k in coord_list1:
#         if j > k:
#             count += 1
#     compression_list.append(count)
# print(compression_list)

# for j in coord_list:
#     print(coord_list1.index(j), end=' ')

compression_dic = {coord_list1[j]:j for j in range(len(coord_list1))}
for k in coord_list:
    print(compression_dic[k], end=' ')