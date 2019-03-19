"""装饰器"""

#装饰器
def outer(func):
    def inner(age):
        if age < 0:
            print("input error")
        else:
            func()
    return inner


@outer #相当于age=outer(age)
def age(age):
    print("you age is %s years old "%(age))

age(-10)