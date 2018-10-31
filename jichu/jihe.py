# -*- coding:utf-8 -*-
# Author:Dan Li

list_1=[1,2,3,4,3]
list_1=set(list_1)
#print(list_1,type(list_1))
list_2=[1,2,5,3,4,3]
list_2=set(list_2)
print(list_1,list_2)
#交集
print(list_1.intersection(list_2)) #&
#并集
print(list_1.union(list_2)) #|
#差集
print(list_1.difference(list_2)) #-
#子集
print(list_1.issuperset(list_1.difference(list_2)))
#对称差集
print(list_1.symmetric_difference(list_2)) #^
print(list_1.isdisjoint(list_1.symmetric_difference(list_2)))
list_1.add(9)
list_1.update([11,12,33]) #添加多个
list_1.pop();
list_1.discard(11)
print(list_1)