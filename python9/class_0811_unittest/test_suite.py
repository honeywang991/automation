#coding=utf-8
#error 代码错误
#fail期望值与实际值不对等

import unittest
from class_0811_unittest.test_math_method import TestMathMethod
from class_0811_unittest import test_math_method#具体到模块名
# import HTMLTestRunnerNew
# import BSTestRunner
import HTMLTestRunner

if __name__ == '__main__':
    test_data=[{"a":4,"b":5,"expected":9},
               {"a":-4,"b":-5,"expected":-9},
               {"a":0.2,"b":0.1,"expected":0.3},
               {"a":1,"b":'',"expected":0.3}
               ]
    #收集测试用例
    suite=unittest.TestSuite()#创建了一个测试套件，专门收集测试用例

    #suite必须在for循环外面
    for item in test_data:#遍历测试数据test_data
        suite.addTest(TestMathMethod('test_add',item['a'],item['b'],item['expected']))



    # 第一种方法：添加指定的用例
    # suite.addTest(TestMathMethod('test_add_two_positive'))#添加了第一条用例
    # suite.addTest(TestMathMethod('test_add_two_negative'))#添加了第2条用例
    # suite.addTest(TestMathMethod('test_add_two_float'))#添加了第3条用例
    # suite.addTest(TestMathMethod('test_add_one_arg'))#添加了第4条用例



    # #第二种方法：loader去加载用例 TestLoader
    # loader=unittest.TestLoader()#实例
    # # suite.addTests(loader.loadTestsFromModule(test_math_method))#导入需要具体到模块名，不是类名
    #
    # suite.addTests(loader.loadTestsFromTestCase(TestMathMethod))#导入需要具体到类名
    #
    # # file=open('test_result.txt','a+',encoding='utf-8')
    # # #执行测试用例  TextTestRunner 专门执行测试用例的类
    # # runner=unittest.TextTestRunner(stream=file,descriptions="123",verbosity=2)
    # # runner.run(suite)

    file=open('test_report.html','wb+')
    runner=HTMLTestRunner.HTMLTestRunner(file,title='python9期')
    runner.run(suite)


#梳理单元测试
#1： 写测试用例 TestCase 继承它  去写测试用例 test_开头
#断言？ 异常判断？ 参数化？
#2：创建测试套件 TestSuite -->addTests去添加用例
# 方法一  实例
# 方法二  loader
#3:执行测试用例 出具测试报告 runner  指定文件的名字 打开模式file

#难点 : 参数化， 超继承__init__? 为什么要参数化？


