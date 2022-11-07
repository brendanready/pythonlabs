#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Brendan Ready
# Module 5 Assignment

# 3. Write a recursive Python function that returns the sum of the first n integers.
#   (Hint: The function will be similar to the factorial function!) ie sum_nint(3) = 1 + 2 + 3 = 6 , sum_nint(4) = 1 + 2 + 3 + 4 = 10.

def sum_nint(n):
    if n == 1:
        return n
    else:
        return n + sum_nint(n - 1)

print('The sum of the first 3 integers is', sum_nint(3))
print('The sum of the first 4 integers is', sum_nint(4))


# In[ ]:




