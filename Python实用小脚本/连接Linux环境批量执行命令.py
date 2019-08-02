# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'
import sys
import paramiko
import threading

def  getConnection( ip , username , password , command , port  = 22):
    """
    :param ip: 服务器的 ip
    :param username: 服务器的用户名称
    :param password: 服务器的密码
    :param CMD: 服务器的命令
    :param port: 服务器的端口
    """
    ssh  = paramiko.SSHClient()
    policy  = paramiko.AutoAddPolicy()
    ssh.set_missing_host_key_policy(policy)
    ssh.connect(
        hostname  =  ip , # 服务器的 ip
        port  =  port , # 服务器的端口
        username  =  username , # 服务器的用户名
        password  =  password # 用户名对应的密码
    )
    stdin, stdout, stderr  = ssh.exec_command( command )
    result  = stdout.read().decode()
    error  = stderr.read().decode()
    print( "+++++++++++++++++++++++start++++++++++++++++++++")
    print( "[connect success] | ip : %s"  %  ip )
    print( "result: \n  %s" %result)
    if error  !=  " ":
        print( "error: \n %s" %error)
    print( "+++++++++++++++++++++++done++++++++++++++++++++")
    ssh.close()

#多线程
def  main( host_list , command ):
    thread_list  = []
    for ip,username,password  in  host_list :
        thread  = threading.Thread(target  = getConnection, args  =
        (ip,username,password, command ))
        thread_list.append(thread)
    for t  in thread_list:
        t.start()
    for t  in thread_list:
        t.join()

if __name__  ==  "__main__":
    host_list  = [
    ( "192.168.89.134",  "root",  "hankai"),
    ( "192.168.89.136",  "root",  "hankai"),
    ]
    # command  = sys.argv[1]
    # command  = 'cd /'
    while True:
        command  = input("请输入要执行的Linux命令：")
        main(host_list,command)
