# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'
import hashlib

print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)
#md5加密
md5_data = hashlib.md5()
md5_data.update(('hankai123'+'HSK').encode('utf-8'))
print(md5_data.hexdigest())
#a8c02650ebec65757c8f15dd4d0dab87   hankai123
#118adf98d49b801691312781bf3076a5   hankai123+HSK

#sha256加密
sha256_data = hashlib.sha256()
sha256_data.update('hankai123'.encode('utf-8'))
print(sha256_data.hexdigest())

#模拟用户登录
#自定义用户的用户名和密码
user = {'name':'hankai','password':'118adf98d49b801691312781bf3076a5'}

class User_login():
    def __init__(self,name,password):
        self.name = name
        self.password = password

    def md5_salt(self,password):
        return self.password+'HSK'

    def login(self):
        md5 = hashlib.md5()
        md5.update(self.md5_salt(self.password).encode('utf-8'))
        password = md5.hexdigest()
        if self.name == user['name'] and user['password'] == password:
            print('用户名密码正确！')
            return 'good!'
        else:
            print('用户名密码错误！')
            return 'bad!'

if __name__ == '__main__':
    name = input("请输入用户名：")
    password = input("请输入密码：")
    user_login = User_login(name,password)
    user_login.login()


