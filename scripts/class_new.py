#coding:utf-8

import traceback
import sys

class Test(object):
    '''
    @property可以将python定义的函数“当做”属性访问，从而提供更加友好访问方式，但是有时候setter/deleter也是需要的
    '''
    def __init__(self):
        self.x = 0
    @property
    def name(self):
        return self.x

    @name.setter
    def name(self,value):
        self.x = value

    @name.deleter
    def name(self):
        del self.x

test = Test()
print (test.x)
try:
    test.name = 3
    print (test.name)
    del test.name
except:
    print (sys.exc_info())
