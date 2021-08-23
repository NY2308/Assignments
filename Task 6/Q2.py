#!/usr/bin/env python
# coding: utf-8

# In[8]:


#using zip function
students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']
d1 = dict(zip(students,subjects))
print(d1)


# In[10]:


#using for loop
result = {}
for x in students:
    for y in subjects:
        res[x] = y
        subjects.remove(y)
        break
print(str(res))


# In[13]:


#using dictionary comprehension
d2 = {key:value for (key,value) in zip(students,subjects)}
print(str(d2))

