#!/usr/bin/env python
# coding: utf-8

# In[7]:


seq = range(1,21)
list1 = filter(lambda x: x % 2 == 0, seq)
print(list(list1))

