#!/usr/bin/env python
# coding: utf-8

# In[ ]:


string = input("Enter any string:")
res = string.split('_')
res.sort()
result = res[0]
for i in range(1,len(res)):
    result = result + "_" + res[i]
print(result)

