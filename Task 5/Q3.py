#!/usr/bin/env python
# coding: utf-8

# In[2]:


while True:
    try:
        num1 = input("Enter any number: ")
        if (len(num1) == 4):
            print("Number is four digit only")
            break
    except ValueError:
        print("Enter number with only four digits")

