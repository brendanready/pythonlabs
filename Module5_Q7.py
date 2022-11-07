#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Brendan Ready
# Module 5 Assignment

# 7. Write a lambda function (area_circle_lambda) that returns the area of a circle of a given radius.

from math import pi

area_circle_lambda = lambda radius : pi * (radius ** 2)

print('The area of a circle with a radius of 4 units is:', area_circle_lambda(4))
print('The area of a circle with a radius of 8 units is:', area_circle_lambda(8))


# In[ ]:




