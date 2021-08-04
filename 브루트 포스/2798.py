# 백준 2798 블랙잭 브론즈2
# 세 장의 카드를 고르는 모든 경우를 고려하는 문제

from itertools import combinations

N, M = map(int, input().split())

number_list = list(map(int, input().split()))

combi_list = list(combinations(number_list, 3))

hap_list = []
for i in combi_list:
    if sum(i) <= M:
        hap_list.append(sum(i))

print(max(hap_list))