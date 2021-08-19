#!/usr/bin/env python
# coding: utf-8

# In[10]:


def showNumbers(limit):
    for i in range(limit+1):
        if i%2 == 0:
            print(i,end=' ')
            print("Even")
        else:
            print(i,end=' ')
            print("Odd")


# In[11]:


showNumbers(3)

