# 소트인사이드 실버5
# 숫자를 정렬하는 문제

N = input()
li = []

for i in N:
    li.append(i)
li.sort()
li.reverse()
print(''.join(li)) # 구분자.join(리스트)
