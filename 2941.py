# 크로아티아 알파벳 실버5
# 크로아티아 알파벳의 개수를 세는 문제

word = input()
A = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in A:
    word = word.replace(i, 'a')
print(len(word))