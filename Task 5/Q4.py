#!/usr/bin/env python
# coding: utf-8

# In[ ]:


count = 0
while count < 4:
    try:
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        if password == "Password1234" and username == "User1234":
            print("Logged In")
            break
        else:
            count += 1
            raise Exception
    except Exception:
        print("Please try again")

