#!/usr/bin/env python
# coding: utf-8

# In[1]:


# # Brendan Ready
# Module 5 Assignment

# 8. The Doubling Time formula below is used in Finance to calculate the length of time required to double an investment or money in an interest bearing account.
# DoublingTime = log(2) / log(1 + r)
# r = rate of return

# If one wishes to calculate the amount of time to double their money in a money market account that is compounded monthly, 
# then r needs to express the monthly rate and not the annual rate. The monthly rate can be found by dividing the annual rate by 12. 
# With this situation, the doubling time formula will give the number of months that it takes to double money and not years 
# (Please use monthly rate for 8a - 8c)

# a. Marc wants to determine how long it would take to double the money in his money market account in BMO Harris Bank in 2020. 
#    BMO offers a 1.85% APR, which is compounded monthly.  
#    How long would it take Marc to double his money by investing with BMO? Please round to 1 decimal place.

from math import log, log10

def doubling_time(r):
    return  round(log(2) / log(1 + r), 1)

apr = 1.85
monthly_rate = (apr/100)/12

print(doubling_time(monthly_rate), 'months')


# In[2]:


# b. Write a lambda function (doubling_time_yrs) that returns the time it will take to double his money in years.
#    Use math.log10(a) to get the base-10 logarithm of a number in the formula.

doubling_time_yrs = lambda r: round((log10(2) / log10(1 + r)) / 12, 1)

print(doubling_time_yrs(monthly_rate), 'years')


# In[3]:


# c. According to your ACME broker The 10-year average annual return on the S&P 500, ending in 2018 and including dividends, is around 10%. 
#    However your ACME broker is recommending that you open a money market account since stock market volatility is high (understanding you will experience down years as well as up years - no guarantees). 
#    How long would it take Marc to double his money if he invests in a money market account that will compound monthly and earn him 3% per year? (round to 1 decimal place)

apr = 3
monthly_rate = (apr/100)/12

print(doubling_time(monthly_rate), 'months')
print('or')
print(doubling_time_yrs(monthly_rate), 'years')


# In[ ]:




