#类 人类 动物类  植物类 妖类
#人以群分 物以类聚
#具有共同的属性，特性这些事物
#谁来定义类，怎么来划分类。

#python类的语法
#关键字 class
#定义一个类：
#class 类名：
    #这一类 共同的属性
    #这一类 共同的方法/行为（用函数来表达）--->类函数 or 类方法

#类名的规范：驼峰 手字符大写 jina见名知意
#BoyFriend
#MyGirl

# girl 你理想中的男朋友是怎么样的？
#帅的 高富帅 1.8 有内涵 支持你 幽默
#有钱 阳光 成熟 潜力股 有上进心
#会做饭 会Python

#男朋友类
class BoyFriend:
    #共同的属性
    money = 1000000
    height = 180

    #共同的行为
    #会做饭
    def cooking(self,order_name,order_2,language):#类函数里面的第一个参数必须是self 不代表任何参数
        self.coding(language)
        print("我男朋友会做{0}、{1}！超赞的！".format(order_name,order_2))
    #会Python
    # def coding(self):
    #     print("我的男朋友会写Python代码")

    def coding(self,language):
        print("我的男朋友会写{0}代码".format(language))

    # def sport(self,sport='爬树'):
    #     print("我男朋友喜欢{0}".format(sport))

    def sport(self,*sport):
        self.describe()#类函数之间的相互调用

        #不想要 （）括号  for  去括号
        sport_item = ''
        # while True:
        for item in sport:
            sport_item+=item
            sport_item+='、'

        # print(sport_item)
        # print(type(sport_item))
        # print(sport_item[-1].replace('、','!'))
        # sport_item_1 = sport_item[-1].replace('、','!')
        # print(sport_item_1)
        # a=sport_item.split('、')
        # print(a)
        a = sport_item[0:-1] + "!"
        # print(a)
        # a = a + "!"
        return ("我男朋友喜欢{0}".format(a))

    def describe(self):
        print("我的男朋友有存款{0}，身高是{1}".format(self.money,self.height))

#类属性和函数的调用 抽象--具体的对象  实例化
#语法： 创建一个实例  类名()
# my_by = BoyFriend()#对象/实例
# print(my_by.height)
# # print(my_by.cooking())#None 函数没有return会返回None
# my_by.cooking()

#BoyFriend().coding()


#关于类与实例的特性
#1：类里面的属性和函数，只能是由实例/对象来调用  类外面调用


#类函数的特性
#1: 类函数里面的第一个参数必须是self
#2: 可以传位置参数吗？
#3：可以传多个位置参数吗？
# BoyFriend().coding('java')
# BoyFriend().cooking("满汉全席","牛排西餐")
#4： 可以传默认参数吗？
# BoyFriend().sport()
#5: 位置参数必须是放在默认参数之前！
#6：可以传动态参数吗？可以传关键字参数吗？
#BoyFriend().sport("打篮球","跑步","打羽毛球！")
#7:类函数要调用类里面的属性，必须是这样调用 self.属性名
#BoyFriend().describe()
#8： 类函数里面： 类函数之间可以相互调用吗？必须是这样调用 self.函数名(参数值)
# BoyFriend().sport("跑步")

# BoyFriend().cooking("满汉全系","牛排西餐","PHP")
#9: 可以有return
#课堂联系
#请随意发挥 下一个软件测试工程师类
#时间：15分钟
t = BoyFriend()
t_1=t.sport("游泳","爬山","足球","散打")
print(t_1)
