

class ReadData:
    def read_data(self):
        #打开文件
        file = open("test_data.txt","r",encoding='utf-8')
        result = file.readlines() #返回列表形式的数据，每行作为一个元素
        # print(result) #调试，看下打印出来的数据
        # print(result[0]) # 首先处理第一行数据  然后加for循环处理多行数据
        test_data = []

        for data_line in result:

            result_split = result[0].split(';') #返回列表形式的数据
            # print(result_split)
            #要列表变成字典，怎么切 循环切
            sub_dict = {} #空字典 存东西
            for item in  result_split:
                # print(item)
                # print("切割前的数据",item)
                # print("切割后的数据",item.split(':',1))

                sub_dict[item.split(':',1)[0]]=item.split(':',1)[1]

                # sub_split = item.split(':',1)
                # # print(sub_dict)
                # sub_dict[sub_split[0]] = sub_split[1]
                # # print(sub_dict)
            test_data.append(sub_dict)#切割完，处理完的数据，要放到这里面来
        return test_data#返回结果

if __name__ == '__main__':
    test_data = ReadData().read_data()
    print(test_data)
