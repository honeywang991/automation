import os

pro_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
print(pro_path)
test_data_path=os.path.join(pro_path,'test_data','testdata.xlsx')
report_path=os.path.join(pro_path,'test_result','test_report111.html')
