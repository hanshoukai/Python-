# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'

import socket

#创建socket
client = socket.socket()
#连接服务器 connect函数
address = ('127.0.0.1',9999)
client.connect(address)

#发送数据  send（）函数
#encode,转换成网络上传输的格式
while True:
   msg = input("请输入要发送的消息：")
   if msg == 'q' or msg == "Q":
      break
   client.send(msg.encode())
   print('消息已发送')
#关闭连接
client.close()
print('客户端已关闭')
