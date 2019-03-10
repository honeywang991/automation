
import configparser
class ReadConfig6:
    def read_config(self,file_name,section,option):
        # print(file_name)
        # 打开配置文件
        cf = configparser.ConfigParser()#实例
        cf.read(file_name,encoding='utf-8')#如果有中午用utf-
        value = cf.get(section,option)
        return value


if __name__ == '__main__':
    path6=r'C:\Users\Administrator\Desktop\automation\python9\old\work2\conf6\pro6.conf'
    vae=ReadConfig6().read_config(path6,'PRO_PATH','pro_path')
    print(vae)


#
# import configparser
#
#
# # print(file_name)
# # 打开配置文件
# cf = configparser.ConfigParser()#实例
# file_name = r'C:\Users\Administrator\Desktop\automation\python9\old\work2\conf6\pro6.conf'
# a=cf.read(file_name,encoding='utf-8')#如果有中午用utf-
# # value = cf.get(section,option)
# print(a)
# b = cf.get('MODE','mode')
# print(b)
# c = cf.get('PRO_PATH','pro_path')
# print(c)

