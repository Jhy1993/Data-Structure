# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 15:38:19 2016

@author: Jhy1993
"""
n = raw_input()

nums = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
nn = list()
for i in range(int(n)):
    fenshen = raw_input()
    num = []
    for shuzi in nums:
#        print shuzi
        if fenshen.find(shuzi) > -1:
#            print nums.index(shuzi)
            num.append(nums.index(shuzi))
    num = sorted(num)
    num =  ''.join([str(i) for i in num])
    nn.append(num)
for i in nn:
    print i


	