import json



class ReadData:
    def read_data(self):
        # file=open(r'C:\Users\Administrator\Desktop\gitwork\python9\class_0816\class_0811_work\test_data_1','r+')#read write append
        file=open(r'C:\Users\Administrator\Desktop\gitwork\python9\class_0811_homework\test_data_1','r+')#read write append

        # C:\Users\Administrator\Desktop\gitwork\python9\class_0811_homework\test_data_1
# file.read()
# file.readline()
# print(file.readlines())
        test_data=file.readlines()
        return test_data

#r r+
# w w+
#a a+ 追加
        # for item in test_data_1:
        #     print(item)
#
# def read_data():
#     file = open('test_data_1.txt','r+')
#     file_line = file.readlines()#按行读取数据
#     list_test_data = []  # 空列表
#     for line in file_line:
#         dict_data = line.replace("\'","\"")
#         dict_data = dict_data.strip("\n")
#         dict_datas = json.loads(dict_data)
#         list_test_data.append(dict_datas)
#     return list_test_data#返回数据  做单元测试
#
