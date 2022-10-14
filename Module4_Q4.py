#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Brendan Ready
# Module 4 Assignment

# 4. The third equation of motion gives the final velocity of an object under uniform acceleration given the distance traveled and an initial velocity:
#       v^2=vo^2+2ad

# a. Using the equation above, build a function called (velocityFinal) which returns the final velocity of the object rounded to one decimal place. 
#    Use the following parameters:
#       u or vo (initial velocity) 
#       a (uniform acceleration) 
#       d (distance traveled)

from math import sqrt

def velocityFinal(u, a, d):
    return round(sqrt((u**2) + (2 * a * d)), 1)

# b. A ball is gently dropped from a height of 51m (167 ft), the acceleration due to gravity is a constant 9.8 m/s2. 
#    Using the arguments described and function you built above, what is the calling expression to determine the final velocity before impact?

velocityFinal(0, 9.8, 51)

# c. Based on the function you created , calculate the speed of the ball before it strikes the ground?
#    Answer should be in m/s.

v = velocityFinal(0, 9.8, 51)

print('The speed of the ball before it strikes the ground is:')
print(v, 'm/s')


# In[ ]:




