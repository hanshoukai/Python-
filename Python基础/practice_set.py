# /usr/bin/env python
# coding=utf-8

#set集合
s1 = {1,2,3,4,4,4,4}
print(type(s1))
print(s1)

a = set('1234')
b = set('3456')
#打印ab的交集
print(a&b)
#打印ab的并集
print(a|b)
#打印ab的差集，只有前项有的元素
print(a-b)
print(b-a)
#打印ab的对称差集，ab中非公共的元素
print(a^b)

#集合的操作
data_set = set(('google','baidu','soso'))
#集合的添加
data_set.add('jd')
data_set.update([1,2])
print(data_set)

#删除指定的元素
data_set.remove(1)
#删除指定的元素，如果不存在不会报错
data_set.discard(2)
#随机删除一个元素
data_set.pop()
print(data_set)

