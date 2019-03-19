"""控制窗体(QQ)"""

import win32con
import win32gui
import time

#找出QQ的窗体编号
QQWin = win32gui.FindWindow("TXGuiFoundation","QQ")#窗体的class 和 标题
time.sleep(2)
#显示窗体
win32gui.ShowWindow(QQWin,win32con.SW_HIDE)
time.sleep(2)

#显示窗体
win32gui.ShowWindow(QQWin,win32con.SW_SHOW)
