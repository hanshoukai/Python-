# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'

'''读'''
#读取所有数据
f = open('data.json','r',encoding='utf-8')
#读取10个字符，指针在最后一个字符后，如果在读取10个字符就在上次结束位置开始，如下
print(f.read(10))
print(f.read(10))

#只读取一行数据
f1 = open('data.json','r',encoding='utf-8')
print(f1.readline())
print(f1.readline())
print(f1.readline())

#以列表的形式返回读取的内容
f2 = open('data.json','r',encoding='utf-8').readlines()

#with操作文件并查看是否关闭
with open('data.json','r',encoding='utf-8')as f:
    print(f.readlines())
print(f.closed)
#关闭文件
q = open('data.json','r',encoding='utf-8')
q.close()


'''写'''
f3 = open('data.json','w',encoding='utf-8')
f3.write('写入的是字符串')
f3.writelines('写入的参数是序列')
#是否可写入
print(f3.writable())


#把png1的内容覆盖png2
# with open('1.png','rb')as png1:
#     with open('2.png','wb')as png2:
#         png2.write(png1.read())


#r+可读可写；r是只读
fp = open('data.json',"r+",encoding='utf-8')
#读取文件中的内容
str = fp.read()
print('打印读取的内容:',str)
#查找当前位置
position = fp.tell()
print("当前位置:",position)
#把指针再次重新定位到文件开头(第一个0是偏移量，第二个0表示开始位置，1表示当前位置，2表示结尾)
position = fp.seek(0,0)
#读取文件中的两个字符
str = fp.read(2)
print("文件中的内容为",str)
#关闭打开的文件
fp.close()

