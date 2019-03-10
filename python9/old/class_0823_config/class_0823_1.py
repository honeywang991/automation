#配置文件
#引用数据文件 绝对路径
#配置文件一般存放：共用的数据 或者经常变化的数据
# .conf1  .ini  .propeities

import configparser
#配置文件：片段 section 片段名一般都是大写       选项option      值values

class ReadConfig:
    def read_config(self,file_name,section,option):
        # 打开配置文件
        cf = configparser.ConfigParser()#实例
        cf.read(file_name,encoding='utf-8')#如果有中午用utf-
        value = cf.get(section,option)
        return value

        #获取值：首先找到section  然后找到option
        # name_1=cf.get('NAME','s_1')
        # print(name_1)
        #
        # mode = cf.get('MODE','mode')
        # print(type(mode)) #str
        #
        # list = cf.get('MODE','list')
        # print(type(eval(list)))

#所有的数据从配置文件里面读取出来  都是str类型
#如果 要转换原本格式  请记得用eval()

if __name__ == '__main__':
    value=ReadConfig().read_config('lemon.conf1','NAME','s_3')
    print(value)