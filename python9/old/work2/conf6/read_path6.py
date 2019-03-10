import os
from common.read_config6 import ReadConfig6

# path6 = r'C:\Users\Administrator\Desktop\automation\python9\old\work2\conf6\pro6.conf'
# vae = ReadConfig6().read_config(path6, 'PRO_PATH', 'pro_path')
# print(vae)

conf_path = os.path.join(os.path.split(os.path.realpath(__file__))[0],'pro6.conf')
pro_path=ReadConfig6().read_config(conf_path,'PRO_PATH','pro_path')
test_data_path=os.path.join(pro_path,'test_data','testdata.xlsx')
# print(test_data_path)
report_path=os.path.join(pro_path,'test_result','test_report111.html')
# print(conf_path)
# print(pro_path)
# print(test_data_path)

#作业题
#路径中怎么实现自动修改配置文件里面的项目路径，
#不用每次去手动变更
