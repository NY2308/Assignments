#!/usr/bin/env python
# coding: utf-8

# In[5]:


def divide(x):
    try:
       n = x/0
    except ZeroDivisionError:
        print("Divisor can not be zero")
    finally:
        print("Execution completed")


# In[4]:


divide(5)

