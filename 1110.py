N = int(input())
chek = N # 입력 받은 값을 체크포인트에 저장
i = 0
M = 0

while True:
        a = N // 10     # 입력받은 값의 십의 자리
        b = N % 10      # 입력받은 값의 일의 자리
        c = a + b 
        d = c % 10      # 합한 값의 일의자리
        M = b * 10 + d  # 새로운 수
        N = M           # while문에 넣기 위한 N 세팅
        i = i + 1
        
        if N == chek:
            break
            
print(i)  