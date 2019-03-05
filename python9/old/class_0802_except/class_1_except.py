#bug 报错？
#程序运行，代码运行过程中遇到的错误
#1：最简单的  就是啥事不做，我只负责帮你识别错误
#try...except
#try:放你要监控的代码，except:放你对这个错误的处理
#2：处理一下 异常

# try:
#     print(a)
#     print("我是try虾米那的语句")
# except Exception as e:
#     # pass#占坑符 啥事都不做
#     print("报错啦：{0}".format(e))
#
# finally:
#     print('123')
#
# #错误基类

#3：
# try:
#     print('a')
# except Exception as e:
#     print(e)
# else:#当try下面的代码，没有报错的时候，才会执行
#     print("8啦8啦")

#4:上下问管理器  with...as
with open('test_a.txt','w+') as file:
    file.write('today is')
print(file.closed)#判断文件是否关闭

# def add(a,b):
#     try:
#         c=a+b
#     except Exception as e:
#         print("报错了%s"%e)
#     return c
# add(1,3)