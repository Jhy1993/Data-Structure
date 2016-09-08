# -*- coding: utf-8 -*-
"""
Created on Thu Sep 08 21:37:03 2016

@author: Jhy1993
"""

def BubbleSort(s):
    L  = len(s)
    for i in range(L):
        for j in range(i, L - i):
            if s[j] > s[j+1]:
                s[j+1], s[j] = s[j], s[j+1]





if __name__ == '__main__':
    s = [4, 6, 2, 5, 7, 9, 8, 1]
    BubbleSort(s)
    print(s)