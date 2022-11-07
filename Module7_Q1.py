#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Brendan Ready
# Module 7 Assignment

# 1. Write a program to print and insert the value of tau in an available field width space of 8 characters (center aligned), 
# also print and insert the value of ½ tau to determine the value and insert / center align as shown in the first console example below). 
# Console:
# The value of Tau is {}, which is two times {}.

# Example:
# The atomic number of Helium is    2     , which is twice the atomic number of 
# Hydrogen, which has a value of    1    .

from math import tau, pi

print(f"The value of Tau is {tau:^11.2f}, which is two times {pi:^11.2f}.")


# In[ ]:




