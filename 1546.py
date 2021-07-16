N = int(input())
a = list(map(int, input().split()))
M = max(a)
aver = sum(a) / len(a) # 평균

result = aver / M * 100

print(round(result, 6))

# 넘파이 공부 하자