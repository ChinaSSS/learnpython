#print(int("100",base=2)) 将100按二进制计算
#偏函数，固定一个函数参数来生成一个函数

import functools

int2=functools.partial(int,base=2)
print(int2("100"))