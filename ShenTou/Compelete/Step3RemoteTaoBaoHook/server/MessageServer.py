# -*- coding: utf-8 -*-

import socket

def hook_tcp_server():
    '''''
    Function:接收远程机器上发送过来的信息并输入出到终端
    Input：even
    Output: Ture
    author: socrates
    blog:http://blog.csdn.net/dyx1024
    date:2012-03-03
    '''

    host = '222.20.40.25'
    port = 34586
    buf_size = 1024
    addr =(host, port)

    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(addr)
    tcp_server_socket.listen(5)

    print 'waiting for connectiong...'
    while True:
        tcp_client_socket, addr = tcp_server_socket.accept()
        print 'connected from :', addr
        while True:
            msg = tcp_client_socket.recv(buf_size)
            print msg
            if not msg:
                break
        tcp_client_socket.close()    #出错误的话，可以把这句注释掉，不让程序关掉客户端的socket
    tcp_server_socket.close()

if __name__ == '__main__':
    hook_tcp_server()