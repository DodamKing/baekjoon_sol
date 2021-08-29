# 요세푸스 문제 실버5
 
n, k = map(int, input().split())

stk = [i for i in range(1, n+1)]
res_list = []

j = k - 1
l = len(stk) - 1
while l >= 0:
    if j <= l:
        res_list.append(str(stk.pop(j)) )
        # print(stk.pop(j))
        l -= 1
    else:
        while j > l: 
            j = j - l - 1
        res_list.append(str(stk.pop(j)))
        # print(stk.pop(j))
        l -= 1
    j += k - 1
    # print(stk)
    # print(j, l)
print('<' + ', '.join(res_list) + '>')