# -*- coding:utf-8 -*-
# Author:Dan Li

with open("a.txt","r",encoding="utf-8") as f1,\
      open("a.bak","r",encoding="utf-8") as f2:
    for line in f1:
        print(line)
    for line in f2:
        print(line)