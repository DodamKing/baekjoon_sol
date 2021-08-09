# 백준 2751번 수 정렬하기2 실버5
# 시간 복잡도가 O(nlogn)인 정렬 알고리즘으로 풀 수 있습니다. 예를 들면 병합 정렬, 힙 정렬 등이 있지만, 어려운 알고리즘이므로 지금은 언어에 내장된 정렬 함수를 쓰는 것을 추천드립니다.
import sys

N = int(input())

number_list = []
for i in range(N):
    number_list.append(int(sys.stdin.readline()))

for i in sorted(number_list):
    print(i)


## 출력 보정
import sys

N = int(input())

number_list = []
for i in range(N):
    number_list.append(int(sys.stdin.readline()))

for i in sorted(number_list):
    sys.stdout.write(str(i) + '\n')