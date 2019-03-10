#coding=utf-8
import unittest
from ddt import ddt,data,unpack
from common.do_excel1 import DoExcel
from conf1 import read_path1
from common.http_request1 import HttpRequest
from common.read_config1 import ReadConfig

#读取配置文件mode
mode=ReadConfig().read_config1(read_path1.conf_path,'MODE','mode')
# print(mode)
#读取配置文件case_jid_list
case_id_list=ReadConfig().read_config1(read_path1.conf_path,'MODE','case_id_list')
# print(case_id_list)
test_data=DoExcel(read_path1.test_data_path,'d1').do_excel(mode,case_id_list)
# for i in  test_data:
#     print(i)



@ddt
class TestRequestMethod1(unittest.TestCase):

    @data(*test_data)
    def test_http_requests(self,item):
        #如果传列表 就根据索引取值
        #如果传进的是字典  经过data拆分  就通过key取值
        result=HttpRequest().http_request(item['method'],item['url'],eval(item['param']))
        # print(result)
        result=result['message']
        # print(result)
        # print(eval(item['expected'])['message'])

        try:
            self.assertEqual(eval(item['expected'])['message'],result)
        except AssertionError as e:
            print("执行测试用例出错啦！结果是{0}".format(e))
            raise e
        else:
            print("测试执行成功啦！结果是{0}".format(result))

        # try:
        #     self.assertEqual(eval(item['expected'])['message'],result)
        # except AssertionError as e:
        #     print("执行测试用例出错啦！结果是{0}".format(e))
        #     raise e
        # else:
        #     print("测试执行成功啦！结果是{0}".format(result))



#光标放在这里 点击运行























# @ddt#装饰测试类
# class RequestMethod(unittest.TestCase):
#     @data(*test_data)#装饰方法  传测试数据，测试数据从哪里获取，写在from下面
#     def test_login(self,item):
#         res=HttpRequest().http_request(item['method'],item['url'],eval(item['param']))
#         try:
#             self.assertEqual(item['expected'],res['info'])
#         except AssertionError as e:
#             print("登陆请求出错了：{0}".format(e))
#             raise e
#         else:
#             print("测试通过了{0}".format(res))



