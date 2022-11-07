#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Brendan Ready
# Module 5 Assignment

# 2. In mathematics, the factorial of a number n is defined as n! = 1 ⋅ 2 ⋅ ... ⋅ n (as the product of all integer numbers from 1 to n). 
# For example, 4! = 1 ⋅ 2 ⋅ 3 ⋅ 4 = 24. Write a recursive function for calculating n! 

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)

print('The factorial of 4 is', factorial(4))


# In[ ]:




