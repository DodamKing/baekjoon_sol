# 손익분기점 브론즈4
# 이익이 발생하는 지점을 찾는 문제

A, B, C = map(int, input().split())
if C <= B:
    print(-1)
else:
    print(int((A/(C-B)))+1)    