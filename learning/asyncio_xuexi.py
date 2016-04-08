#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Jhy_Bistu'
import asyncio
import asyncio

#把一个generator标记为coroutine类型，
# 然后，我们就把这个coroutine扔到EventLoop中执行。
async def hello():
    print("hello.world")
    #异步调用asynciosleep(1)
    r=await asyncio.sleep(1)
    print("hello again")

#获取eventloop
loop=asyncio.get_event_loop()
#执行coroutine
loop.run_until_complete(hello())
loop.close()
