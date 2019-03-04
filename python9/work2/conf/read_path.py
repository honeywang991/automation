import os
from work2.common.read_config import ReadConfig


conf_path = os.path.join(os.path.split(os.path.realpath(__file__))[0],'pro.conf')

pro_path=ReadConfig().read_config(conf_path,'PRO_PATH','pro_path')


test_data_path=os.path.join(pro_path,'test_num_data','testdata.xlsx')
print(test_data_path)

report_path=os.path.join(pro_path,'test_result','test_report111.html')


#作业题
#路径中怎么实现自动修改配置文件里面的项目路径，
#不用每次去手动变更
