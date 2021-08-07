# 백준 1018 체스판 다시 칠하기
# 체스판을 만드는 모든 경우를 시도하여 최적의 방법을 찾는 문제

# N, M = map(int, input().split())
N = 10
M = 13
cnt1 = 0
cnt2 = 0
bord = []

for i in range(N):
    line_list =[]
    line = input()
    for j in line:
        line_list.append(j)
    bord.append(line_list)

## 시작이 W 일 때
# 세로줄 검사


# bord1 = bord # W로 시작
# if bord1[0][0] == 'B': 
#     bord1[0][0] = 'W'
#     cnt1 += 1
# for k in range(N-1):
#     if bord1[k][0] == bord1[k+1][0] == 'W':
#         bord1[k+1][0] = 'B'
#         cnt1 += 1
#     elif bord1[k][0] == bord1[k+1][0] == 'B':
#         bord1[k+1][0] = 'W'
#         cnt1 += 1
# print(cnt1)
# print(bord1)

# # 가로줄 검사
# for i in bord1: 
#     for j in range(M-1):
#         if i[j] == i[j+1] == 'B':
#             i[j+1] = 'W'
#             cnt1 += 1
#         elif i[j] == i[j+1] == 'W':
#             i[j+1] = 'B'
#             cnt1 += 1
# print(cnt1)
# print(bord1)

# ## 시작이 B 일 때
# # 세로줄 검사
# bord2 = bord # B로 시작
# if bord2[0][0] == 'W': 
#     bord2[0][0] = 'B'
#     cnt2 += 1
# for k in range(N-1):
#     if bord2[k][0] == bord2[k+1][0] == 'W':
#         bord2[k+1][0] = 'B'
#         cnt2 += 1
#     elif bord2[k][0] == bord2[k+1][0] == 'B':
#         bord2[k+1][0] = 'W'
#         cnt2 += 1       
# print(cnt2)
# print(bord2)

# # 가로줄 검사
# for i in bord2: 
#     for j in range(M-1):
#         if i[j] == i[j+1] == 'B':
#             i[j+1] = 'W'
#             cnt2 += 1
#         elif i[j] == i[j+1] == 'W':
#             i[j+1] = 'B'
#             cnt2 += 1
# print(cnt2)
# print(bord2)

# count = min([cnt1, cnt2])
# print(count)