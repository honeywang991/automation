#函数
#type()   print()  input() len() str()
#列表 append() pop() insert(i,value)
#range() upper()   lower()

#函数的特点：
#1：拿来 就可以用  内置的函数 直接可以调用
#2: 不需要定义 想用就用

#函数的语法：
#def 函数名(参数1，参数2，参数3，........):
    #函数体（你要该函数实现的功能是什么？）

#函数的调用：函数名(参数1，参数2，参数3)

#入门级函数
# def print_msg(): #定义函数
#     print("12345")
#
# print_msg()#调用函数

#加参数的函数  #形参  调用的时候是实参
#默认参数必须放在位置参数（形参）的后面
#形参是按顺序赋值的
# def greet_user(content,name='铁鹰'):
#     print(name+content)
#
# greet_user(',晚上好')
#如果你不传参，那我就取默认值，如果你参了，选你的值
#函数运行的结果是：函数体的代码执行的结果
#默认参数可以有无数了，按着语法来就可以


#动态参数 你想加几个就加几个
# def add(*args):
#     print(args)
#     sum=0
#     for i in args:
#         sum+=1
#     print(sum)
# add(1,2,3,4)


#关键字参数 **kwargs keyword
# def priny_msg(**kwargs):
#     print(kwargs)
#
# priny_msg(x=1,y=2)

#return 关键字 返回一个值

def add_2(x,y):
    return x+y#返回值 如果你想拿到这个值？用变量去接收
    print("123")#return后面的代码不执行

def add_1(a):
    b=add_2(6,5)#函数的调用
    print(a+b)


add_1(5)
# result=add_2(6,6)
# print(result)

