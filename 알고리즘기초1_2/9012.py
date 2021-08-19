# 괄호 실버4

t = int(input())
for _ in range(t):
    test_data = input()
    while True:
        if '()' in test_data:
            test_data = test_data.replace('()', '')
        else :
            break
    # print(test_data)
    if len(test_data) == 0:
        print('YES')
    else:
        print('NO')