import unittest
import HTMLTestRunner
from conf1 import read_path1
from common.test_http_request1 import TestRequestMethod1

suite = unittest.TestSuite()#创建的测试套件
loader =unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestRequestMethod1))

with open(read_path1.report_path1, "wb+") as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='dog', description='ddt装饰测试用例',tester="HoneyWang")
    runner.run(suite)
        

#C:\Users\Administrator\Desktop\automation\python9\auto_api\conf1\pro.conf1
#如果conf中的mode 是1   则执行所有用例   ；  是0则执行case_id_list=[1，3]