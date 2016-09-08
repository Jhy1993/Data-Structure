# -*- coding: utf-8 -*-
"""
Created on Thu Sep 08 21:37:03 2016

@author: Jhy1993
"""


def LinearSearch(s, v):
    L  = len(s)
    for i in range(L):
        if v == s[i]:
            return True
    return False

def SortedLinearSearch(s, t):
    L = len(s)
    for i in range(L):
        if s[i] == t:
            return True
        elif s[i] > t:
            return False
    return False

def FindSmallest(s):
    L = len(s)
    smallest = s[0]
    for i in range(L):
        if s[i] < smallest:
            smallest = s[i]
    return smallest

if __name__ == '__main__':
    s = [3, 4, 6, 2, 5, 11]
    ss = [1, 2, 3, 6, 7, 22]
    v = 5
    print LinearSearch(s, v)
    print SortedLinearSearch(ss, v)
    smallest = FindSmallest(s)
    print smallest
