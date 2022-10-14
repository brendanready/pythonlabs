#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Brendan Ready
# Module 4 Assignment

# 5. Final velocity (v) of an object equals initial velocity (u) of that object plus acceleration (a) of the object times the elapsed time (t) from u to v.
#       v = u + a * t

# a. Create a function which returns the elapsed time using the arguments v, u, and a.
#    Calculate the elapsed time from when the ball is dropped till it hits the ground (1 decimal place)?
#    Use standard gravity as 9.8 m/s2.

from math import sqrt

def velocityFinal(u, a, d):
    return round(sqrt((u**2) + (2 * a * d)), 1)

def elapsedTime(v, u, a):
    return round((v - u) / a, 1)

v = velocityFinal(0, 9.8, 51)
t = elapsedTime(v, 0, 9.8)

print('The elapsed time from when the ball is dropped till it hits the ground is:')
print(t, 'seconds')


# In[ ]:




