#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Jhy_Bistu'

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'
def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
#把函数consumer传入produce中
#n = yield r 并不是赋值语句，相当于：
#if produce return n
#if consume return r
#如果是produce调用send的话，就相当于在consumer中为n赋值
#如果是consume调用yield r的话，就相当于在produce中为r赋值