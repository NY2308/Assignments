#!/usr/bin/env python
# coding: utf-8

# In[4]:


x = int(input("Enter a number:"))
if x%3 == 0 and x%5==0:
    print("Consultadd - Python Training")
elif x%5 == 0:
    print("Python Training")
elif x%3==0:
    print("Consultadd")
else:
    print("Enter valid input number")





