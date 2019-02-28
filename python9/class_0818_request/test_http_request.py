#第二步 做单元测试
#第34节 python配置文件的使用与设计  26：10

#单元测试  写测试用例 对不同的接口写测试用例？

import unittest
# C:\Users\Administrator\Desktop\gitwork\python9\class_0818_request\http_request.py
from class_0818_request.http_request import HttpRequest
class TestHttpRequest(unittest.TestCase):
    def __init__(self,methodName,url,request_data,method,expected):
        super(TestHttpRequest,self).__init__(methodName)
        self.url = url
        self.request_data = request_data
        self.method = method
        self.expected = expected


    # def test_right_login(self,url,request_data,method):#正常登陆
    def test_login(self):
        # url='https://www.baidu.com'
        # request_data={"name":"honey","pw":"123"}
        # method='post'
        res=HttpRequest().http_request(self.url,self.request_data,self.method,self.expected)
        try:
            self.assertEqual('expected',res['info'])
        except AssertionError as e:
            print("登陆请求出错了：{0}".format(e))
            raise e

    # def test_wrong_pwd_login(self):
    #     url='https://www.baidu.com'
    #     request_data={"name":"honey","pw":"1123"}
    #     method='post'
    #     res=HttpRequest().http_request(self.url,self.request_data,self.method)
    #     try:
    #         self.assertEqual('密码错误',res['info'])
    #     except AssertionError as e:
    #         print("登陆请求出错了：{0}".format(e))
    #         raise e

