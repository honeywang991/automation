import unittest
from work2.common.http_request import HttpRequest
class RequestMethod(unittest.TestCase):
    def __init__(self,methodName,url,request_data,method,expected):
        super(RequestMethod,self).__init__(methodName)
        self.url = url
        self.request_data = request_data
        self.method = method
        self.expected = expected
    def test_login(self):
        res=HttpRequest().http_request(self.url,self.request_data,self.method,self.expected)
        try:
            self.assertEqual('expected',res['info'])
        except AssertionError as e:
            print("登陆请求出错了：{0}".format(e))
        raise e