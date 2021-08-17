#!/usr/bin/env python
# coding: utf-8

# In[2]:


def get_sum(list1):
    return sum(list1)


# In[14]:


def get_multiply(list1):
    temp = 1
    for i in list1:
       temp *= i
    return temp
        


# In[18]:


list1 = [1, 2, 3, 4, 6]
print("Sum of list is:",get_sum(list1))
print("Multiplication of list is:",get_multiply(list1))


# In[ ]:





# In[ ]:




