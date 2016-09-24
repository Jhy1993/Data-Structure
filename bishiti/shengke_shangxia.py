# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 10:53:18 2016

@author: Jhy1993
输入
第一行读入一个整数n(1<=n<=100)，表示有n个站点
接下来n行，每行两个数值，分别表示在第i个站点下车人数和上车人数
样例输入
4
0 3
2 5
4 2
4 0

输出
每组输出车上最多的乘客数目
样例输出
6
"""
ren_num = 0
ren_max = 0
zhan_num = int(raw_input())
for i in range(zhan_num):
    s = raw_input()
    xia, shang = int(s.split()[0]), int(s.split()[1])
    ren_num += shang - xia
    if ren_num > ren_max:
        ren_max = ren_num
print (ren_max)
    