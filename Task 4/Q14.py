#!/usr/bin/env python
# coding: utf-8

# In[5]:


def division(n):
    res = []
    for i in range(len(n)):
        if (i % 3 != 0) & (i % 7 == 0):
            res.append(i)
    return res

n = input("Enter a range:")
list1 = range(1, int(n))
x = (list(division(list1)))
print(x)

