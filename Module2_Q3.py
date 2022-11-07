#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Brendan Ready
# Module 2 Assignment

weight_on_earth = float(input('Please enter the mass in lb that you would like to convert to kg: '))

# a. convert weight_on_earth to kg
weight_on_earth_in_kg = weight_on_earth/2.20462
print('The converted mass in kg is:', str(weight_on_earth_in_kg))

# b. convert the weight of the mass (on Earth) to Newtons
weight_on_earth_in_newtons = weight_on_earth_in_kg * 9.807
print('Your weight on Earth is:', str(weight_on_earth_in_newtons), 'Newtons')

# c. calculate weight of mass on moon in Newtons
weight_on_moon_in_newtons = weight_on_earth_in_kg * 1.62
print('Your weight on the Moon is:', str(weight_on_moon_in_newtons), 'Newtons')

# d. calculate percentage of weight on the Moon in comparison to what is experienced on Earth
percent_weight_on_moon_vs_earth = weight_on_moon_in_newtons/weight_on_earth_in_newtons * 100
print('The percentage of the weight on the Moon in comparison to what is experienced on Earth:', str(percent_weight_on_moon_vs_earth), '%')

# e. calculate the percentage of the weight on the moon in comparison to what is experienced on Earth as an integer
percent_weight_on_moon_vs_earth_as_integer = round(percent_weight_on_moon_vs_earth)
print('The percentage of the weight on the Moon in comparison to what is experienced on Earth as an integer is', str(percent_weight_on_moon_vs_earth_as_integer), '%')


# In[ ]:




