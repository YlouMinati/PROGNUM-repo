#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Sirius data
apparentMagnitude = -1.46
absoluteMagnitude = 1.45

#apparantMagnitude=m
#absoluteMagnitude=M

m=float(input("the apparantMagnitude is: "))
M=float(input("the absoluteMagnitude is: ")) 


d = 10.0 * pow( 10.0, (m-M)/5.0 ) * 3.26164 

print(d)

