import unittest
from class_0811_homework import math
# D:\wf\python9\class_0816\class_0811_work

class TestMath(unittest.TestCase):
    #类名 首字母大写 驼峰命名 见名知意 不能数字开头
    #函数名 变量名： 模块名 都是小写 字母字母之间用下划线隔开
    def __init__(self,methodName,a,b,expected):
        super(TestMath,self).__init__(methodName) #超继承
        self.a = a
        self.b = b
        self.expected = expected

    #测试用例
    def test_add(self):
        result = math().add(self.a,self.b)
        try:
            self.assertEqual(self.expected,result)
        except Exception as e:
            print("执行用例出错了，报的错是：{0}".format(e))
        else:
            print("测试执行结果是：{0}".format(result))