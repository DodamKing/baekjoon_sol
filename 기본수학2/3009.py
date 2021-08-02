#!/usr/bin/env python
# coding: utf-8

# # 백준 3009번
# ## 네 번째 점 브론즈2
# ### 직사각형을 완성하는 문제

# In[2]:


x1, y1 = map(int, (input().split()))
x2, y2 = map(int, (input().split()))
x3, y3 = map(int, (input().split()))

if x1 == x2:
    a = x3
elif x1 == x3:
    a = x2
else: 
    a = x1
    
if y1 == y2:
    b = x3
elif y1 == y3:
    b = y2
else: 
    b = y1
    
print(a, b)


# In[4]:


x_list = []
y_list = []

for i in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
    
for j in range(3):
    if x_list.count(x_list[j]) == 1:
        a = x_list[j]
    if y_list.count(y_list[j]) == 1:
        b = y_list[j]
        
print(a, b)


# In[ ]:





# In[ ]:




