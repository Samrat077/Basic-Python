#!/usr/bin/env python
# coding: utf-8

# print function using parameter

# In[1]:


#print using end
name=input()
print("hi",end=",")
print(name)


# In[2]:


#print using sep
name=input()
print("hi",name,sep=",")


# print quotes

# In[3]:


print('hi,"Seri"')


# In[5]:


print("hi,\"Seri\"")


# Other printing methods

# In[6]:


name="Seri"
print(f"hello,{name}")


# remove space while printing

# In[12]:



name=input()
print(f"hi,{name}")


# In[11]:


name=input()
name=name.strip()
print(f"hi,{name}")


# Playing with str

# In[13]:


name=input()
name=name.capitalize()
print(f"hi,{name}")


# In[14]:


#This looks littel odd so using 
name=input()
name=name.title()
print(f"hi,{name}")


# In[15]:


#channinng the function
name=input()
name=name.strip().title()
print(f"hi,{name}")


# In[16]:


#or you can also do this
name=input().strip().title()
print(f"hi,{name}")


# In[20]:


#or also can be done
print(f'hi,{input().strip().title()}')

