# -*- coding = utf-8 -*-
# @Time : 2022/9/20 14:33
# @Author : name
# @File : udp_client.py
# @software : PyCharm

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = input('请输入数据:')
s.sendto(data.encode(), ('127.0.0.1', 8888))
print(s.recv(1024).decode())
s.close()
