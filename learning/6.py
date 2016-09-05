#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Jhy_Bistu'
#server
#从wsgiref模块导入
from wsgiref.simple_server import make_server
#导入直接的application函数
from hello import application
#创建服务器，ip地址为空，端口8000，处理函数是application 在5.py中
httpd=make_server('',8000,application)
print('server HTTP on port 8000...')
#开始监听http请求
httpd.serve_forever()