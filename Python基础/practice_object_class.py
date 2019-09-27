# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'

class Bird():
    def say_hello(self):
        print('hello,i am bird.')
    def bird_info(self):
        print('My name is %s'%(self.name))
#创建一个对象
d = Bird()
#调用方法的两种方式
d.say_hello()
Bird.say_hello(d)
#调用方法
d.name = 'hankai'
d.bird_info()


#类的内置方法
print('类的属性', Bird.__dict__)
print('类的文档字符串', Bird.__doc__)
print('类的名字', Bird.__name__)
print('类定义所在的模块', Bird.__module__)
print('类的所有父类构成的元素', Bird.__bases__)


#小示例
class registration:
    def __init__(self):
        self.school = {
            'Linux':[],
            'Python':[]
        }

    def register(self,major,student):
        if major in self.school:
            self.school[major].append(student)
            print('报名成功！')
        else:
            print('报名失败！没有你要的专业%s'%major)

if __name__ == '__main__':
    student = {
        'name':'hk',
        'major':'Linux'
    }
    reg = registration()
    reg.register(student.get('major'),student)
    print(reg.school)

"""类的三种方法"""
#1、类方法@classmethod
class People(object):
    #类属性
    country = 'china'
    #类方法，用classmethod来进行修饰
    @classmethod
    def getCountry(cls):
        return cls.country
    @classmethod
    def setCountry(cls,country):
        cls.country = country
p = People()
#通过实例对象引用
print (p.getCountry())
#通过类对象引用
print (People.getCountry())
#更改类属性为USA
p.setCountry('USA')
#通过实例对象引用
print (p.getCountry())
#通过类对象引用
print (People.getCountry())

#2、静态方法@staticmethod
class People():
    country = "china"
    @staticmethod
    def getcountry():
        print('i am hankai,come from china.')
    def test(self):
        print('test')
people = People()
people.getcountry()
people.test()
People.getcountry()

#3、对象方法（函数）

#私有属性
class Peo():
    def __init__(self,name,age):
        self.__name = name
        self.age = age
    def hello(self):
        print(self.__name)
        print(self.age)
P = Peo('hanki',18)
P.hello()
#私有方法
class Peo():
    def __init__(self,name,age):
        self.__name = name
        self.age = age
    def __func(self):
        print('-------------')
        print(self.__name)
        print(self.age)
    def hello(self):
        self.__func()
P = Peo('hanki',18)
P.hello()

"""
私有的方法只能在类中调用不能被继承，可继承的只有类的方法
多继承，先广度后深度
"""
class Base(object):
    def test(self):
        print('base')
class A(Base):
    def test1(self):
        print('test1')
class B(Base):
    def test2(self):
        print('test2')
class C(B,A):
    pass
c = C()
c.test()
c.test1()
c.test2()

#单例模式
