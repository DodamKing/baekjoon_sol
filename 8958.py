T = int(input())

for i in range(T):
    score = 0
    a = 1
    case = list(str(input())) 
    for j in case:
       if j == 'O':
           score = score + a
           a = a + 1
       else:
           a = 1
    print(score)        