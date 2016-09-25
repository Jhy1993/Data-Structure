# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 11:38:46 2016

@author: Jhy1993
"""

#Implementation of the Set ADT using a sorted list
class Set:
    """create a empty set instance"""
    def __init__(self):
        self._theElements = list()

    def __len__(self):
        return len(self._theElements)
    # determine if an element is in the set   
    def __contains__(self, element):
        ndx = self._findPosition(element)
        return ndx < len(self) and self._theElements[ndx] == element

    def add(self, element):
        if element not in self:
            ndx = self._findPosition(element)
            self.__theElements.insert(ndx, element)

    def remove(self, element):
        assert element in self, "the element must in the set"
        ndx = self._findPosition(element)
        self._theElements.pop(ndx)

    def isSubsetof(self, setB):
        for element in self:
            if element not in setB:
                return False
        return True

    def __iter__(self):
        return _SetIterator(self._theElements)

    def _findPosition(self, element):
        low = 0
        high = len(theList) - 1
        while  low <= high:
            mid = (low + high) / 2
            if theList[mid] == target:
                return mid
            elif target < theList[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low

    
