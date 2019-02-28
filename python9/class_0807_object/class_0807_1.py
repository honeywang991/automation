class BoyFriend:
    #初始化函数里面可以放属性值
    def __init__(self,money,height=170): #出厂设置
        self.money = money
        self.height = height

    #共同的行为
    #会做饭
    def cooking(self,order_name,order_2,language):#类函数里面的第一个参数必须是self 不代表任何参数
        self.coding(language)
        print("我男朋友会做{0}、{1}！超赞的！".format(order_name,order_2))

    def coding(self,language):
        print("我的男朋友会写{0}代码".format(language))

    def sport(self,*sport):
        # self.describe()#类函数之间的相互调用

        #不想要 （）括号  for  去括号
        sport_item = ''
        # while True:
        for item in sport:
            sport_item+=item
            sport_item+='、'

        a = sport_item[0:-1] + "!"
        return ("我男朋友喜欢{0}".format(a))

    def describe(self):
        print("我的男朋友有存款{0}，身高是{1}".format(self.money,self.height))


#特殊的函数： 初始化函数
#__init__() #初始化函数 跟普通函数是一样
# t=BoyFriend(1000,180)
# t.coding('python')
# print(t.height)
# print(t.money)

#继承：重写 & 拓展
class SuperBoyFriend(BoyFriend):

    #重写 1： 子类里面的函数名与父类函数名一样，那么就直接覆盖父类的写法
    #2: 重写是针对有需要做修改的父类里面的函数
    def __init__(self,name):
        self.name=name

    def coding(self,language):
        print("我的男朋友{0}会写{1}代码".format(self.name,language))

    def fly(self):# 拓展： 父类里面没有的函数，但是子类有，这个叫拓展
        print(self.sport("篮球","游泳"))#这个操作经常用，所以请注意！！！
        self.coding('JAVA')
        print("可以飞到珠穆拉马蜂")

#爸爸的就是我的
#SuperBoyFriend 子类    BoyFriend 父类
if __name__ == '__main__':#函数执行的入口

    t = SuperBoyFriend("王思聪")
    # t.coding('python')
    # print(t.name)
    # print(t.sport("游泳","打球"))
    t.fly()

#只有在执行当前模块的时候 main里面的代码才会被执行
#如果在别的页面调用这个模块，代码也不会被执行
