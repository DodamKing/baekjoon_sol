# 나이순 정렬 실버5
# 값이 같은 원소의 전후관계가 바뀌지 않는 정렬 알고리즘을 안정 정렬(stable sort)이라고 합니다.

import sys
n = int(input())
data = []
for _ in range(n):
    data.append(sys.stdin.readline().split())
data.sort(key=lambda x:int(x[0]))
for i in data:
    print(i[0], i[1])

# 버블정렬
# for i in range(len(data)-1):
#     for j in range(len(data) -1 -i):
#         if data[j][0] > data[j+1][0]:
#             data[j][0], data[j+1][0] = data[j+1][0], data[j][0]
# for k in data:
#     print(k[0], k[1])
