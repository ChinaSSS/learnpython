"""编码"""
path="space.txt"
with open(path,"wb") as f:
    str="i am ironman"
    f.write(str.encode('utf-8'))

with open(path,'rb') as f:
    data=f.read()

print(data)
print(type(data))
newdata=data.decode("utf-8")
print(newdata)
print(type(newdata))