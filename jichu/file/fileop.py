# -*- coding:utf-8 -*-
# Author:Dan Li

data=open("jihe.py",encoding="utf-8").read()
#print(data)

f=open("fileop.py",'r',encoding="utf-8")
#print(f.read())
#w为创建一个文件。
f=open("a.txt",'w+',encoding="utf-8")
f.write("12345\n")
f.seek(0)
print(f.readline())
f.write("222")

print("aaa")
f.tell()
f.read()
f=open("a.txt",'a',encoding="utf-8")
f.write("上山打老虎")
f.truncate(10)
f=open("a.txt",'r+',encoding="utf-8")
f.read()
f.write("12345\n")
f.write("上山打老虎")
f=open("fileop.py",'r',encoding="utf-8")
for i in range(5):
    print(f.readline())
'''
for index,line in enumerate(f.readlines()):
    if index==9:
        print('')
        continue
    print(line.strip())
'''
count=0;
for line in f:
    if count==9:
        print('')
        count+=1
        continue
    print(line.strip())
    count+=1

f=open("a.txt",'r',encoding="utf-8")
print(f.tell())
print(f.read(5))
print(f.tell())
f.seek(1)
print(f.tell())
print(f.encoding)
print(f.fileno())
f=open("a.txt",'ab')
f.write("aaabbbctd".encode())







f.close()