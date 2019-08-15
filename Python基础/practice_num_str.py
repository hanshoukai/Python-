# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'

import keyword
#打印python中的关键字
print(keyword.kwlist)
#打印变量的类型
print(type(keyword.kwlist))

#赋值
name = 'hankai'             #传统赋值
user = mingzi = 'xiaobei'   #链式赋值
name1,age = 'hank',29       #序列解包赋值

a = 10
b = 11
a,b = b,a
print(a)
print(b)

#数字
#数字分为整型和浮点型   // 取整除  % 取余
#取x的绝对值
print(abs(-2.5))
#2**3次方
print(pow(2,3))
#查看函数的帮助文档
print(help(pow))

#字符串
print("my name is %s"%('xiaobei'))  #my name is xiaobei
print("my age is %d"%(28))          #my age is 28
print("my age is %f"%(28))          #my age is 28.000000
print("my age is %.2f"%(28))        #my age is 28.00

str_test = 'hello world'
#正向
print(len(str_test))
print(str_test[2:7])
print(str_test[0:7])
print(str_test[:7])
print(str_test[2:])
print(str_test[:])
print(str_test[::2])
#反向
print(str_test[-1])
print(str_test[::-1])
print(str_test[::-2])
print(str_test[1:9:-1])   #打印为空
print(str_test[10:0:-2])

print('小练习'.center(50,'-'))
a = input('请输入性别:')
if a == 'F' or a == 'M':
    b = int(input('请输入年龄：'))
    if b >= 18:
        print('youare daren!')
    else:
        print('youare baby!')
else:
    print('输入不正确，请重新输入！')

