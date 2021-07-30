#!/usr/bin/env python
# coding: utf-8

# # 백준 4513
# ## 직각삼각형
# ### 피타고라스의 정리에 대해 배우는 문제

# In[4]:


while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    else:
        side = [a, b, c]
        hyp = max(side)
        side.remove(hyp)
        if hyp ** 2 == side[0] ** 2 + side[1] ** 2:
            print('right')
        else:
            print('wrong')


# In[5]:


while True:
    side = list(map(int, input().split()))
    if sum(side) == 0:
        break
    else:
        hyp = max(side)
        side.remove(hyp)
        if hyp ** 2 == side[0] ** 2 + side[1] ** 2:
            print('right')
        else:
            print('wrong')


# In[ ]:




