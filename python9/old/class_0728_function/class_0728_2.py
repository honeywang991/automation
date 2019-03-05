#今天的主题： 讲函数 左拓展题
#1： return 关键字
#2：内置函数、函数之间的调用（先定义了才可以调用，参数的传递）
#3： 变量的作用域
#4：编写函数的三个步骤

# def add(a,b):
#     c=a+b
#     return  #返回空，下面的代码不会执行
#     print("777")
# add(1,2)

#内置函数
#print()  input()  len()  type()  int()
#str() list() range()  upper() lower()
#append()  insert() pop() sort()


#字符串的函数  strip  split  find  replace
# str_1 = "6666helloworld"
# print(str_1.strip("6"))
#strip() 什么都不传，去空格只针对字符串头和尾
#strip("指定字符串") 剔除头和尾指定的字符
#去除字符串中，指定的字符串（不只限于头尾）

#split 切割
# str_2="py,thon9,666"
# # print(str_2.split('9'))#返回的数据类型是列表
# print(str_2.split(',',1))#指定切割1刀

# #find查找字符串
# str_3="hello"
# # print(str_3.find("o")) #查找单个字符，如果存在的话，返回字符所在位置索引
# #如果没有找到，就返回-1
# print(str_3.find("llo"))#如果查找的是字符串，找到了的话，返回收个字符的索引

#replace 替换字符串
str_4="6h6l6i6k"
print(str_4.replace('6','R',2))
#指定位置替换？自己去拓展
