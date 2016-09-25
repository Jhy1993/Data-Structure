# -*- coding: utf-8 -*-
"""
Created on Thu Sep 08 21:37:03 2016

@author: Jhy1993
"""
def binarySearch(array, target):
    low = 0
    high = len(array) - 1
    while low < high:
        mid = (low + high) // 2
        print array[mid]
        if target == array[mid]:
            return True
        elif target < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False
if __name__ == '__main__':
    s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    v = 2
    print binarySearch(s, v)
