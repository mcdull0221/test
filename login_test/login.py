# coding:utf-8
# 导入我们需要用到的包和类并且起别名
import datetime
import os
import sys
import time

from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi
from com.android.monkeyrunner import MonkeyRunner as mr

# connect device 连接设备
# 第一个参数为等待连接设备时间
# 第二个参数为具体连接的设备
device = mr.waitForConnection(1.0, '4318610e')
print 'connection success'

device.installPackage('E:/apk/Application/pinganyun.apk')
mr.sleep(15.0)
print 'install success'

# 直接点击屏幕上app启动，用下面的方法启动较慢
device.touch(300, 500, 'DOWN_AND_UP')
mr.sleep(8.0)

# 启动特定的Activity
#device.startActivity(component='com.snowball.sshome/com.backeytech.safetycloud.ui.SplashActivity')
#mr.sleep(8.0)
print 'start success'

# 拖动引导图
device.drag((600, 500), (130, 500), 0.5, 10)
mr.sleep(2)
device.drag((600, 500), (130, 500), 0.5, 10)
mr.sleep(2)
device.drag((600, 500), (130, 500), 0.5, 10)
mr.sleep(2)

# 空内容点击登录
device.press('KEYCODE_BACK', 'DOWN_AND_UP')
mr.sleep(0.5)
device.touch(300, 700, 'DOWN_AND_UP')
mr.sleep(0.5)
login = device.takeSnapshot()
login.writeToFile('F:\jietu\login.png', 'png')
mr.sleep(1)

# 点击账号栏输入内容，点击登录
device.touch(300, 500, 'DOWN_AND_UP')
mr.sleep(0.5)
device.type('1445555')
mr.sleep(0.5)
device.touch(300, 700, 'DOWN_AND_UP')
mr.sleep(0.5)
loginerror = device.takeSnapshot()
loginerror.writeToFile('F:/jietu/loginerror.png', 'png')
mr.sleep(1)
# 登录密码错误
device.touch(300, 500, 'DOWN_AND_UP')
mr.sleep(0.5)
device.type('5555')
mr.sleep(0.5)
device.touch(300, 600, 'DOWN_AND_UP')
mr.sleep(0.5)
device.type('123457')
mr.sleep(0.5)
device.touch(300, 700, 'DOWN_AND_UP')
mr.sleep(0.5)
loginerror1 = device.takeSnapshot()
loginerror1.writeToFile('F:/jietu/loginerror1.png', 'png')
mr.sleep(1)
# 这里的backeyup是为了关闭输入法
device.press('KEYCODE_BACK', 'DOWN_AND_UP')

# 点击注册会员，跳转到注册页面
device.touch(130, 800, 'DOWN_AND_UP')
mr.sleep(2)

# 空手机号码和邮箱 点击获取验证码
device.touch(600, 300, 'DOWN_AND_UP')
mr.sleep(0.5)
# 进行截图
login1 = device.takeSnapshot()
# save to file 保存到文件
login1.writeToFile('F:\jietu\login1.png', 'png')
mr.sleep(1)

# 点击手机号一栏
device.touch(60, 200, 'DOWN_AND_UP')
# 输入内容
device.type('1375555')
mr.sleep(0.5)
#  点击获取验证码
device.touch(600, 300, 'DOWN_AND_UP')
mr.sleep(0.5)
# 进行截图
login2 = device.takeSnapshot()
# save to file 保存到文件
login2.writeToFile('F:\jietu\login2.png', 'png')
mr.sleep(1)

# 输入手机号 点击注册
device.touch(300, 200, 'DOWN_AND_UP')
mr.sleep(0.5)
device.type('6666')
mr.sleep(0.5)
device.touch(300, 700, 'DOWN_AND_UP')
mr.sleep(0.5)
login3 = device.takeSnapshot()
login3.writeToFile('F:\jietu\login3.png', 'png')
mr.sleep(1)

# 继续输入验证码点击注册
device.touch(300, 300, 'DOWN_AND_UP')
mr.sleep(0.5)
device.type('123456')
mr.sleep(0.5)
device.touch(300, 700, 'DOWN_AND_UP')
mr.sleep(0.5)
login4 = device.takeSnapshot()
login4.writeToFile('F:\jietu\login4.png', 'png')
mr.sleep(1)

