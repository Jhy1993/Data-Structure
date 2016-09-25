# -*- coding: utf-8 -*-
"""
Created on Thu Sep 08 21:37:03 2016

@author: Jhy1993
"""



def SelectionSort(s):
    L = len(s)
    for i in range(L):
        minumus_index = i
        for j in range(i, L):
            if s[minumus_index] > s[j]:
                minumus_index = j
        s[i], s[minumus_index] = s[minumus_index], s[i]
        print s


if __name__ == '__main__':
    s = [3, 4, 6, 2, 9, 5, 1, 9, 8]
    SelectionSort(s)
'''
Result:
[1, 4, 6, 2, 9, 5, 3, 9, 8]
[1, 2, 6, 4, 9, 5, 3, 9, 8]
[1, 2, 3, 4, 9, 5, 6, 9, 8]
[1, 2, 3, 4, 9, 5, 6, 9, 8]
[1, 2, 3, 4, 5, 9, 6, 9, 8]
[1, 2, 3, 4, 5, 6, 9, 9, 8]
[1, 2, 3, 4, 5, 6, 8, 9, 9]
[1, 2, 3, 4, 5, 6, 8, 9, 9]
[1, 2, 3, 4, 5, 6, 8, 9, 9]
'''