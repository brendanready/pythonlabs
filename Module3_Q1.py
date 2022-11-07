#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Brendan Ready
# Module 3 Assignment

# 1. What is the difference between “pass” and “continue” in Python?

print("In this example, the pass statement doesn't do anything when i == 5 in the loop's countdown from 10 to 0.\n")
countdown = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

for i in countdown:
    if i == 5:
        pass
    print(i)


# In[2]:


print("In this example, the continue statement skips the iteration when i == 5 in the loop's countdown from 10 to 0.\n")

for i in countdown:
    if i == 5:
        continue
    print(i)


# In[ ]:




