# -*- coding: utf-8 -*-
"""
Created on Thu Sep 08 21:37:03 2016

@author: Jhy1993
"""


def InsertionSort(s):
    L  = len(s)
    for i in range(1, L):
        v = s[i]
        pos = i
        

if __name__ == '__main__':
    s = [4, 6, 2, 5, 7, 9, 8, 1]
    InsertionSort(s)
    print(s)