# -*- coding:utf-8 -*-
from VideoCapture import Device
import time, string
interval = 2

cam = Device(devnum=0, showVideoWindow=0)

#cam.setResolution(648, 480)
cam.saveSnapshot('image.jpg', timestamp=3, boldfont=1, quality=75)

i = 0
quant = interval * .1
starttime = time.time()
while 1:
    lasttime = now = int((time.time() - starttime) / interval)
    print i
    cam.saveSnapshot('image.jpg', timestamp=3, boldfont=1)

    i += 1
    while now == lasttime:
        now = int((time.time() - starttime) / interval)
        time.sleep(quant)