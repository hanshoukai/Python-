# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'
import paramiko

trans = paramiko.Transport(
    sock = (
        '192.168.89.134',22
    )
)
trans.connect(
    username = 'root',
    password = 'hankai'
)
sftp = paramiko.SFTPClient.from_transport(trans)

#上传文件
# sftp.put('1.py','/root/1.py')

#下载文件
sftp.get('/root/1.py','2.py')

sftp.close()

