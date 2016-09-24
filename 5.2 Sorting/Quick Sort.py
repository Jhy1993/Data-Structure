# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 21:56:27 2016

@author: Jhy1993
"""
def sub_sort(array, low, high):
    key = array[low]
    while low < high:
        while low < high and key <= array[high]:
            high -= 1
        while low < high and key > array[low]:
            array[low] = array[high]
            low += 1
            array[high] = array[low]
        key = array[low]
    return low

def quick_sort(array, low, high):
    if low < high:
        key_index = sub_sort(array, low, high)
        #Every While,key will be put on the final positon and won't change.
        quick_sort(array, low, key_index)
        quick_sort(array, key_index+1, high)

if __name__ == '__main__':
    array = [8,10,9,6,4,16,5,2,1,7,3]
    quick_sort(array,0,len(array)-1)
    print array


'''
8 9 5 1 3
while 1
3l 9 5 1 3h
3 9l 5 1 9h
while 2 
3 1l 5 1h 9
3 1 5l 5h 9 
while 3   8> 最后一个5
3 1 5l 5h 9
3 1 5 5lh 9

while jieshu
3 1 5 8 9 
'''








