# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'

import paramiko

ssh = paramiko.SSHClient()
trans = paramiko.Transport(
    sock= (
        "192.168.89.136",22
    )
)

trans.connect(
    username = 'root',
    password = 'hankai'
)
ssh._transport = trans
shell = ssh.invoke_shell()
shell.settimeout(1)
shell.send(input( ">>> ")+  " \n " )
while True:
    try:
        recv  = shell.recv(512).decode()  #接收返回值
        if recv:
            print(recv)
        else:
            continue
    except:
        shell.send(input( ">>> ")  + "\n" )

ssh.close()


