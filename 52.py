# -*- coding: utf-8 -*-
"""
Created on Sat Sep 03 19:48:32 2016

@author: Jhy1993
"""
v = [1, 3, 4, 2, 1, 0]
t = 4
def linearsearch(v, t):
    n = len(v)
    for i in range(n):
        if v[i] == t:
            return True
    return False
flag = linearsearch(v, t)
print flag

def sortedlinearsearch(v, t):
    n = len(v)
    for i in range(n):
        if v[i] == t:
            return True
        elif v[i] > t:
            return False
    return False
flag = sortedlinearsearch(v, t)
0902-2
