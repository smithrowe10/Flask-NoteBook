# -*- coding = utf-8 -*-
# @Time : 2022/9/20 14:24
# @Author : name
# @File : udp_server.py
# @software : PyCharm
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 8888))
print('绑定UDP到8888端口')
data, addr = s.recvfrom(1024)
send_data = str(data)
s.sendto(send_data.encode(), addr)
s.close()
