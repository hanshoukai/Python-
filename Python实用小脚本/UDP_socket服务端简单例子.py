# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'

from socket import *

#创建UDP的socket    SOCK_DGRAM类型
server = socket(AF_INET,SOCK_DGRAM)
#绑定端口和监听主机
address  = ('0.0.0.0',9999)
server.bind(address)
print("服务器已启动",address)

#收发消息
while True:
   data,addr = server.recvfrom(1024)
   if not data:#收到的数据为空
      break
   print("收到数据：",data.decode())
   print(' 发送自:',addr)
   #回数据
   resp = "你发送的消息已收到："+data.decode()
   server.sendto(resp.encode(),addr)

server.close()
