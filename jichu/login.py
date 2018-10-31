# -*- coding:utf-8 -*-
# Author:Alex Li
#import getpass

_username='a';
_password='b';
username=input("username;")
password=input("password:")
if _username==username and _password==password:
    print("{name}".format(name=username))
elif _username==username:
    print("pass error")
else:
    print("error")