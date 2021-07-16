A = int(input())
B = int(input())
C = int(input())
D = list(map(int,str(A * B * C))) # 각 자리수를 리스트에 담기

for i in range(10):
    print(D.count(i)) # D 리스트의 i요소의 갯수