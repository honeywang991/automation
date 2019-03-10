#coding=utf-8
# 作者:Administrator
#ddt  data driver testing 数据驱动测试
#pip install ddt

#动态参数
# def print_msg(*args):
#     print(args)
#     print('args的类型是{0}'.format(type(args)))
#     print('args的类型是{0}'.format(len(args)))

# print_msg('tiger','shenlan','21','65')

# a=['tiger','shenlan','21','65']
# print_msg(*a)

# a=[['tiger','shenlan'],['21','65']]
# print_msg(a)

#关键字参数
# def print_msg(**kwargs):
#     print(kwargs)
#     print('args的类型是{0}'.format(type(kwargs)))
#     print('args的类型是{0}'.format(len(kwargs)))
# a={'x':1,'y':2}
# print_msg(**a)



from ddt import ddt,data,unpack
import unittest
# test_data=[[1,2],[3,4],[1,0]]
# test_data_1=[[1,1],[3,3]]
# test_data = [{'age':18,'sex':'girl','money':100,'name':'honey'},
#              {'age':20,'sex':'boy','money':10,'name':'tom'}]
test_data = [[1,2,'girl1','girl2'],[3,'girl3',4,'girl4']]
@ddt#装饰测试类
class TestAdd(unittest.TestCase):

    @data(*test_data)#装修测试方法  测试用例
    #拆分数据的功能
    @unpack#再次进行拆分     #@unpack#再次进行拆分
    def test_add(self,age,sex,money,name):#参数传递进来
        #如果unpack的是字典  ，那么变量名要跟key一致
        # print("传进来的参数是",a)
        # print("传进来的参数是", type(a))
        # print(a[0]+a[1])
        print("age是：{0}".format(age))
        print('sex是： {0}'.format(sex))
        print("money是：{0}".format(money))
        print("name是：{0}".format(name))
        # a=1
        # b=2
        # print(a+b)

    # @data(*test_data_1)#装修测试方法  测试用例
    # #拆分数据的功能
    #
    # def test_add_1(self,item):
    #     print("传进来的参数是",item)
    #     print("传进来的参数是", type(item))
    #     print(item[0]+item[1])


#=================
#执行该文件 请把光标放在此处
#@unpack  除了字典不能胡来，其他可以想咋搞咋搞，有几个参数传几个参数

