# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 12:14:32 2016

@author: Jhy1993
"""

class ListNode:
    """docstring for ListNode"""
    def __init__(self, data):    
        self.data = data  
        self.next = None  

a = ListNode(11)
b = ListNode(52)
c = ListNode(18)
a.next = b
b.next = c
print (a.data)
print(a.next.data)
print(a.next.next.data)

        