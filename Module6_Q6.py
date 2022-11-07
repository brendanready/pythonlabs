#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Brendan Ready
# Module 6 Assignment

# 6. Write a program that takes your full name as input and displays the abbreviations of the middle name except the first and last name which is displayed as it is. 
# For example, if your name is Elvis Aaron Presley, then the output should be Elvis A. Presley.

full_name = input('What is your full name? ')

full_name = full_name.split()
print(f"{full_name[0]} {full_name[1][0]}. {full_name[2]}")


# In[ ]:




