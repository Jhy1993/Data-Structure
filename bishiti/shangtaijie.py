# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 10:34:26 2016

@author: Jhy1993
题目描述
有一楼梯共m级，刚开始时你在第一级，若每次只能跨上一级或二级，要走上第m级，共有多少走法？
注：规定从一级到一级有0种走法。
输入
输入数据首先包含一个整数n(1<=n<=100)，表示测试实例的个数，然后是n行数据，每行包含一个整数m，（1<=m<=40), 表示楼梯的级数。
样例输入
2
2
3

输出
对于每个测试实例，请输出不同走法的数量。
样例输出
1  即 1-2
2  即 1-3 或 1-2-3

"""
def jump(n):
    if n <= 3:
        return n - 1
    else:
        return jump(n - 1) + jump(n - 2)

num = int(raw_input())
for i in range(num):
    x = int(raw_input())
    print jump(x)

