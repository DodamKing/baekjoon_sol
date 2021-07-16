import string
allphabet = string.ascii_lowercase #알파벳 소문자 (a ~ z)

S = str(input())

for i in allphabet:
    print(S.find(i), end=' ')

#아스키코드를 활용하는 방법도 있음