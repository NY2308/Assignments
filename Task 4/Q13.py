#!/usr/bin/env python
# coding: utf-8

# In[2]:


from functools import reduce
list1 = [1,2,3,4,5,6,7]
list_flatten = reduce(lambda total, i: 10 * total + i, list1)
print(list_flatten)

