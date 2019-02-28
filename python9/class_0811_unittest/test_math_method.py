#coding=utf-8
import unittest #引入Python的单元测试模块
from unittest  import TestCase
from class_0811_unittest.math_method import MathMethod #测试目标类

#针对加法  你会想到那些测试点？ 开始写用例
#类型 参数的个数 大小
#1：输入两个正数
#2：输入两个负数
#3：输入一个参数
#4:只输入一个参数
#TestCase  专门来写测试用例的    我们会把测试用例组织在测试类里面
#用例是作为测试类一个个的函数

class TestMathMethod(TestCase):#里面放测试用例  继承

    def __init__(self,methodName,a,b,expected):
        super(TestMathMethod,self).__init__(methodName)
        self.a=a
        self.b=b
        self.expected=expected

    def setUp(self):
        print("hello start")

    def test_add(self):
        result=MathMethod().add(self.a,self.b)
        try:
            self.assertEqual(self.expected,result)
        except AssertionError as e:
            print("执行用例的时候出错了，报错是：{0}".format(e))
            raise
        else:
            print("测试执行结果是：{0}".format(result))

    # #写用例 test_ 前缀 以这个开头
    # def test_add_two_positive(self):#1：输入两个正数
    #     result=MathMethod().add(4,5)
    #     self.assertEqual(9,result)
    #     print("我正在执行加法运算，结果是：{0}".format(result))
    #
    # def test_add_two_negative(self):#2：输入两个负数
    #     result=MathMethod().add(-4,-5)
    #     self.assertEqual(-9, result)
    #     print("我正在执行加法运算，结果是：{0}".format(result))
    #
    # def test_add_two_float(self):#3：输入两个小数
    #     result=MathMethod().add(0.1,0.2)
    #     try:
    #         self.assertEqual(0.3, result)
    #     except Exception as e:
    #         print("执行用例出错了{0}".format(e))
    #
    #         raise e #抛出错误
    #
    #     print("我正在执行加法运算，结果是：{0}".format(result))
    #
    # def test_add_one_arg(self):#4：输入一个参数
    #     result=MathMethod().add(0.2)
    #     try:
    #         self.assertEqual(None, result)
    #     except Exception as e:
    #         print("执行用例出错了{0}".format(e))
    #     print("我正在执行加法运算，结果是：{0}".format(result))

    def tearDown(self):
        print("hello finish")

if __name__ == '__main__':

    #收集测试用例
    suite=unittest.TestSuite()#创建了一个测试套件，专门收集测试用例
    suite.addTest(TestMathMethod('test_add_two_positive'))#添加了第一条用例
    # suite.addTest(TestMathMethod('test_add_two_negative'))#添加了第2条用例
    # suite.addTest(TestMathMethod('test_add_two_float'))#添加了第3条用例
    # suite.addTest(TestMathMethod('test_add_one_arg'))#添加了第4条用例
    #

    #执行测试用例  TextTestRunner 专门执行测试用例的类
    runner=unittest.TextTestRunner()
    runner.run(suite)