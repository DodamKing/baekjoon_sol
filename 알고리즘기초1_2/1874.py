# 스택 수열 실버3

n = int(input())
number_list = [x for x in range(1, n+1)] # 1부터 순서대로 있는 수열
result_list = [] # 입력된 값을 받을 리스트 결과적으로 우리가 출력해야 할 수열 비교할 값이다
stack = [] 
pm_list = [] # 출력 값을 넣을 리스트 +, -
for _ in range(n):
    result_list.append(int(input()))
i = 0
while i < n:   
    try: 
        if stack == []: # 일단 스택이 비어 있을 꺼니까 하나 넣어준다
            a = number_list.pop(0) # 하나 꺼내서
            stack.append(a) # 스택에 넣고
            pm_list.append('+') # 넣었으니 +
        else:
            if result_list[i] == stack[-1]: # 이제 스택과 결과를 배교해서 같으면
                stack.pop(-1) # 같은 값을 빼내주면 됨
                pm_list.append('-') # 뺏으니까 -
                i += 1 # 그 다음번째 결과값과 비교해야 하니까
            else:
                a = number_list.pop(0) # 스택과 결과가 다를꺼야 그러면 숫자 하나 빼서
                stack.append(a) # 스택에 넣어줘 
                pm_list.append('+') # 넣었으니까 +
    except: # 그런데 오류가 나네
        pm_list = ['NO'] # 그럼 내가 코드를 잘 짯다는 가정하에 넌 안돼는 구나
        break # 출력할 내용을 NO로 바꿔버리자 그리고 반복분 탈출
print('\n'.join(pm_list))   # 출력 형식 맞춰서 출력         
    
            


# 43687521
# 12578643
