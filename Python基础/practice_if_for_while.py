# /usr/bin/env python
# coding=utf-8
"""
# if for while 流程控制三大常客

#if 循环
age = 28
if age >= 30:
    print('大于30')
elif age >= 20:
    print('大于20')
elif age >= 10:
    print('大于10')
else:
    print('other!')
#if嵌套循环
if age <= 30:
    if age > 20:
        print('20<age<30')


#for循环
'''
for i in range(10):
    print(i,end='')
    print(i,end='|')
    #打印结果为 00|11|22|33|44|55|66|77|88|99|
'''
#特殊的for循环，序列解包赋值
a = [(1,2),(3,4)]
for i,j in a:
    print('这是i %s'%i)
    print('这是j %s'%j)
#for循环：外层循环一次，内层循环一遍
for i in range(1,10):
    for j in range(1,i+1):
        print('%d x %d = %d\t'%(j,i,j*i),end='')
    print()


#while循环
i = 1
while i < 5:
    print("woshiyigexiaoxuesheng!")
    i += 1
else:
    print("ok")
#while嵌套循环
n = int(input('请输入要输入的数字：'))
i = 1
while i <= n:
    j = 1
    while j <= i:
        print('*',end='')
        j += 1
    print()
    i += 1




#循环中的三剑客

#pass占位符 break直接退出循环 continue跳出本次循环
name = 'xuesheng'
for i in name:
    if i == 'e':
        continue
    print(i,end='')
print()




#列表、字典和集合推导式，元组生成式

#非列表推导式写法
result = []
for i in range(10):
    result.append(i)
print(result)
#列表推导式写法
result1 = [i for i in range(10)]
print(result1)

L =  [[1,2,3],[4,5,6],[7,8,9]]
resu147 = [i[0] for i in L]
print(resu147)
resu159 = [L[i][i] for i in range(len(L))]
print(resu159)

a = [(x,y,z) for x in range(2) for y in range(2) for z in range(2)]
b = [(x,y) for x in range(2) for y in range(2) ]
print(a)
print(b)

#字典推导式
dict1 = {k:v for k,v in {'name':'kk','age':28}.items()}
print(dict1)

#集合推导式
L = [1,2,3,1,2,3,4]
set1 = {i for i in L}
print(set1)
print(type(set1))

#元组生成式
tup = (i for i in range(5))
for i in tup:
    print(i)


"""
#深拷贝会拷贝所有的对象，包括顶级对象和嵌套循对象，原始对象的改变不会造成深拷贝任何子元素的改变
#浅拷贝只拷贝顶级对象，没有拷贝嵌套对象，所以原始对象的嵌套对象改变也随之改变
import copy
a = [1,2,3,4,[5,6,7]]
b = a
#浅拷贝
c = copy.copy(a)
#深拷贝
d = copy.deepcopy(a)

a.append(8)
a[4].append(8)

print(a)
print(b)
print(c)
print(d)

'''
[1, 2, 3, 4, [5, 6, 7, 8], 8]
[1, 2, 3, 4, [5, 6, 7, 8], 8]
[1, 2, 3, 4, [5, 6, 7, 8]]
[1, 2, 3, 4, [5, 6, 7]]
'''

