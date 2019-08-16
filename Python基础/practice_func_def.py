# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'
"""
#递归函数
#函数的内部也可以调用外部的函数
#函数的内部也可以调用自己，这就是深度循环
'''阶乘'''
n = int(input('请输入一个数字：'))
i = 1
resu = 1
while i <= n:
    resu = resu * i
    i += 1
print(resu)
'''
1 1 1
1 2 2
2 3 6
6 4 24
24 5 120
'''
#递归小例子
def test(n):
    if n ==1:
        return 1
    return n * test(n - 1)

while True:
    n = int(input('请输入一个数字：'))
    print(test(n))
    if n > 6:
        break


#斐波那契数列
def fribo(n):
    a,b = 0,1
    c = []
    while n > 0:
        c.append(b)
        a,b = b,a+b
        n -= 1
    print(c)
fribo(5)
# 斐波那契数列:递归函数版
def feibo(n):
    if n <= 1:
        return n
    elif n ==2:
        return 1
    return (feibo(n-1)+feibo(n-2)) # i = 1,2,3,4   lsit = [1,1,2,3]
n = int(input('>>>'))
a = [feibo(i) for i in range(1,n+1)]
print(a)
# print(feibo(3))

"""
#闭包:外部找到内嵌函数，完成内嵌函数的调用而已
def outer():
    def inner():
        print('i am inner!')
    return inner
outer()()
'''打印 i am inner!'''

def outer(num):
    def inter(num_in):
        print('inter ,num_in is %d'%(num_in))
        return num_in + num
    return inter
a = outer(20)
print(a(200))


#装饰器
def fun():
    print('i am hanshoukai')

print('*'.center(50,'-'))

def outer(func):
    def inner():
        fun()
        print('i come from china!')
    return inner
a = outer(fun)
print(a())



















print('*'.center(50,'-'))

import time
print(time.time()*1000)
print(int(time.time()*1000))

