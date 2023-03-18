# -*- coding = utf-8 -*-
# @Time : 2022/9/20 14:05
# @Author : name
# @File : client.py
# @software : PyCharm
import socket

host = '127.0.0.1'  # 获取主机地址
port = 8086
s = socket.socket()
s.connect((host, port))  # 主动初始化TCP服务器连接
send_data = input('请输入要发送的数据:')
s.send(send_data.encode())

recvData = s.recv(1024).decode()
print('接收到的数据为:', recvData)
s.close()
