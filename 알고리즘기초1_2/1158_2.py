n, k = map(int, input().split())

stk = [i for i in range(1, n+1)]
res_list = []

num = 0  #제거될 사람 인덱스

for _ in range(n):
   num += k - 1
   if num >= len(stk): # 한바퀴가 넘어갈 때를 계산
       num = num % len(stk)
   res_list.append(str(stk.pop(num)))

print('<' + ', '.join(res_list) + '>')