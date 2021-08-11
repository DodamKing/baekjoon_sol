# 통계학 실버4
# 정렬을 활용하는 문제

import sys
import itertools
from collections import Counter

N = int(input())
data = []
for _ in range(N):
    data.append(int(sys.stdin.readline()))
data.sort()

# 시간초과
# count_list = []
# for i in data:
#     count_list.append(data.count(i))
# mode_dictionary = dict(zip(data, count_list))

# mode_list = []
# for key, value in mode_dictionary.items():
#     if value == max(mode_dictionary.values()):
#         mode_list.append(key)
# if len(mode_list) == 1:
#     mode = mode_list[0]
# else:
#     # mode_list.remove(min(mode_list))
#     # mode = min(mode_list)
#     moed = mode_list[1]

mode_dict = Counter(data) # 중복 되는 것의 개수를 세서 딕셔너리로 만들어 준다.
mode_list = mode_dict.most_common() # 개수가 많은, 빈도가 큰 값으로 정렬해서 리스트 튜플 형태로 리턴해준다.
if len(mode_list) == 1:
    mode = mode_list[0][0]
else:
    if mode_list[0][1] == mode_list[1][1]:
        mode = mode_list[1][0]
    else:
        mode = mode_list[0][0]

# if len(mode_list) != 1 and mode_list[0][1] == mode_list[1][1]:
#     mode = mode_list[1][0]
# else:
#     mode = mode_list[0][0]
    

mean = round(sum(data) / N)
median = data[int(N/2)]
# mode = 
rang = max(data) - min(data)

print(mean)
print(median)
print(mode)
print(rang)