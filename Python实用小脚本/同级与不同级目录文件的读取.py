# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'
#两种方式实现读取文件的内容，下级目录中的txt
import sys
sys.path.append("D:/PycharmProjects/HQZX_company")
fp = open("./HQ_Test/phone_num1.txt","r").readlines()
print(fp)

doc = "D:\PycharmProjects\HQZX_company\HQ_Test\phone_num1.txt"
fs = open(doc,"r").readlines()
print(fs)

# -----------------------------------------------------------

#同级目录中txt内容读取
with open("phone_num1.txt","r")as fpp:
    txt = fpp.readlines()
    for i in txt:
        print(i.replace("\n",""))

