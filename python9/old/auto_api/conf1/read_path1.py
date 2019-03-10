import os

pro_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# print(pro_path)

test_data_path=os.path.join(pro_path,'test_data','t1.xlsx')
# print(test_data_path)
#测试数据的路径

report_path1=os.path.join(pro_path,'test_result','test_report1.html')
#测试报告的路径
# print(report_path)

conf_path = pro_path + '\conf1\pro.conf'
#配置文件的路径

# print(conf_path)