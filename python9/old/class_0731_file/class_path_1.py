#路径处理
#目录--> 文件夹-->路径
#相对路径  绝对路径

import os
#新建文件夹  如果是跨级，必须保证前面的路径存在，你不能跨级创建文件
# os.mkdir('python0731/test_1')#path 传入一个文件名 相对路径
#os.mkdir('python0801/test_1')  #错误师范，08001路径不存在


#删除文件夹
# os.rmdir('python0731')#必须要求文件夹里面是空的

#找路径
path_1 = os.getcwd()
#获取当前的工作路径，绝对路径，只能具体到文件夹
print(path_1)

#------------------------------
path_2 = os.path.realpath(__file__)
#获取当前的文件所在路径，绝对路径，具体到文件
print(path_2)
#------------------------------


#拆分路径
path_3 = os.path.split(path_2)[0]
path_4 = os.path.split(path_2)[1]
print('path_3: ',path_3)
print('path_4: ',path_4)

#路径拼接 os.path.join
path_5 = os.path.join(path_3,'hello','python')
print('path_5: ',path_5)

#判断当前文件夹 文件
print(os.path.isdir(path_4))#判断你输入的路径是否是文件夹
print(os.path.isfile(path_4))#判断你输入的路径是否是文件

# os.mkdir(path_5)
# 创建文件 找路径
#找到对应的目录/路径  打开文件

#保存文件