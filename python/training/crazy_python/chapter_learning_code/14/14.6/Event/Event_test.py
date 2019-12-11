# coding: utf-8
#########################################################################
# 网站: <a href="http://www.crazyit.org">疯狂Java联盟</a>               #
# author yeeku.H.lee kongyeeku@163.com                                  #
#                                                                       #
# version 1.0                                                           #
#                                                                       #
# Copyright (C), 2001-2018, yeeku.H.Lee                                 #
#                                                                       #
# This program is protected by copyright laws.                          #
#                                                                       #
# Program Name:                                                         #
#                                                                       #
# <br>Date:                                                             #
#########################################################################
import threading
import time

event = threading.Event()
def cal(name):
    # 等待事件，进入等待阻塞状态
    print('%s 启动' % threading.currentThread().getName())
    print('%s 准备开始计算状态' % name)
    event.wait()    # ①
    # 收到事件后进入运行状态
    print('%s 收到通知了.' % threading.currentThread().getName())
    print('%s 正式开始计算！'% name)
# 创建并启动两条，它们都会①号代码处等待
threading.Thread(target=cal, args=('甲', )).start()
threading.Thread(target=cal, args=("乙", )).start()
time.sleep(2)    #②
print('------------------')
# 发出事件
print('主线程发出事件')
event.set()