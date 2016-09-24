# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 11:04:07 2016

@author: Jhy1993
"""

def ysj(zz, yy, sz, zy):
    if zz >= 60 and yy >=60 and sz >=90 and zy >= 90 and zz+yy+sz+zy >=310:
        if zz+yy+sz+zy >= 350:
            print ('Gongfei')
        else:
            print ('Zifei')
    else:
        print ('Fail')
n = int(raw_input())
for i in range(n):
    s = raw_input().split()
    zz = int(s[0])
    yy = int(s[1])
    sx = int(s[2])
    zy = int(s[3])
    ysj(zz, yy, sx, zy)