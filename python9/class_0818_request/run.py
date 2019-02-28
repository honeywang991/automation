import unittest
import HTMLTestRunner
from class_0818_request.read_data import ReadData
from class_0818_request.test_http_request import TestHttpRequest
# C:\Users\Administrator\Desktop\gitwork\python9\class_0818_request\test_http_request.py


suite = unittest.TestSuite()

#参数化在这里完成
test_data = ReadData().read_data()
for item in test_data:
# test_data = [
# {"url":"https://www.baidu.com",
#  "request_data":"{'name':'honey','pw':'123'}",
#  'method':'post'},]
#请求参数
    suite.addTest(TestHttpRequest("test_login",item['url'],eval(item['request_data']),item['method'],item['expected']))
    # suite.addTest(TestMath('test_add', eval(item)['a'], eval(item)['b'], eval(item)['expected']))

with open("test_report.html","wb+") as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,title='自动化测试报告',description='11详细测试用例结果',tester="HoneyWang")
    runner.run(suite)