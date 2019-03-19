import os

# print(os.name) #获得电脑的类型 nt--windows
# print(os.environ) #获取操作系统的环境变量
# print(os.environ.get()) #获取特定的环境变量

#获取当前目录  ./a/
# print(os.curdir)
#获取当前工作目录
# print(os.getcwd()) #current working driectory
#列出指定目录下的所有文件
# print(os.listdir(r'D:\python'))
#建立目录
# os.mkdir("good")
# os.rmdir("good")

#获取文件属性
# print(os.stat("space.txt"))
#重命名
# os.rename("space2.txt","space1.txt")
#删除普通文件
# os.remove(filename)
#运行系统命令
# os.system("shutdown -s -t 500")
# os.system("shutdown -a")
#查看当前下文件的绝对路径
# print(os.path.abspath("./test.py"))
# os.path.join(dir,filename)
#拆分路径
# print(os.path.split(r'D:\python\python'))
#判断是否是目录
# print(os.path.isdir(r'D:\python'))
#判断文件是否存在
# print(os.path.isfile(path))
#判断目录是否存在
# print(os.path.exists(r'D:\a'))
#获取文件大小
# print(os.path.getsize(('space.txt')))
