#学习一下 模块引入
#1:  import
# 2: from...import

# import class_0807_object.class_0807_1
# #导入 引入 具体到模块名
# class_0807_object.class_0807_1.SuperBoyFriend("王思聪").coding("PHP")

#from ...import 后面具体到类名、模块名
# from class_0807_object.class_0807_1 import SuperBoyFriend
# # SuperBoyFriend("王思聪").coding("PHP")
# from class_0807_object.class_0807_1 import BoyFriend

# #多继承
# class BestBoyFriend(SuperBoyFriend,BoyFriend):
#     pass
#
# #继承顺序
# BestBoyFriend("彭于晏").coding("PHP!")


class Mother:
    def __init__(self,name):
        self.name = name
    def cooking(self):
        print("我妈： {0}是中华小当家".format(self.name))

    def running(self):
        print("我： {0}可以跑3000米".format(self.name))

class Dad:
    def __init__(self,name):
        self.name = name

    def swiming(self):
        print("我爸：{0}会游泳".format(self.name))

    def cooking(self,fish):
        print("我爸: 我只会煮方便面和{0}吃".format(fish))

#超继承  贪婪继承
class Son(Dad):
    def cooking(self,dish_name,fish):
        super(Son,self).cooking(fish)
        print("我：我做的{0}非常好吃".format(dish_name))



t = Son("summer")
t.cooking("辣椒","fish")


#调试
#1：print 掌握最快
#2：debug 难度最大 但是实用，最快可以发现bug
#3: logging 日志 手把手带你取写日志类
#可以打印你运行的情况