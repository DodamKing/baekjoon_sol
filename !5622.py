# 다이얼
# 규칙에 따라 문자에 대응하는 수를 출력하는 문제
## 못품 ㅠㅠ

A = ['ABC', 'DEF', 'GHI','JKL', 'MNO', 'PQRS', 'TUV','WXYZ'] 
word =  input()
time = 0
for a in A:
    for b in a:
        for c in word:
            if c == b:
                time = time + A.index(a) + 3

print(time)
