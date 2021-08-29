# 에디터 실버3 시간초과
import sys

init = sys.stdin.readline().strip()
n = int(input())
i = len(init) - 1

# print(i)

for _ in range(n):
    comm = input()
    if comm == "L":
        i -= 1
        if i < 0: i = 0
        # print(i)
    elif comm == "D":
        if i == -1: i = 0
        i += 1 
        if i > len(init): i = len(init) - 1
        # print(i)
    elif comm =="B":
        if i >= 0:
            init = init.replace(init[i], "", 1)
            i -= 1
        # print(i, init)
    elif "P" in comm:
        if i == -1: i = 0
        if i == 0:
            init = init.replace(init[i], comm[2] + init[i], 1)
        else:
            init = init.replace(init[i], init[i] + comm[2], 1)
        i += 1
        # print(i, init)
print(init)
