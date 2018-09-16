# coding:utf-8
# 导入我们需要用到的包和类并且起别名
import datetime
import os
import sys
import time

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice, By

device = MonkeyRunner.waitForConnection()

print '****** Use Monkeyrunnner to check  receive zhiling result******'

print '---- start  App'

device.startActivity('com.backeytech.third.xiang/com.backeytech.safetycloud.ui.main.IndexActivity')

MonkeyRunner.sleep(5)

# 需要手机开启view server
easy = EasyMonkeyDevice(device)

# print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 打印时间
# 测试 流程 循环
# step1：点击跌倒报警开关
# step2：发送远程拾音
# step3：心率测量
# step4：血压测量
# step5：立即定位
# step6：精准定位

for i in range(1, 50):
    # 点击设置按钮
    easy.touch(By.id('id/pi_setting'), MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(3)
    # 点击 跌倒报警
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print '***touch fall down***'
    device.touch(600, 580, 'DOWN_AND_UP')
    MonkeyRunner.sleep(3)
    # 点击返回到主页
    easy.touch(By.id('id/left_image'), MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(3)
    # 点击微聊 发送远程拾音
    device.touch(300, 1000, 'DOWN_AND_UP')
    MonkeyRunner.sleep(2)
    easy.touch(By.id('id/btn_more'), MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print '*** get vice ***'
    easy.touch(By.id('id/image'), MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    # 点击返回到主页
    easy.touch(By.id('id/left_image'), MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(4)
    # 跳转到心率，开始检测心率
    easy.touch(By.id('id/pi_ll_beatheart'), MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(3)
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print '*** start hr ***'
    easy.touch(By.id('id/btn_start_check_hr'), MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(5)
    # 点击血压页面，开始血压检测
    # easy.touch(By.id('id/tv_item_bp'), MonkeyDevice.DOWN_AND_UP)
    device.touch(500, 200, 'DOWN_AND_UP')
    MonkeyRunner.sleep(5)
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print '*** start bp ***'
    easy.touch(By.id('id/btn_start_check_bp'), MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    # 点击返回到主页
    device.touch(50, 100, 'DOWN_AND_UP')
    MonkeyRunner.sleep(5)
    # 进入定位页面 立即定位和精准点位
    device.touch(600, 900, 'DOWN_AND_UP')
    MonkeyRunner.sleep(5)
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print '*** get location ***'
    easy.touch(By.id('id/iv_reload_location'), MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(12)
    easy.touch(By.id('id/iv_focus'), MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print '*** start gps dm ***'
    device.touch(600, 700, 'DOWN_AND_UP')
    # easy.touch(By.id('id/button1'), MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    # 点击返回到主页
    device.touch(50, 100, 'DOWN_AND_UP')
    # easy.touch(By.id('id/left_image'), MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(3)
    print'----A round of testing is completed-----'
    print 'this is ', i, 'times'

