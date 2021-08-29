# 큐 실버4

import sys

queue = []

def push(x):
    queue.append(x)

def pop():
    if queue == []: print(-1)
    else: print(queue.pop(0))

def size():
    print(len(queue))

def empty():
    if queue == []: print(1)
    else: print(0)

def front():
    if queue == []: print(-1)
    else: print(queue[0])

def back():
    if queue == []: print(-1)
    else: print(queue[-1])

n = int(sys.stdin.readline())
for _ in range(n):
    comm = sys.stdin.readline().split()

    if comm[0] == 'push': push(comm[1])
    elif comm[0] == 'pop': pop()
    elif comm[0] == 'size': size()
    elif comm[0] == 'empty': empty()
    elif comm[0] == 'front': front()
    elif comm[0] == 'back': back()
