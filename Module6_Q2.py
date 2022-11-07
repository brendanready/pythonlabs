#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Brendan Ready
# Module 6 Assignment

# 2. Take the following Python code that stores a string: str = 'inet addr:127.0.0.1  Mask:255.0.0.0'. 
# Use find and string slicing to extract the portion of the string after the colon inet address character
# and then use the rstrip function to remove any trailing characters.

str = 'inet addr:127.0.0.1  Mask:255.0.0.0'

string_1 = str[slice(str.find(":")+1,-1)]
trailing_char = string_1.find(" ")
address = string_1[:trailing_char].rstrip()
print(address)


# In[2]:


str = 'inet addr:127.0.0.1  Mask:255.0.0.0'

string_1 = str[slice(str.find(":")+1,-14)]
print(string_1)


# In[ ]:




