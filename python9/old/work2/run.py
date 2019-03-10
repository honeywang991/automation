from common.test_http_request import RequestMethod
import unittest
import HTMLTestRunner
from common.do_excel import DoExcel
from conf6 import read_path6
from common.read_config6 import ReadConfig6

if __name__ == '__main__':

    mode=ReadConfig6().read_config(read_path6.conf_path, 'MODE', 'mode')
    case_id_list=ReadConfig6().read_config(read_path6.conf_path, 'MODE', 'case_id_list')
    print(read_path6.test_data_path)
    test_data=DoExcel(read_path6.test_data_path, 'test_data_1').do_excel(mode, case_id_list)
    # print(test_data)
    suite = unittest.TestSuite()
    for item in test_data:
        suite.addTest(
            RequestMethod("test_login", item['url'], eval(item['param']), eval(item['expected']), item['method']))

    with open(read_path6.report_path, "wb+") as file:
        runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='自动化测试报告', description='11详细测试用例结果',
                                               tester="HoneyWang")
        runner.run(suite)


#C:\Users\Administrator\Desktop\automation\python9\auto_api\conf1\pro.conf1
#如果conf中的mode 是1   则执行所有用例   ；  是0则执行case_id_list=[1，3]