# 벌집 브론즈2
# 벌집이 형성되는 규칙에 따라 벌집의 위치를 구하는 문제

N = int(input())
time = 1
count = 1 
while N > time:
    time = time + count * 6
    count = count + 1
print(count)
