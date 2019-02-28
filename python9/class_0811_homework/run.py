import unittest
import HTMLTestRunner
# from class_0811_homework import ReadData
# from class_0811_homework import TestMath
from class_0811_homework.read_data_1 import ReadData
from class_0811_homework.math_method import TestMath
#C:\Users\Administrator\Desktop\gitwork\python9\class_0811_homework\math_method.py

test_data=ReadData().read_data()#测试数据
suite = unittest.TestSuite()

for item in test_data:
    suite.addTest(TestMath('test_add',eval(item)['a'],eval(item)['b'],eval(item)['expected']))

with open('test_report.html','wb+') as file:

    runner = HTMLTestRunner.HTMLTestRunner(file,title='Python9期')
    runner.run(suite)