#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Brendan Ready
# Module 5 Assignment

# 1. What is the Base Case in Recursion?

print("The base case in recursion is a way to stop the process of making resursive calls.")
print("It is the first condition that doesn't return any resursive calls, and makes the recurion stop.")
print("A proper recursive function should always have a base case.")
print("We should make sure that every function call eventually reaches the base case to avoid infinite recursion.\n")
print('For example, the base case used in this countdown function is the condition "if number >= 0".')
print('When number reaches 0, the countdown stops.\n')

def countdown(number):
    if number >= 0:
        print(number)
        return countdown(number-1)

countdown(10)


# In[ ]:




