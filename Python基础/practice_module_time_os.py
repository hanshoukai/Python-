# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'
import time,os

print('打印本地九元素时间：',time.localtime())
print('打印格林尼治九元素时间：',time.gmtime())
print('字符串格式本地时间：',time.asctime())
print('字符串格式本地时间：',time.ctime())
print('打印时间戳：',time.time())
# print(time.sleep(3))
print('格式化输出本地时间：',time.strftime('%Y-%m-%d %H:%M:%S'))
print('格式化输出本地时间：',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
print('格式化输出格林尼治时间：',time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime()))
#把时间转换成九元素格式时间
date_str = '2019-08-23 16:09:23'
print(time.strptime(date_str,'%Y-%m-%d %H:%M:%S'))



print('华丽的分割线'.center(40,'*'))


print('返回操作系统类型，nt为window：',os.name)
print('返回操作系统的分隔符：',os.sep)
print('返回当前的工作路径：',os.getcwd())
print('返回当前路径下的文件：',os.listdir('D:\pycharmworkspace'))

# print('创建文件夹名为a的目录：',os.mkdir('a'))
# print('删除a文件夹',os.rmdir('a'))
# print('递归创建文件夹目录：',os.makedirs('b/c/d'))
# print('递归删除文件夹目录：',os.removedirs('b/c/d'))

print('执行系统命令：',os.system('ipconfig'))

for i in os.popen('dir'):
    print('打印当前目录有啥：',i)

