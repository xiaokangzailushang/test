#coding:utf-8

class CommonException(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return 'Exception Error is {}'.format(self.msg)

ce = CommonException('kcy')
print (ce)
try:
  1/0
except Exception as e:
  raise CommonException("error in div")
