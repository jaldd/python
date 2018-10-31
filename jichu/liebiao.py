# -*- coding:utf-8 -*-
# Author:Alex Li

names=["a","b","c","e","v"]
names2=["1","2","3",["4","5"]]
print(names2[:-1:2])
# print(names[1])
# print(names[1:3])
# print(names[-3:-1])
# print(names[-3:])
# names.append("d");
# names.insert(1,"f")
# names[1]=3
# names.remove(3)
# names.remove(names[2])
# names.pop()
# names.pop(0)
# print(names)
# print(names.index("b"))
# names.append(names[names.index("b")])
# print(names.count("b"))
# names.reverse()
# print(names)
# names.sort()
# print(names)
# names.clear()
# print(names)
# names.extend(names2)
# del names2
print(names,names2)
names3=names2.copy()
print(names3)
names2[0]=111
print(names3)
names2[3][0]="0"
print(names2)
print(names3)


import  copy
names4=copy.deepcopy(names2)
names2[3][0]="9"
print(names2)
print(names4)









