# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 10:42:24 2016

@author: Jhy1993
Run Time Analysis
Assume len(listA) = len(listB) = N
While 1: listA and listB are copy into newlist, 
a total 2n-1 iteration
While 2&3 : if all elements in listA smaller than listB, 
will be n
Reslut :O(n)
"""
def findSortedPosition(array, target):
    low = 0
    high = len(array) - 1
    while low < high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            high = mid -1
        else:
            low = mid + 1

    return low# low = mid = high, so they can exchange
if __name__ == '__main__':
    s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    v = 9
    print findSortedPosition(s, v)
def mergeSortedLists(listA, listB):
    newlist = list()
    a = 0
    b = 0
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newlist.append(listA[a])
            a += 1
        else:
            newlist.append(listB[b])
            b += 1
    while a < len(listA):
        newlist.append(listA[a])
        a += 1
    while b < len(listB):
        newlist.append(listB[b])
        b += 1
    return newlist
if __name__ == '__main__':
    s1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    s2 = [1.1, 7.4, 8.1, 9, 10]
    print mergeSortedLists(s1, s2)

