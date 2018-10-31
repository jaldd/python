# -*- coding:utf-8 -*-
# Author:Dan Li
import sys
f=open("a.txt","r",encoding="utf-8")
f_new=open("a.bak","w",encoding="utf-8")
#
# find_str=sys.argv[1]
# replace_str=sys.argv[2]
for line in f:
    if "222" in line:
        line=line.replace("222","45678")
        # line=line.replace(find_str,replace_str)
    f_new.write(line)
f.close()
f_new.close()