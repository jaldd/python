# -*- coding:utf-8 -*-
# Author:Dan Li

import sys
print(sys.getdefaultencoding())
s="你好"
s_gbk=s.encode("gbk")
print(s)
print(s_gbk)
print(s.encode())
print("utf8",s_gbk.decode("gbk").encode("utf-8"))
print(s_gbk.decode("gbk"))
