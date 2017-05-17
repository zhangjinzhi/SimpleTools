# -*- coding: utf-8 -*-

import socket
import struct
import time

def hook_pic_file_server():
    '''''
    Function:接收远程机器上发送过来的图片并保存到本地
    Input：even
    Output: Ture
    author: socrates
    blog:http://blog.csdn.net/dyx1024
    date:2012-03-03
    '''

    host = '222.20.40.25'
    port = 34587
    buf_size = 1024
    addr =(host, port)
    pic_file_size_info = struct.calcsize('128s32sI8s')

    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(addr)
    tcp_server_socket.listen(5)

    print 'waiting for connectiong...'
    while True:
        tcp_client_socket, addr = tcp_server_socket.accept()
        print 'connected from :', addr

        pic_file_head = tcp_client_socket.recv(pic_file_size_info)

        #接收文件头信息
        pic_file_name, temp1, pic_file_size, temp2 = struct.unpack('128s32sI8s', pic_file_head)
        local_pic_dir = pic_file_name.strip('\0')

         #接收文件内容
        pic_fobj = open(local_pic_dir, 'wb')
        temp_file_size = pic_file_size
        while True:
            if temp_file_size > buf_size:
                pic_file_data = tcp_client_socket.recv(buf_size)
            else:
                pic_file_data = tcp_client_socket.recv(temp_file_size)

            if pic_file_data:
                pic_fobj.write(pic_file_data)
                temp_file_size -= len(pic_file_data)
            if temp_file_size == 0:
                       break
        pic_fobj.close()
        print time.strftime('[%Y-%m-%d %H:%M:%S]: ',time.localtime(time.time()))+ local_pic_dir + ' was received'

        tcp_client_socket.close()  #出错误的话，可以把这句注释掉，不让程序关掉客户端的socket
    tcp_server_socket.close()

if __name__ == '__main__':
    hook_pic_file_server()