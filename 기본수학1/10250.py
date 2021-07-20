# 백준 10250번 ACM호텔 브론즈3
# 호텔 방 번호의 규칙을 찾아 출력하는 문제

T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    a = N % H
    b = N // H + 1
    if N % H != 0:
        print('%d%02d' % (a, b))
    else:
        print('%d%02d' % (H, b - 1))  
# %02d == 공백 0으로 채우기, 자릿수 2자리, d는 십진수

## 처음에는 이프문을 작성하지 않아서 틀렸다. N번째 손님을 층수로 나누었을때
# 나머지가 0인 경우를 따로 생각하지 않아서 한참 고생했다