import configparser
class ReadConfig:
    def read_config1(self,file_name,section,option):
        # 打开配置文件
        cf = configparser.ConfigParser()#实例
        cf.read(file_name,encoding='utf-8')#如果有中午用utf-
        value = cf.get(section,option)
        return value


if __name__ == '__main__':
    from conf1 import read_path1
    path = read_path1.pro_path + '\conf1\pro.conf'
    print(path)
    value=ReadConfig().read_config1(path,'MODE','mode')
    print(value)