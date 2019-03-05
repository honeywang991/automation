#for循环 关键字 90%
#第一个作用 ： 遍历元素
#for item in 数据范围： #str list dict tuple 其他类型的数据范围

#str_1='python9'
#list_1=[1,3,4,5]
# tuple_1 = (1,3,4,5)
# dict_1 = {'date':'2018-7-24','class':'python9'}
# print(dict_1.keys())#访问字典里的key
# print(dict_1.values())#访问字典里的值
# for i in dict_1.values():
#     print(i)

#range函数  range(m,n,k)起始值 结束值 k步长

#range函数 生成指定范围的整数序列  数据
# range(1,8,1)#1-7
# a=list(range(1,8,1))#强制装换成列表list()
# print(a)

# a=list(range(1,8,2))#强制装换成列表list()
# print(a)

# a=list(range(4))#默认m=0 k=1 从0开始
# print(a)

# a=list(range(3,4))
# print(a)

# a=list(range(6,0,-1))#倒序
# print(a)

str_1='python9'
#如果我要用range 来打印出str_1里面的每一个元素
#我要利用下标打印出str_1的每一个元素

for i in range(7):
    print(str_1[i])
