#!/usr/bin/env python
# coding: utf-8

# In[3]:


def hello_decorator(func):
    def inner1(*args, **kwargs):
          
        print("before Execution")
        returned_value = func(*args, **kwargs)
        print("after Execution")
        return returned_value
    return inner1
  
  
# adding decorator
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b
  
a, b = 2, 3
print("Sum =", sum_two_numbers(a, b))

