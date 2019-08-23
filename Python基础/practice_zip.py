# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'
#zip函数
numbers = ['10086','10010','10000']
names = ['中国移动','中国联通','中国电信']

for i in zip(names,numbers):
    print(i)

for x,y in zip(names,numbers):
    print(x,'客服电话是：',y)

print('==================zip重写============================')
def my_zip(*args):
    all_list = list(args)
    min_list_long = len(min(all_list,key=lambda x:len(x)))
    a_list = []
    for a in range(min_list_long):
        a = [args[j][a] for j in range(len(args))]
        a_list.append(a)
    print(a_list)
my_zip(numbers,names)


#enumerate函数
#循环遍历的时候打印序号，默认0开始
for i in enumerate(zip(names,numbers)):
    print(i)
#循环遍历的时候打印序号，给了值从50开始
for i in enumerate(names,50):
    print(i)
