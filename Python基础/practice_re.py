# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'
import re
data1 = re.findall('a.c','abcacc')
data2 = re.findall('a\.c','abcacca.c')
data3 = re.findall('a[bcd.]c','abcacca.c')
data4 = re.findall('a\d\w','abcacca.ca7bsjdhskdkas')
data5 = re.findall('h\ssk','abcacca.ca7bsjdh skdkas')
data6 = re.findall('a\Sc','abcacca.ca7bsjdh skdkas')
data7 = re.findall('a\w','abcacca.ca7bsjdh skdka_s')
data8 = re.findall('a{2}','aabcacca.ca7bsjdh skdkaaa_s') #匹配前一个字符两次，打印出两个aa
data9 = re.findall('a{2,4}','aabcacca.ca7bsjdh skdkaaa_s') #匹配前一个字符2到4次，打印出一个aa一个aaa
data10 = re.findall(r'^abc','abcdef')  #以abc为开头
data11 = re.findall(r'abc$','abcdef')   #以abc为结尾
data12 = re.findall(r'abc|def','abcdef')


data13 = re.findall(r'Heelo','heelo what',re.I)   #忽略大小写
data14 = re.findall(r'heelo','heelo \n wnhat heelo',re.M)   #多行模式
data = re.findall(r'he(.*)o','heelo \n wnhat heelo\n heelo',re.S)   #改变.的行为
print(data)

#全部进行匹配
test_str = '''
<thead>
    <tr>
      <th class = 'ok'>Month</th>
      <th>Savings</th>
    </tr>
  </thead>
'''
print(re.findall(r"<tr>(.*?)</th>",test_str,re.S))

#从开头进行匹配
temp = '''first line
second line
third line '''
print(re.match(r'.+',temp,re.S).group())

#从整个字符串中匹配数字123
tempp = 'hello world\nhankai\nxiaobei wo123'
print(re.search('\d{3}',tempp,re.S).group())

#以什么进行切割
stringg = 'hello world,i am one,what is your name?'
print(re.split(',',stringg))

#以HK替换掉字符串中的数字
string = 'dhshdkahkddhsiuddhshkjh372648kdskshkd'
print(re.sub('\d','HK',string))

#group与groups区别
strin = '''Once upon a time there were three little sisters; and their names were
and they lived at the bottom of a well. '''
print(re.match('(\w+) (\w+) (\w+) (\w+) (\w+) (\w+)',strin,re.S).group())
#group和group(0)返回整个Once upon a time there were
#group(1)返回第一个单词Once
print(re.match('(\w+) (\w+) (\w+) (\w+) (\w+) (\w+)',strin,re.S).groups()[3])
#groups括号内无论写还是不写都以元组的形式返回整个匹配的结果('Once', 'upon', 'a', 'time', 'there', 'were')
#groups()[3]从0开始取第3个值

'''
#练习：从列表中提取出字符并拼凑成大写的LUCKY
list1 = ['aycc','kh','llc','u','l']
list1 = ''.join(list1)
a = []
a.append(list1[1])
a.append(list1[4])
a.append(list1[8])
a.append(list1[9])
a.append(list1[10])
a.reverse()
a = ''.join(a)
print(a.upper())
'''
