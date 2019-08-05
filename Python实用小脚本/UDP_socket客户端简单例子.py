# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'

from socket import *

address = ('127.0.0.1', 9999)
# 创建UDP套接字
client = socket(AF_INET, SOCK_DGRAM)
while True:
    data = input("请输入要发送的消息")
    if not data:
        continue
    if data == "Q" or data == 'q':
        break
    client.sendto(data.encode(), address)

    # 接收数据
    resp, addr = client.recvfrom(1024)
    if not resp:
        print(resp.decode())
client.close()
