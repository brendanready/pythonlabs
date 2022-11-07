#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Brendan Ready
# Module 6 Assignment

# 5. Write a Python script that takes input from the user and displays that input back in upper and lower cases.

#Console Output
# What is your first name? alison
# What is your last name? smith
# Hi Alison Smith, welcome to my python greet application!

first_name = input('What is your first name? ')
last_name = input('What is your last name? ')

full_name = first_name.capitalize() + ' ' + last_name.capitalize()
print(f"Hi {full_name}, welcome to my python greet application!")


# In[ ]:




