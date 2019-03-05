#coding=utf-8
#@Time : 2018/7/19 20:16
#@Author : lemon huahua
#@Email :
#@File : class_basic.py
#命名的规范
#1：项目名 project name
#2: 包名 package name 把一些代码存放在一个包里面 方便管理代码
#3: 模块名 py文件 module name
#规范： 1：命名不能以数字开头
        #2：数字 字母 下划线组成（中文 ￥#@  不要包含进来）
        #3：一般字母都是小写的
        #4：不同的字母之间是用下划线
        #5：模块名 项目名 包名 变量名都不能使用关键字
        #都要遵守1-5这几个规则
        #classbasic  class_basic
#语法：

#变量 x=1 y=5
# 单行注释
# a=1
# print(a)#把内容输出到控制台
#如果要引用变量，先声明赋值，在引用

#数据类型 整数 浮点数 字符串
#整数 int  type(你要判断的值) 获取数据的类型
# a=1
# print(type(a))

#浮点数 关键字 float
# f=0.2
# print(type(f))

#字符串 关键字str
#字符 字符串 没有区别
#凡是成对的单引号 或者引号 引起来的都是字符串
# s='hello python'
# s="'hello' python"
# s_2 = "8"
# print(type(s_2))
#请不要用中问的字符

 #布尔值 boolean True False
 #布尔值 必须是首字母大写

 #拼接 字符串之间的拼接
# s_1 = "hello"
# s_2 = "python"
# print(s_1+" 123 "+s_2)
#字符串要拼接起来  可以直接用+

#如果不是字符串？不同类型之间的拼接
#字符串 与整数拼接  1： 加逗号
# s_1 = "hh"
# a = 1
# print(s_1,a)#这叫输出2个变量的值 变量和变量之间用逗号隔开
# print(s_1 + str(a))

#格式化输出
#{0} 占了一个坑 表示这里要填入一个值
# name = '太阳'
# name_2 = '猜猜'
# print("python 9期有一个学生的名字叫做：{0}、{1}".format(name,name_2))

#%s %d  %f

#常用数据类型List&Tuple&dict(一)（1）