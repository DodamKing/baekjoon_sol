#!/usr/bin/env python
# coding: utf-8

# # 백준 7568번 덩치 실버5
# ## 모든 사람을 비교하여 덩치 등수를 구하는 문제

# In[95]:


N = int(input())
x_list = []
y_list = []
data = []


# In[96]:


for i in range(N):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
    data.append((x, y))


# In[93]:


print(x_list, y_list)
print(data)


# In[94]:


for i in range(N):
    count = 1
    data2 = data
    print(data)
    print(data2)
    pop = data2.pop(i)
    print(pop)
    print(data2)
    for j in range(N-1):
        if pop[0] <= data2[j][0] and pop[1] <= data2[j][1]:
            count += 1
    print(count)


# In[74]:


# pop으로 시도
# for i in range(N):
#     x_count = 0
#     x_list2 = x_list
#     for j in x_list2:
#         if x_list2.pop(i) <= j:
#             x_count += 1
#     print(x_count)


# In[42]:


print(sorted(x_list))


# In[43]:


print(x_list)


# In[55]:


index_x_list = []
index_y_list = []
for i in x_list:
    index_x_list.append(sorted(x_list).index(i))
for i in y_list:
    index_y_list.append(sorted(y_list).index(i))
print(index_x_list)
print(index_y_list)
for i in range(N):
    if index_x_list[i] <= index_y_list[i]:
        result = index_y_list[i]
    else:
        result = index_x_list[i]
    print(5-result)


# In[103]:


# 정답
N = int(input())
data = []
for i in range(N):
    x, y = map(int, input().split())
    data.append((x, y))
for i in range(N):
    count = 1
    for j in range(N):
        if i != j:
            if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
                count += 1
    print(count, end=' ')


# In[100]:


print(count, end=' ')


# In[ ]:




