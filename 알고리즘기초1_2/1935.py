# 후위 표기식2

op = ['+', '-', '*', '/']
ap = ['A', 'B', 'C', 'D', 'E', 'F', 
'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
f_list = []
numbers = []
sp = 0

n = int(input())
formula = input()
for i in formula:
    f_list.append(i)

for i in range(n):
    numbers.append(input())

z_dict = dict(zip(ap, numbers))

for i in range(len(f_list)):
    if f_list[i] in ap:
        f_list[i] = z_dict[f_list[i]]

while sp == 0:
    index = len(f_list)
    for i in range(index):
        if f_list[i] in op:
            sp = 0
            f_list[i] = str(eval(f_list[i-2] + f_list[i] + f_list[i-1]))
            f_list.pop(i-2)
            f_list.pop(i-2)
            break
        else:
            sp = 1

print('{:.2f}'.format(float(f_list[0])))