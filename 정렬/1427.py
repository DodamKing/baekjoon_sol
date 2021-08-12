# 소트인사이드 실버5
# 숫자를 정렬하는 문제

N = input()
li = []

for i in N:
    li.append(i)
li.sort()
li.reverse()
print(''.join(li))
