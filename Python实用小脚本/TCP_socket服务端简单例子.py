# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'
# 服务端
import socket

# 创建 socket
server = socket.socket()
# 绑定地址:bind()函数
address = ('0.0.0.0', 9999)
server.bind(address)
# 监听 listen()函数,10表示如果服务器没有能力去接收的话，后面可以有多少个队列可以在这等
# 到这一步才开始正式的工作
server.listen(10)
print('服务器已启动:', address)
sockfd, addr = server.accept()
# 接收成功以后可以打印一下
print("收到客户端请求：", addr)
# 数据收发，recv(),1024表示最大接收1024个字节
# 网络上的数据是经过编码或格式转化的，decode是要将格式转回来
data = sockfd.recv(1024).decode()
if data == "q" or data == "Q":
    # 关闭连接
    sockfd.close()  # 关闭通信socket
    server.close()  # 关闭监听socket
else:
    print(data)

