# 백준 1018 체스판 다시 칠하기
# 체스판을 만드는 모든 경우를 시도하여 최적의 방법을 찾는 문제

N, M = map(int, input().split())
board = []
count = []
for i in range(N):
    board.append(list(input()))

for x in range(N-8+1): # 세로의 크기가 8이 되도록 자르는 경우의 수
    for y in range(M-8+1): # 가로의 크기가 8이 되도록 자르는 경우의 수
        start_W = 0 # W로 시작
        start_B = 0 # B로 시작
        for j in range(x, x+8): # row * 8
            for k in range(y, y+8): # column * 8
                if (j + k) % 2 == 0: # 행렬의 합이 짝수인 경우 = 색이 같은 대각선
                    # 맨 왼쪽 위칸이 W이면 행렬의 합이 짝수인 경우(대각선)은 모두 색이 W
                    if board[j][k] == 'B': # W로 시작하는 경우 B이면 W로 바꿔야 함
                        start_W += 1 # 색을 바꾸면 카운트
                    if board[j][k] == 'W': # B로 시작하는 경우 W이면 B로 바꿔야 함
                        start_B += 1 # 색을 바꾸면 카운트
                else: # 위와 색이 다른 대각선
                    if board[j][k] == 'W': # W로 시작, 색이 다른 대각선이므로 여기는 B이어야 함
                        start_W += 1 # W면 B로 바꿔야 하고 W로 시작하는 경우 카운트
                    if board[j][k] == 'B': # B로 시작, W 여야함
                        start_B += 1 # B이면 W로 바꿔야 하고 B로 시작하는 경우 카운트
        count.append(min([start_W, start_B]))
print(min(count))
