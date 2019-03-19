"""把一个函数做参数传入，返回一个函数"""

def getage(age):
    print("your age is %s years old"%(age))

def panduan(func):
    def inner(age):
        if age<0:
            print("is error")
        else:
            func(age)
    return inner

age = panduan(getage)
age(5)