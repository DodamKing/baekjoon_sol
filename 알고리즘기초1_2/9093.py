# 단어 뒤집기 브로즌1

import sys
t = int(input())
sentence = []
for _ in range(t):
    sentence.append(sys.stdin.readline().split())
for i in sentence:
    for j in range(len(i)):
        i[j] = i[j][::-1]
for k in sentence:
    print(' '.join(k))