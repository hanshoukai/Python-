# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'
#访问元组中的一个元素
tup1 = (11,22,33,44,55,66,77)
print(tup1[1])
#定义元组
num = 1,2,3,4,5
print(num)
#两种定义元组的方式
mun1 = 1,
mun2 = (1,)
print(mun1)
print(mun2)

#元组是不可变的。提取出元组中的列表可进行修改
tup2 = (6,7,8,9,[1,2,3])
tup2[4].append(4)
print(tup2)

#元组转列表
print(list(tup2))
#列表转元组
list12 = [1,2,3]
print(tuple(list12))

#提取元组中的元素
tup3 = (('haha','gaga'),('hehe','huhu'),('kuku','lulu'))
print(tup3[0][1])

#元组的切片
print(tup3[::-1])
print(tup3[-1:-9:-1])

#元组中的方法
print(tup2.count(6))
