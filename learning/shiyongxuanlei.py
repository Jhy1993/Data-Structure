#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Jhy_Bistu'

#定义父类Field
class Filed(object):
    def __init__(self,name,colunm_type):
        self.name=name
        self.column_type=colunm_type
    def __str__(self):
        return '<%s:%S>'%(self.__class__,self.name)

#再定义子类StringField等
class StringField(Field):
    def __init__(self,name):
        super(StringField, self).__init__(name,'varchar(100)')
class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField,self).__init__(name,'bigint')
#模型选择
class ModelMetaclass(type):
    def __new__(cls,name,base,attrs):
        if name=='Model':
          return type.__new__(cls,name,bases,attrs)
    print('Found Modek: %s' % name)
    mapping=dict()
    for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)
#基类Model
class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))



class User(Model):
    id=IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u=User(id=1,name='jhy',email='1.qq.com',password='pass')
u.save()