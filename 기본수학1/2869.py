# 백준 2869번 달팽이는 올라가고 싶다 브론즈1
# 달팽이의 움직임을 계산하는 문제

A, B, V = map(int, input().split())
count = (V - A) // (A - B)
mod = (V - A) % (A - B)
if mod == 0:
    result = count + 1
else:
    result = count + 2
print(result)

# 위와 같이 작성했지만 분수라는 관점의 풀이가 있었음
# 그리고 마지막 부분을 난 올라간 A를 뺏지만 B를 빼면 계산이 더 수월함
# A, B, V = map(int, input().split())
# count = (V - B) / (A - B)
# print(count) if count == int(count) else print(int(count) + 1)
# 코드는 잘 돌아가는데 백준에서 틀렸다고 함 왜인지 이유는 아직 모르겠음
# 답으로 소수점으로 나오는데 그게 문제인 것인가 라는 생각을 해봄



# A = 100,  B = 1, V = 1000000000
# 1000000000 - 100 // 99
# 1000000000 - 100 % 99 + 2  

# A = 100,  B = 99, V = 1000000000
# 1000000000 - 100 // 99
# 1000000000 - 100 % 99 + 1