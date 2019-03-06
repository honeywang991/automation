import requests
#封装好类 第一步  ； 第二步 做单元测试
#如果要完成不同接口的请求，为了最高的复用性
#我们可以封装成函数
#升级为类

#写这个类的目的： 完成接口测试
class HttpRequest:


    #1
    def http_request(self,url,request_data,method):
        #请求地址
        # url = 'https://www.ketangpai.com/UserApi/login'
        # request_data = {"email":"17718567797","password":"123456","remember":"0"}
        #发起请求POST
        if method.lower()=='get':
            try:
                response=requests.get(url,request_data)
            except Exception as e:
                print("get报错了:{0}".format(e))
                raise e
        elif method.lower()=='post':
            try:
                response=requests.post(url,request_data)
            except Exception as e:
                print("post报错了： {0}".format(e))
                raise e
        else:
            print("请求方式错误")
        return response.json()#只返回结果，后面可能会改
        # #响应头 字典
        # print(response.headers)
        # #状态码
        # print(response.status_code)
        # #响应数据
        # print(response.json()) #只有当你返回的数据格式 是json 采用json去解析
        # print(response.text)  # html xml json 格式都可以解析
        #有时间就可以去了解下装饰器

if __name__ == '__main__':
    run = HttpRequest()
    url = 'https://www.ketangpai.com/UserApi/login'
    request_data = {"email":"17718567797","password":"123456","remember":"0"}
    # method = 'post'
    run.http_request(url,request_data,'Post')



