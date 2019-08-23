# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'
'''
#迭代器
# 打印是否是可迭代对象：匹配成功返回True，不成功返回False
from collections.abc import Iterable
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance((1,2,3),Iterable))
print(isinstance({'name':'hankai','age':28},Iterable))


#for循环迭代器和next方法
a = 'abcdef'
for i in a:
    print(i)   #遍历打印a中的字符串
print(i)       #只打印a中的 “f”

print('------------')
b = iter(a)         #可迭代对象赋值给b
print(next(b))      #打印b的第一个迭代对象字母“a”

for i in b:         #因为已经用next打印了a，所以for循环从b开始打印
    print(i)



'''
#for循环的本质
L = [1,2,3,4]
it = iter(L)
#第一种方式
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         print('循环结束')
#         break
#第二种方式
n = 0
while n < len(L):
    print(next(it))
    n += 1
else:
    print('循环结束')
#以上两种方式不可同时运行！





