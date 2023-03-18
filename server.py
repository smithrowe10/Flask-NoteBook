# -*- coding = utf-8 -*-
# @Time : 2022/9/20 13:55
# @Author : name
# @File : server.py
# @software : PyCharm
import socket

host = '127.0.0.1'  # 主机ip
port = 8086
web = socket.socket()
web.bind((host, port))  # 绑定端口
web.listen(5)  # 设置最多连接数
print('服务器等待客户端连接...')
while True:
    conn, addr = web.accept()  # 建立客户端连接
    data = conn.recv(1024)  # 获取客户端请求数据
    print(data)
    conn.sendall(b'HTTP/1.1 200 OK\r\n\r\n Hello World')  # 向客户端发送数据
    conn.close()  # 关闭连接
