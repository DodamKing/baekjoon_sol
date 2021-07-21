# 백준 2839번 설탕 배달 브론즈1
# 5와 3을 최소 횟수로 합하여 N을 만드는 문제

N = int(input())
if N % 5== 0:
    print(N // 5)
elif N % 5 == 1:
    print((N // 5) + 1)
elif N % 5 == 2:
    if N == 7:
        print(-1)
    else:
        print(N // 5 + 2)
elif N % 5 == 3:
    print(N // 5 + 1)
elif N % 5 == 4:
    if N == 4:
        print(-1)
    else:
        print(N // 5 + 2)

# 나는 5로 나눈 나머지 별로 케이스를 나누고 그에 맞는 계산식을 세웠다
# 예외가 나오는 4와 7에 대해서만 -1을 찍고 나머지는 그대로
# 하지만 더 간략한 코드가 있어 데리고 온다

N = int(input())   
count = 0 
while N >= 0:
    if N % 5 == 0: # 설탕이 5의 배수이면 
        print(N // 5 + count)
        break
    N = N - 3 # 설탕을 3킬로그램 봉지에 
    count = count + 1 # 하나씩 담자
else: # 3킬로그램 봉지에 계속 담아 나갔는데 남은 설탈이 0보다 작아지면 
    print(-1) # 3의 배수가 아니므로 -1을 출력