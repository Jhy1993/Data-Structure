# -*- coding: utf-8 -*-
"""
Created on Thu Sep 08 21:37:03 2016

@author: Jhy1993
"""


def SelectionSort(s):
    L  = len(s)
    for i in range(L):
        small_index = i
        for j in range(i + 1, L):
            if s[small_index] > s[j]:
                small_index = j
        s[i], s[small_index] = s[small_index], s[i]
        print s

if __name__ == '__main__':
    s = [3, 4, 6, 2, 5, 1]
    SelectionSort(s)
    print(s)