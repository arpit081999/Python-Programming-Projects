# -*- coding: utf-8 -*-
"""
@author: Arpit Somani
"""


import random

def evolve(x):
    ind=random.randint(0,len(x)-1)
    p=random.randint(1,100)
    print(p) 
    """
    here,checking if change is taken place.
    it will run for 10,000 times ,each time you encounter with 1,
    the evolution will take place, in all other cases evolution will not take place.
    """
    if(p==1):
        if (x[ind]=='0'):
            x[ind]=='1'
        else:
            x[ind]='0'

with open("file.txt") as myfile:
    x=myfile.read()
    x=list(x)
for i in range (0,10000):
    evolve(x)
print(x)    