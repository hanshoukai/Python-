# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'

dict1 = {"name":"kk","age":28,"addr":"beijing"}
#打印键名对应的值
print(dict1['age'])
print(dict1.get('name'))
#打印name1对应的值，如果没有打印name
print(dict1.get('name1','name'))
#增加
dict1['like'] = '小野百惠'
print(dict1)
#删除
# del dict1['like']
# print(dict1)
#打印字典的键
print(dict1.keys())
#打印字典的值
print(dict1.values())
#如果存在返回，如果不存在创建键
print(dict1.setdefault('car','bieke'))
print(dict1)
#{'name': 'kk', 'age': 28, 'addr': 'beijing', 'like': '小野百惠', 'car': 'bieke'}

#更新字典，如果键不存在，创建键和值
dict1.update({'love':"abc"})
print(dict1)
#以元组的形式返回字典的内容
print(dict1.items())
#查看键值对的个数
print(len(dict1))
#删除指定的元素
print(dict1.pop('love'))
#随机删除一个元素
print(dict1.popitem())
#清空字典
# print(dict1.clear())
#判断是否在字典中
print('name' in dict1)

for k,w in dict1.items():
    print(k,w)



