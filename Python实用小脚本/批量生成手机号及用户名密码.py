# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'

import random

"""批量生成手机号"""
#可能会出现重复的手机号，因为是随机生成的。
num = 1
while num < 5:
    cell_phone_number1 = "1780148"+str(random.randint(1000,9999))+"\n"
    num += 1
    with open("cell_phone_number.txt","a")as fp:
        fp.write(cell_phone_number1)
        print(num)

#方法二：避免出现重复的手机号
for i in range(5000,5010):
    print(i)
    cell_phone_number1 = "1780148"+str(i)+"\n"
    with open("phone_num1.txt","a")as fp:
        fp.write(cell_phone_number1)

#-------------------------------------------------------------------------
"""批量生成用户名和密码"""
num = 1
while num < 10:
    username = ''.join(random.sample(
        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o',
         'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'], 8))
    password = random.randint(100000, 999999)
    txt = str(username) + "," + str(password) + "\n"
    num += 1
    with open("user.txt", "a") as f:
        f.write(txt)
        print(num)

#生成的格式如下
'''
04cyh7bd,898065
qb1td85e,149545
o7znrwyq,416928
6turbxw9,148315
rm7l24ic,671465
'''
