#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Swapping with third variable
a, b = 5 , 7
temp = a
a = b
b = temp
print(a, b)

#Swapping without third variable
a, b = 5, 7
a = a + b
b = a - b
a = a - b
print(a, b)


# In[ ]:




