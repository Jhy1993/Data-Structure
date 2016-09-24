# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 19:07:00 2016

@author: Jhy1993

“水仙花数”是指一个三位数，它的各位数字的立方和等于其本身，
比如：153=1^3+5^3+3^3。
"""

def SXH(x):
    a = x / 100
    b = (x-a*100) / 10
    c = (x-a*100-b*10)

    if a**3 + b**3 + c**3 == x:
        return x
    else:
        return None

#m = 370 
#n = 380
str = raw_input()
m = int(str.split()[0])
n = int(str.split()[1])
xx = list()
for i in range(m, n+1):
    x = SXH(i)
    if x != None:
        xx.append(x)
if len(xx) >0:
    for x in xx:
        print x,
else:
    print ('no')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    