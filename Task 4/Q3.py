#!/usr/bin/env python
# coding: utf-8

# In[9]:


def unique(x):
    new_list = []
    for i in x:
        if i not in new_list:
            new_list.append(i)
    print(new_list)      
