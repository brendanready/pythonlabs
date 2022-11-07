#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Brendan Ready
# Module 3 Assignment

# 2. What is the output of the code below? Could you explain what happened?

letter = "Hizthere,zThisziszhowzazpasszstatementzworks!"
for i in letter:
    if i == "mn":
        pass
    elif i == "z":
        print(" ",end="")
    else:
        print(i, end="")

print('\n\nThe code loops through every character in a string.')
print('If the condition i == "mn" is true, the code will do nothing and pass to the next statement of the loop.')
print('If the condition i == "z" is true, a blank space will replace the character "z" and be inserted into the print statement.')
print('The final part of the loop runs an else statement that prints the next character in the string.')


# In[ ]:




