# -*- coding: UTF-8 -*-

import socket
import time
import traceback
from VideoCapture import Device
import threading

# 全局变量
is_sending = False
cli_address = ('', 0)

# 主机地址和端口
host = ''
port = 1234

# 初始化UDP socket
ser_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ser_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ser_socket.bind((host, port))

# 接收线程类，用于接收客户端发送的消息
class UdpReceiver(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.thread_stop = False

    def run(self):
        while not self.thread_stop:
            # 声明全局变量，接收消息后更改
            global cli_address
            global is_sending
            try:
                message, address = ser_socket.recvfrom(2048)
            except:
                traceback.print_exc()
                continue
       #     print message,cli_address
            cli_address = address
            if message == 'startCam':
                print 'start camera',
                is_sending = True
                ser_socket.sendto('startRcv', cli_address)
            if message == 'quitCam':
                is_sending = False
                print 'quit camera',

    def stop(self):
        self.thread_stop = True

# 创建接收线程
receiveThread = UdpReceiver()
receiveThread.setDaemon(True)           # 该选项设置后使得主线程退出后子线程同时退出
receiveThread.start()

# 初始化摄像头
cam = Device()
#cam.setResolution(320,240)

# 主线程循环，发送视频数据
while 1:
    if is_sending:
        img = cam.getImage().resize((160,120))
        data = img.tostring()
        ser_socket.sendto(data, cli_address)
        time.sleep(0.05)
    else:
        time.sleep(1)

receiveThread.stop()
ser_socket.close()