# -*- coding:utf-8 -*-
# Author:Dan Li

name="my \tname is {name} and {year} old"
print(name.capitalize())
print(name.count("a"))
print(name.center(50,"-"))
print(name.endswith("ex"))
print(name.expandtabs(tabsize=30))
print(name[name.find("name"):])
print(name.format(name='ldd',year=11))
print(name.format_map({'name':'ldd','year':11}))
print(','.join(['1','2','3']))
print('\na'.lstrip())
print(name.ljust(50,'*'))
p=str.maketrans("abcdefg","1234567")
print("ldd".translate(p))
print("ldd".replace("d","D",1))
print("ldd".rfind("l"))
print("l\ndd".split("\n"))
print("l\ndd".splitlines())
print("Ldd".swapcase())
print("ldd".title())
print("ldd".zfill(4))

c=dict.fromkeys([1,2,3],"a");
print(c)
