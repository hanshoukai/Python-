# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'

#判断是否是可迭代对象
from collections.abc import Iterable
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance((1,2,3),Iterable))
print(isinstance({'name':'hankai','age':28},Iterable))


