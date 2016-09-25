# -*- coding: utf-8 -*-
"""
Created on Thu Sep 08 21:37:03 2016

@author: Jhy1993
"""

def InsertionSort(s):
    L = len(s)
    for i in range(1, L):
        val = s[i]
        pos = i 
        while val < s[pos - 1] and pos > 0:
            s[pos] = s[pos - 1]
            pos -= 1
        s[pos] = val 
        print s
if __name__ == '__main__':
    s = [0, 6, 2, 5, 7, 9, 8, 1]
    InsertionSort(s)

    print(s)
    
'''
Result:
[0, 6, 2, 5, 7, 9, 8, 1]
[0, 2, 6, 5, 7, 9, 8, 1]
[0, 2, 5, 6, 7, 9, 8, 1]
[0, 2, 5, 6, 7, 9, 8, 1]
[0, 2, 5, 6, 7, 9, 8, 1]
[0, 2, 5, 6, 7, 8, 9, 1]
[0, 1, 2, 5, 6, 7, 8, 9]
[0, 1, 2, 5, 6, 7, 8, 9]
'''