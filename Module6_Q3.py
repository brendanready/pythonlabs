#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Brendan Ready
# Module 6 Assignment

# 3a. Using a for loop through a string, count the number of internet addresses in the string below by using the split method.

# Line 1      str = \
# Line 2      '''
# Line 3      inet addr :127.0.0.1 Mask:255.0.0.0
# Line 4      inet addr :127.0.0.2 Mask:255.0.0.0

# Line 5      inet addr :127.0.0.3 Mask:255.0.0.0
# Line 6      inet addr :127.0.0.4 Mask:255.0.0.0
# Line 7      '''

# 3b. Use the count() method to return the number of occurrences of the substring in the given string.

str = '''
inet addr :127.0.0.1 Mask:255.0.0.0
inet addr :127.0.0.2 Mask:255.0.0.0
inet addr :127.0.0.3 Mask:255.0.0.0
inet addr :127.0.0.4 Mask:255.0.0.0
'''

list = str.split('\n')

count = 0

for i in list:
    count += i.count('inet addr')

print(f"There are {count} internet addresses in the string")


# In[ ]:




