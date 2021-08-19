#!/usr/bin/env python
# coding: utf-8

# In[2]:


a= input('Enter the first string:')
b=input('Enter the second string:')

def  max_length(a,b):
    if len(a)== len(b):
        print(a, b, sep='\n')
    elif len(a) > len(b):
        print(a)
    else:
        print(b)

max_length(a,b)

