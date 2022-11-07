#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Brendan Ready
# Module 5 Assignment

# 4. Explain what happens when the following recursive functions is called with the value “alucard” and 0 as arguments:

# Line 1      def semordnilap(aString,index):
# Line 2              if index < len(aString):
# Line 3                   semordnilap(aString, index +1)
# Line 4                    print(aString[index]), end="")

'''
def semordnilap(aString,index):
    if index < len(aString):
        semordnilap(aString, index +1)
        print(aString[index]), end="")
        
semordnilap("alucard", 0)
'''

print('Note the recursive function in the assignment throws a syntax error due to an unmatched parenthesis in the print statement.')
print('The extra parenthesis must be removed for the recursive function to execute.\n')

def semordnilap(aString,index):
    if index < len(aString):
        semordnilap(aString, index +1)
        print(aString[index], end="")

semordnilap("alucard", 0)

print('\n\nThe recursive function prints the string "dracula", which is the palindrome of "alucard".')
print('It prints the text string in its argument backwards.')
print('The other argument the recursive function takes is an index, which is the position it starts printing at in the text string.')
print('The recursive function loops through and prints each letter in the string, starting at the first letter of the text string.')
print('When the index equals the length of the string, the recursive function will stop executing.')
print('So the recursive function will first print the first letter in the string (a), then the next letter (l), until it reaches the end of the string (d).')


# In[ ]:




