# -*- coding: utf-8 -*-
"""
@author: Arpit Somani
"""


from scipy import stats
estimates=[50,60,55,56,10,30,100,40,65,51]
estimates.sort()
a=stats.trim_mean(estimates,0.1)
print("Estimated Mean :",a)