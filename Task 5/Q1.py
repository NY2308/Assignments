

# In[2]:


def error():
    try:
        eval('a===b')
    except SyntaxError:
        print("There is syntax error")
error()

