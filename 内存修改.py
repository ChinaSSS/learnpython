#进程模块
import win32process
#系统
import win32con
import win32gui
import win32api
import ctypes

PROCESS_ALL_ACCESS = (0X000F0000|0x00100000|0xFFF) #位运算
#找窗体
win = win32gui.FindWindow()
#根据窗口找到进程号
hid,pid = win32process.GetWindowThreadProcessId(win)

#以最高权限打开进程
p = win32api.OpenProcess(PROCESS_ALL_ACCESS,False,pid)


#data = ctypes.c_long()
#加载内核模块
md = ctypes.windll.LoadLibrary("C:\\Windows\\System32\\kernel32")
data = ctypes.c_long()
#读取内存
md.ReadProcessMemory(int(p), ,ctypes.byref((data)),4,None)
print("data=",data)

#新值
newData = ctypes.c_long(10000)
#修改
md.WriteProcessMemory(int(p), ,ctypes.byref((newData),4,None))