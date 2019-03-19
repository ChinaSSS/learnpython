
import win32con
import win32gui
import time
import random


#找到窗口
QQWin = win32gui.FindWindow("TXGuiFoundation","QQ")#

#arg1 : 控制的窗体
#arg2 : 大致方位
#arg3 : 位置x
#arg4 : 位置y
#arg5 : 长度
#arg6 : 宽度
while True:
    x=random.randrange(900)
    y=random.randrange(600)
    win32gui.SetWindowPos(QQWin,win32con.HWND_TOPMOST,x,y,600,300,win32con.SWP_SHOWWINDOW)