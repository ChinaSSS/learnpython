# import pickle #数据持久性模块
#
# myList = [1,2,3,4,'you are a good man']
# path = "space.txt"
#
# #写入
# f=open(path,"wb")
# pickle.dump(myList,f)
# f.close()
#
# #读取
# f1=open(path,"rb")
# tempList=pickle.load(f1)
# print(tempList)
# f1.close()
# #写进去后文件看不懂但是读出来就好了

import json
path="space.txt"
myList=[1,2,3,4,'dogs']
with open(path,'w') as f:
    f.write(json.dumps(myList,ensure_ascii=False))

with open(path,'r') as f:
    print(json.loads(f.read()))
