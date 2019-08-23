# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'
#生成器
def myyield():
    print('生成2')
    yield 2
    print('生成3')
    yield 3
    print('生成5')
    yield 5
    print('生成7')
    yield 7
gen = myyield()
print(gen)       #<generator object myyield at 0x0000025F23D92F48>
# print(next(gen)) #打印第一个生成的2和‘生成2’

it = iter(gen)   #生成器通过iter函数转换成迭代器
for i in it:
    print(i)


#生成器表达式
"""
1利用元组生成式生成元组
2打印是否为生成式
3利用iter函数转成迭代器
4for循环打印元组的内容
"""
genn = (x**2 for x in range(1,5))
print(genn)
itt = iter(genn)
for i in itt:
    print(i)


#练习：将L内容的数都变成数的平方并以列表形式返回
L = [2,3,4,5]
#直接使用列表推导式
L1 = [x**2 for x in L]
print(L1)
#元组生成式再转换成列表的形式
G3 = (i**2 for i in L)
print(list(G3))