# 继续输入昵称点击注册
device.touch(300, 400, 'DOWN_AND_UP')
mr.sleep(0.5)
device.type('test123456')
mr.sleep(0.5)
device.touch(300, 700, 'DOWN_AND_UP')
mr.sleep(0.5)
login5 = device.takeSnapshot()
login5.writeToFile('F:\jietu\login5.png', 'png')
mr.sleep(1)

# 点击密码输入3位
device.touch(300, 500, 'DOWN_AND_UP')
mr.sleep(0.5)
device.type('123')
mr.sleep(0.5)
device.touch(300, 700, 'DOWN_AND_UP')
mr.sleep(0.5)
login6 = device.takeSnapshot()
login6.writeToFile('F:\jietu\login6.png', 'png')
mr.sleep(1)

# 点击密码 继续输入内容
device.touch(300, 500, 'DOWN_AND_UP')
mr.sleep(0.5)
device.type('456')
mr.sleep(0.5)
device.touch(300, 700, 'DOWN_AND_UP')
mr.sleep(0.5)
login7 = device.takeSnapshot()
login7.writeToFile('F:\jietu\login7.png', 'png')
mr.sleep(1)

# 点击确认密码输入内容1234
device.touch(300, 600, 'DOWN_AND_UP')
mr.sleep(0.5)
device.type('1234')
mr.sleep(0.5)
device.touch(300, 700, 'DOWN_AND_UP')
mr.sleep(0.5)
login8 = device.takeSnapshot()
login8.writeToFile('F:\jietu\login8.png', 'png')
mr.sleep(1)

# 点击左上角返回按钮
device.touch(50, 100, 'DOWN_AND_UP')
mr.sleep(3)
# 跳转到忘记密码页面
device.touch(500, 800, 'DOWN_AND_UP')
mr.sleep(3)

# 空内容点击确定
device.touch(300, 600, 'DOWN_AND_UP')
mr.sleep(1)
login9 = device.takeSnapshot()
login9.writeToFile('F:\jietu\login9.png', 'png')
mr.sleep(1)

# 手机号输入139 点击确定
device.touch(300, 200, 'DOWN_AND_UP')
mr.sleep(0.5)
device.type('144')
mr.sleep(0.5)
device.touch(300, 600, 'DOWN_AND_UP')
mr.sleep(1)
login10 = device.takeSnapshot()
login10.writeToFile('F:\jietu\login10.png', 'png')
mr.sleep(1)

# 输入未注册的手机号 点击获取验证码
device.touch(300, 200, 'DOWN_AND_UP')
mr.sleep(0.5)
device.type('99999999')
mr.sleep(1)
device.touch(450, 200, 'DOWN_AND_UP')
mr.sleep(1)
login11 = device.takeSnapshot()
login11.writeToFile('F:\jietu\login11.png', 'png')
mr.sleep(1)

# 继续输入验证码 点击确定
device.touch(300, 300, 'DOWN_AND_UP')
mr.sleep(0.5)
device.type('123456')
mr.sleep(0.5)
device.touch(300, 600, 'DOWN_AND_UP')
mr.sleep(1)
login12 = device.takeSnapshot()
login12.writeToFile('F:\jietu\login12.png', 'png')
mr.sleep(1)

# 点击密码 输入123 点击确定
device.touch(300, 400, 'DOWN_AND_UP')
mr.sleep(0.5)
device.type('123')
mr.sleep(0.5)
device.touch(300, 600, 'DOWN_AND_UP')
mr.sleep(1)
login13 = device.takeSnapshot()
login13.writeToFile('F:\jietu\login13.png', 'png')
mr.sleep(1)

# 继续点击密码栏，输入4567 点击确定
device.touch(300, 400, 'DOWN_AND_UP')
mr.sleep(0.5)
device.type('4567')
mr.sleep(0.5)
device.touch(300, 600, 'DOWN_AND_UP')
mr.sleep(1)
login14 = device.takeSnapshot()
login14.writeToFile('F:\jietu\login14.png', 'png')
mr.sleep(1)

# 点击确认密码栏，输入123 点击确定
device.touch(300, 500, 'DOWN_AND_UP')
mr.sleep(0.5)
device.type('123')
mr.sleep(0.5)
device.touch(300, 600, 'DOWN_AND_UP')
mr.sleep(1)
login15 = device.takeSnapshot()
login15.writeToFile('F:\jietu\login15.png', 'png')
mr.sleep(1)

print 'end'
