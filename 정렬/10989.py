# 수 정렬하기3 실버5
# 수의 범위가 작다면 카운팅 정렬을 사용하여 더욱 빠르게 정렬할 수 있습니다.

## 메모리 초과
import sys
# N = int(input())
# number_list = []
# for _ in range(N):
#     line = sys.stdin.readline()
#     number_list.append(line.strip('\n'))
# number_list.sort()
# print('\n'.join(number_list))

## 카운팅 정렬 활용
N = int(input())
# 리스트 작성시 메모리를 먹는거 같음
# li = []
# for _ in range(N):
#     num = sys.stdin.readline()
#     li.append(int(num.rstrip('\n')))

# 인풋으로 받은 수가 몇변 들어왔는지 빈도 저장
counting_li = [0] * 10001
for _ in range(N):
    i = int(sys.stdin.readline())
    counting_li[i] += 1

# 배열의 시작부터 돌며 저장된 빈도만큼 인덱스값을 출력
for j in range(1, 10001):
    count = counting_li[j]
    for _ in range(count):
        print(j)