# -*- coding: utf-8 -*-
"""
@author: Arpit Somani
"""
from statistics import mean
estimates=[50,60,55,56,10,30,100,40,65,51]
print("Original Mean :",mean(estimates))
estimates.sort()
tv=int(0.1*len(estimates))
estimates=estimates[tv:]
estimates=estimates[:len(estimates)-tv]
print("Estimated Mean :",mean(estimates)) 

