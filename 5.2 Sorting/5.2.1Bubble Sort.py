# -*- coding: utf-8 -*-
"""

Created on Thu Sep 08 21:37:03 2016

@author: Jhy1993
"""

def BubbleSort(s):
    L  = len(s)
    for i in range(L):
        for j in range(L-i-1): # L - (i+1)
            if s[j] > s[j+1]:
                s[j+1], s[j] = s[j], s[j+1]
        print s
    return s





if __name__ == '__main__':
    s = [4, 6, 2, 5, 7, 9, 8, 1]
    s = BubbleSort(s)
    print(s)

'''
Result:
[4, 2, 5, 6, 7, 8, 1, 9]
[2, 4, 5, 6, 7, 1, 8, 9]
[2, 4, 5, 6, 1, 7, 8, 9]
[2, 4, 5, 1, 6, 7, 8, 9]
[2, 4, 1, 5, 6, 7, 8, 9]
[2, 1, 4, 5, 6, 7, 8, 9]
[1, 2, 4, 5, 6, 7, 8, 9]
[1, 2, 4, 5, 6, 7, 8, 9]
[1, 2, 4, 5, 6, 7, 8, 9]
'''