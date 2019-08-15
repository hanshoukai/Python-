# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'

list1 = ['山东','北京','辽宁','广东','新疆']
#在原来列表中追加
list1.append('海南')
#在指定下标下添加元素
list1.insert(0,'四川')
print(list1)

list2 = ['广西','内蒙','陕西','江西']
#把list2加入list1后，显示为两个列表合并
list1.extend(list2)
print(list1)
#两个列表合并的另一种方式
# print(list1+list2)
#删除列表最后一位元素
list1.pop()
print(list1)
#删除列表中指定的元素
list1.remove('北京')
print(list1)
#删除列表中指定的下标的元素
del list1[1]
print(list1)
#修改列表中的元素
list1[-1] = '河南'
print(list1)
#获取指定元素的下标
print(list1.index('河南'))
#查询是否在列表中
print('河南' in list1)
#列表根据ascii码进行排序
list1.sort()
print(list1)
#列表进行倒序排序，显示的结果与方向切片一样
list1.reverse()
print(list1)

#列表中的切片
print(list1[1:9:2])
print(list1[-1:-6:-2])

#列表转字符串
print(''.join(list1))

