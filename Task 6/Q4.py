#!/usr/bin/env python
# coding: utf-8

# In[3]:


string ="Consultadd Training"
def reverse(string):
    for i in range(len(string)-1, -1, -1):
        yield string[i]

a = reverse(string)
print(a.__next__())
print(a.__next__())
print(a.__next__())

for i in a:
    print(i)

