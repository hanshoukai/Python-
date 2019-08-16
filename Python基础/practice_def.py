# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'
#函数
def func(n):
    print('这是一个测试函数。')
    a = n + 1
    return a
# func(2)
# print(func(3))

#位置参数、关键字参数、默认参数、参数组
#位置参数
def func1(name,city):
    print('i am %s ,i from %s'%(name,city))

func1('kk','beijing')

#关键字参数
def func1(name,city):
    print('i am %s ,i from %s'%(name,city))

func1(city='beijing',name='kk1')

#默认值参数
def func1(name,city='beijing'):
    print('i am %s ,i from %s'%(name,city))

func1('xiaobei')
func1('xiaobei','shenzhen')

#参数组
# 以元组的形式进行返回
def cc(*args):
    print(args)
cc('1,2,3,4,5')
cc(['1,2,3,4,5'])
# 以字典的形式进行返回
def kk(**kwargs):
    print(kwargs)
kk(a = 1,b = 2)
kk(a = 1,b = 2,c = 3)


#不定长参数小例子
def hello(e,f,d=2,*args,**kwargs):
    a = args
    b = kwargs
    print(a,b)
hello(1,2,3,4,5,6,7,name = 'kk')


#匿名函数
l = lambda x: x* x
print(l(3))

def lamdada(x):
    return x * x
print(lamdada(3))



L = lambda x:'x>10' if x>10 else 'x<10'
print(L(3))

def L(x):
    if x>10:
        return 'x>10'
    else:
        return 'x<10'
print(L(26))



#map函数,map对象需要用list函数显示出来
#map() 会根据提供的函数对指定序列做映射。
a = map(lamdada,[1,2,3,4])
print(list(a))
b = map(lambda x:x*x,[1,2,3])
print(list(b))

c = [1,2,3,4]
d = [5,6,7,8]
f = map(lambda x,y:x+y,c,d)
print(list(f))

print('*'.center(50,'-'))

import sys
#打印模块的内置函数
print(dir(sys))



#作用域遵循就近原则
'''
name = 'han'  #用于全局，全局变量
def outer():
    name = 'kai'  #嵌套作用域
    def inter():
        name = 'shou'  #局部变量，本地作用域
        age = 28
        print(name)
        print(age)
    inter()
outer()


name = 'han'  #用于全局，全局变量
def outer():
    name = 'kai'  #嵌套作用域
    def inter():
        global name  #直接找到全局变量
        age = 28
        print(name)
        print(age)
    inter()
outer()
'''

name = 'han'  #用于全局，全局变量
def outer():
    name = 'kai'  #嵌套作用域
    def inter():
        nonlocal name  #找到上一级变量
        age = 28
        name = 'hanshoukai'
        print(name)
        print(age)
    inter()
    print(name)
outer()


#偏导数
import functools
def add(a,b):
    print('a是：',a)
    print('b是：',b)
    return a+b
plus = functools.partial(add,30)
print(plus(2))


#小练习，把两个列表的值进行拼接生成一个新的列表
A = ['a','b','c']
B = ['d','e','f']
C = map(lambda x,y: x+y,A,B)
print(list(C))

def funcc(x,y):
    return x+y
cc = map(funcc,A,B)
print(list(cc))


