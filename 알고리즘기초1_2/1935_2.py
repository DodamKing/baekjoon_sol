n = int(input())
numbers = []
f_list = []
stk = []
formula = input()
for _ in range(len(formula)):
    f_list.append(formula[_])
for _ in range(n):
   numbers.append(input())

for i in f_list:
    if ord('A') <= ord(i) <= ord('Z'):
        stk.append(str(numbers[ord(i) - ord('A')]))
    else:
        num2 = stk.pop()
        num1 = stk.pop()
        stk.append(str(eval(num1 + i + num2)))
print('{:.2f}'.format(float(stk[0])))