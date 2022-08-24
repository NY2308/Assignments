#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Q1
x = 'yash'
y = x.replace('y','Y')
print(y)


# In[ ]:


#Q2
x = 'My name is yash navdiwala'
print(x.count('a'))


# In[ ]:


#Q3
str1 = input("First String: ")
str2 = input("Second String: ")

if(sorted(str1)==sorted(str2)):
    print("Both strings are anagram")
else:
    print("Not Anagram")


# In[ ]:


#Q4
z = input("Enter a string: ")
if (z == z[::-1]):
    print("Palindrome")
else:
    print("Not Palindrome")


# In[4]:


#Q5
ch = input("Enter character: ")
if (ch = 'A' or ch = 'E' or ch = 'I' or ch = 'O' or ch = 'U' or ch = 'a' or ch = 'e' or ch = 'i' or ch = 'o' or ch = 'u'):
    print('Its a vowel')
else:
    print('Its a constant ')


# In[ ]:


#Q6 & Q7
ch = input("Enter character: ")
if(ch.isdigit()):
    print("Its a digit")
else:
    print("Its not digit")


# In[2]:


#Q8 & Q9
string = "My name is yash navdiwala";  
ch = '-';  
string = string.replace(' ', ch);  
   
print(string);  


# In[1]:


#Q10
s1 = input("Enter your Text : ")
s2 = s1.upper()
print(s2)


# In[2]:


#Q11
s1 = input("Enter your Text : ")
s2 = s1.lower()
print(s2)


# In[3]:


#Q12
arr = [1,2,3,4,5,6,7,9,10]
missing_elements = []
for ele in range(arr[0], arr[-1]+1):
    if ele not in arr:
        missing_elements.append(ele)
print(missing_elements)


# In[4]:


#Q13
arr = [1, 2, 3, 4, 2, 7, 8, 8, 3];     
     
print("Duplicate elements in array: ");    
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] == arr[j]):    
            print(arr[j]);    


# In[ ]:


#Q14


# In[5]:


#Q15
arr1=[1,2,3,4,5]
arr2=[1,3,4,5,7]
if len(arr1) == len(arr2):
    print("array is equal")
else:
    print("array is not equal") 


# In[7]:


#Q16
arr1=[1,2,3,4,5]
print(max(arr1))
print(min(arr1))


# In[10]:


#Q17
arr1 = [10, 20, 4, 45, 99]
print(sorted(arr1)[-2])


# In[ ]:


#Q18 & Q20


# In[11]:


#Q19
def remove_duplicate(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list


# In[12]:


remove_duplicate([1,2,3,3,2,4,5])


# In[15]:


#Q21
arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
reverse_arr = x[::-1]
print(reverse_arr)


# In[22]:


#Q22
arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
arr1.reverse()
print('Reverse array :', arr1)


# In[25]:


#Q23
arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(len(arr1))


# In[26]:


#Q24
my_input = ['orange','yellow']
my_input.append('green')
print(my_input)


# In[ ]:




