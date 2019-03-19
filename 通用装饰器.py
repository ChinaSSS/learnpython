
def outer(func):
    def inner(*args,**kwargs):
        #添加修饰的功能
        print("#############")
        func(*args,**kwargs)
    return inner

@outer
def say(name,age):
    print(" my name is %s ,and my age is %s"%(name,age))


say("zhang",18)