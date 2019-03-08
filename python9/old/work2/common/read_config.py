
import configparser
class ReadConfig:
    def read_config(self,file_name,section,option):
        # print(file_name)
        # 打开配置文件
        cf = configparser.ConfigParser()#实例
        cf.read(file_name,encoding='utf-8')#如果有中午用utf-
        value = cf.get(section,option)
        return value


if __name__ == '__main__':
    value=ReadConfig().read_config('pro.conf1','PRO_PATH','pro_path')
    print(value)