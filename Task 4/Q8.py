#!/usr/bin/env python
# coding: utf-8

# In[3]:


def square(n):
    square_list=[]
    for i in range(1,n+1):
        square_list.append(i*i)
    print(tuple(square_list))


# In[10]:


square(20)

