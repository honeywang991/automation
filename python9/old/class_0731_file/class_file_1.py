# #open()函数 可以新建文件
# #txt 文本文件
# # file = open('test_1.txt','w+',encoding='utf-8')
# # file = open('test_1.txt','w+')
# file = open('test_1.txt','r+',encoding='utf-8')#如果是直接读的话，那就是从头开始读
# result=file.read()#如果先读在写，那就是根据光标的位置走
# print(result)
# file.write('today is a sunny day ')

#1： r 只读  r+读写  文件必须要存在
#2： w 只写 w+读写 文件存在的话，就直接清空覆盖重写
# if 文件不存在，就直接新建一个文件进行写操作
#3：a 写  a+读写   追加 append
#文件存在的话，就直接追加内容在后面
#if 文件不存在，就直接新建一个文件进行写操作

# # file.write("adsdsadsad")#可以写多行数据吗？
# # file.write("adsdsa\ndsad")#换行的写法
# file.writelines(['8888\n','777\n','999\n'])#传入列表类型的数据
# #要实现写入多行的功能，就要加\n
#
#
# #w+ w 方式写完数据后，鼠标在最后面
# #位置跟你鼠标的位置有关
# s=file.tell()
# print(s)
# #可以挪一下光标吗
# # file.seek(0,0) #第一个参数 是偏移量，第二个参数是相对位置
# file.seek(0,0)
# #第二个参数有3个取值 0头部   1中间  2尾部
# #重新读取内容
# result = file.read()
# print(result)

# file = open("test_a.txt",'a+')
# # file.write('8888')
# # result = file.read()#先写在读，是无法读出内容的
# # print(result)
# file.close()

# file = open('test_a.txt','r')
# res = file.readlines()#返回列表
# #每一行的数据存到列表里面
# print(res)


file = open('test_a.txt','a',encoding='utf-8')
file.write('Python9979期')
file.close()