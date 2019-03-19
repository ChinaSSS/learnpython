"""人开枪射击"""
#创建一个弹夹类
class Box(object):
    def __init__(self,acount):
        self.acount=acount

#创建枪类
class Gun(object):
    def __init__(self,box):
        self.box=box

    def fire(self):
        if self.box.acount == 0:
            print("没有子弹了！！！")
        else:
            self.box.acount-=1
            print("BOOM!!!")
            print("剩余子弹 %s 发"%(self.box.acount))

#创建人类
class Person(object):
    def __init__(self,gun):
        self.gun=gun

    def fire(self):
        self.gun.fire()

    def fill(self,num):
        self.gun.box.acount+=num

#创建实例进行模拟
box = Box(5)
gun = Gun(box)
per = Person(gun)

#开枪射击
for i in range(3):
    per.fire()

per.fill(5)
per.fire()

