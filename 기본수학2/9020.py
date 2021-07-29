#!/usr/bin/env python
# coding: utf-8

# # 백준 9020번
# ## 골드바흐의 추측 실버1
# ### 소수 응용 문제 2

# In[27]:


import random

T = int(input()) # 테스트 케이스

for i in range(T):
    n = int(input())

    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
      if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
            
    while True:
        random.shuffle(primes)
        if primes[0] + primes[1] == n:
            primes = primes[:2]
            primes.sort()
            print(primes)
            break


# In[28]:


from itertools import combinations_with_replacement

T = int(input())

for i in range(T):
    n = int(input())

    a = [True]*n
    m =  int(n ** 0.5)
    for i in range(2, m+1):
      if a[i] == True:
        for j in range(i+i, n, i):
            a[j] = False
    primes = [i for i in range(2, n) if a[i] == True]
  
        
    comb_list = list(combinations_with_replacement(primes, 2))
    gold_list = []
    for i in comb_list:
        if sum(i) == n:
            gold_list.append(i)
            answer = gold_list[-1]
    if n >= 4:
        print(gold_list)
        print('{} {}'.format(answer[0], answer[1]))


# In[ ]:





# In[54]:


def sosu(x):
    m = int(x**0.5)

    p_list = [False,False] + [True]*(x-1)

    for i in range(m+1):
        if p_list[i] == True:
            for j in range(i+i, x+1, i):
                p_list[j] = False
    return p_list[x]
                
T = int(input())
gold_list = []
    
for i in range(T):
    n = int(input())
   
    for i in range(n):
        p = n - i
        if sosu(i) == True and sosu(p) == True and p - i >= 0:
            gold_list.append((i, p))
            answer = gold_list[-1]
    print('{} {}'.format(answer[0], answer[1]))


# In[65]:


def prime(x): # 소수 리스트 작성 에라토스테네스의 체
    a = [True] * x
    m = int(x ** 0.5)
    for i in range(2, m + 1):
        if a[i] == True:
            for j in range(i+i, x, i):
                a[j] = False
    return [i for i in range(2, x) if a[i]==True]


# In[68]:


def gold(x): # 합이 입력값과 같아지는 소수 찾기
    p_list = prime(x)
    middle = max([i for i in range(len(p_list)) if p_list[i] <= x/2]) # 두 수의 차가 가장 작아야 하므로 중앙에서 부터 찾는다
    for i in range(middle, -1, -1): # 중앙에서 거꾸로 작아지면서
        for j in range(i, len(p_list)): # 중앙에서 커지면서
            if p_list[i] + p_list[j] == x: # 합이 x가 되는
                return [p_list[i], p_list[j]]


# In[71]:


T = int(input())
for i in range(T):
    n = int(input())
    answer = gold(n)
    print('{} {}'.format(answer[0], answer[1]))


# In[ ]:





# In[ ]:




