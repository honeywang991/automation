from common.test_http_request import RequestMethod
import unittest
import HTMLTestRunner
from common.do_excel import DoExcel
from conf import read_path
from common.read_config import ReadConfig

if __name__ == '__main__':
    # excle_path = read_path.pro_path + r'\test_num_data\testdata.xlsx'
    # file_name = r'C:\Users\Administrator\Desktop\automation\python9\auto_api\test_num_data\testdata.xlsx'
    mode=ReadConfig().read_config(read_path.conf_path,'MODE','mode')
    case_id_list=ReadConfig().read_config(read_path.conf_path,'MODE','case_id_list')
    test_data=DoExcel(read_path.test_data_path,'test_data_1').do_excel(mode,case_id_list)
    # print(test_data)
    suite = unittest.TestSuite()
    for item in test_data:
        suite.addTest(
            RequestMethod("test_login", item['url'], eval(item['param']), eval(item['expected']), item['method']))

    with open(read_path.report_path, "wb+") as file:
        runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='自动化测试报告', description='11详细测试用例结果',
                                               tester="HoneyWang")
        runner.run(suite)


#C:\Users\Administrator\Desktop\automation\python9\auto_api\conf\pro.conf
#如果conf中的mode 是1   则执行所有用例   ；  是0则执行case_id_list=[1，3]