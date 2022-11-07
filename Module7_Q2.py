#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Brendan Ready
# Module 7 Assignment

# 2. The data type integer signed range is from -2,147,483,648 to 2,147,483,648 (4 bytes). 
# Write a program that determines the range of numbers for an integer based on the number of bytes it can encode (Hint integral type with n bits can encode 2^n numbers).

# Console:
# Enter number of Bytes you would like to determine the signed range of: 4
# 4 Byte(s) integral type with 8 bits can encode 4,294,967,296 numbers. The signed range will be from -2,147,483,648 to 2,147,483,647

initial_bytes = int(input("Enter number of Bytes you would like to determine the signed range of: "))

total_range = 2**(initial_bytes*8)

print(f"{initial_bytes} Byte(s) integral type with 8 bits can encode {total_range:,} numbers. The signed range will be from {total_range/2*-1:,.0f} to {total_range/2-1:,.0f}")


# In[ ]:




