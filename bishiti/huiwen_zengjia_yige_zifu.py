# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 11:36:57 2016

@author: Jhy1993
回文串
题目描述
给定一个字符串，问是否能够通过添加一个字母将其变成“回文串”。 “回文串”是指正着和反着读都一样的字符串。如：”aa”,”bob”,”testset”是回文串，”alice”,”time”都不是回文串。
输入
一行一个有小写字母构成的字符串，字符串长度不超过10。

样例输入
coco

输出
如果输入字符串可以通过   添加一个字符变为回文
，则输出”YES”，否则输出”NO”。

样例输出
YES
"""
s = raw_input()
s = list(s)
s1 = s[1:len(s)] 
s2 = s[0:len(s)-1]
if s1[::] == s1[::-1] or s2[::] == s2[::-1]:
    print('YES')
else:
    print('NO')

















