#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Jhy_Bistu'
from flask import Flask
from flask import request
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>77777py</h1>'

@app.route('/signin',methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin',methods=['POST'])
def signin():
    #需要从reques对象中读取表单内容
    if request.form['username']=='a' and request.form['password']=='b':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'
if __name__ == '__main__':
    app.run()