from old.work import RequestMethod
import unittest
import HTMLTestRunner
from old.work import DoExcel


if __name__ == '__main__':
    # file_name = r'C:\Users\Administrator\Desktop\automation\python9\work\my_test_data\t1.xlsx'
    test_data=DoExcel('t1.xlsx','test_data_1').do_excel()
    suite = unittest.TestSuite()
    for item in test_data:
        suite.addTest(
            RequestMethod("test_login", item['url'], eval(item['param']), eval(item['expected']), item['method']))

    with open(r"test_result\test_report111.html", "wb+") as file:
        runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='自动化测试报告', description='11详细测试用例结果',
                                               tester="HoneyWang")
        runner.run(suite)