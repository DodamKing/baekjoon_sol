# 스택 실버4

import sys
stack = []
n = int(sys.stdin.readline())
for _ in range(n):
    command = sys.stdin.readline().split()
    if 'push' in command:
        stack.append(command[1])
    elif 'pop' in command:
        if stack == []:
            print(-1)
        else:
            x = stack.pop(-1)
            print(x)
    elif 'size' in command:
        print(len(stack))
    elif 'empty' in command:
        if stack == []:
            print(1)
        else:
            print(0)
    elif 'top' in command:
        if stack == []:
            print(-1)
        else:
            print(stack[-1])
