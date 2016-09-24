# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 20:20:44 2016

@author: Jhy1993
题目描述：
数列的定义如下：
数列的第一项为n，以后各项为前一项的平方根，求数列的前m项的和。
输入
输入数据有多组，每组占一行，由两个整数n（n<10000）和m(m<1000)组成，n和m的含义如前所述。
输出
对于每组输入数据，输出该数列的和，每个测试实例占一行，要求精度保留2位小数。

样例输入
81 4
2 2
样例输出
94.73
3.41
"""
str = raw_input()
m = int(str.split()[0])
n = int(str.split()[1])
#print range(n)
x=0
for i in range(n):
    y = m ** (2**(-i))
#    print y
    x  += y
#    print x, m
print "%.2f" %x
