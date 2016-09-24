# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 17:16:38 2016

@author: Jhy1993
"""

s = raw_input()
s = list(s)
zc = list()
k = 0
for i in range(len(s)):
    j = i+1
    if s[j] == s[i] and s[i:j] not in zc:
    
        zc.append(s[i:j])
        j += 1
print k

