import requests

class HttpRequest:
    def http_request(self,method,url,param):
        if method=='get':
            try:
                response=requests.get(url,param)
            except Exception as e:
                print("get报错了:{0}".format(e))
                raise e
        elif method=='post':
            try:
                response=requests.post(url,param)
            except Exception as e:
                print("post报错了： {0}".format(e))
                raise e
        else:
            print("请求方式错误")
        return response.json()#只返回结果，后面可能会改


if __name__ == '__main__':
    run = HttpRequest()
    #url = 'https://www.ketangpai.com/UserApi/login'
    url='https://passport.csdn.net/v1/register/pc/login/doLogin'
    # request_data = {"email":"17718567797","password":"123456","remember":"0"}
    # method = 'post'
    param ='{"Content-Type":"application/json","loginType":"1","pwdOrVerifyCode":"wangfang123","userIdentification":"17718567797","fkid":"WC39ZUyXRgdFhTf0hDIo3V6/yTKO8NOPq8vd7qogwNE9fGkdpuw5CSLC5kZgQxTET799bWOUpq4fNJqrlLMEXPg4g1qUN5iIwH2DWLjo7hT11/wVTJYCra0zA0CtbXuWTErzxpd9YAAcgJlcF7M15V1f14annaclKPAg2vqULfkcWb38ZIHBX2KBAN/TVWjHUi+tj1o4Ia9YG7wWr0zokq37ryRiki2vYK9/WsyV7FZn0O5OLQgkZngpBjWyIEb3hUXSi7AOqpnbPzkIT4yg2ruRinzXzxrxK1487577677129","uaToken":"115#17sZ1C1O1TNSDEQCG5E71CsoElRdxJZI134kOsvirftbq42fYR2WTaxuPBsEsJf1DfOloaUzrB4d2Ypfu5qQAS45HMWOykNQi/JJeJUWA5ccawpfyr+dAzhPehT8y+qQiwJJhZ78AzVcag2fy+lE9NAPejTzuHNdqQy+PUUzdkN0uLpbuX1dfSfz2t/zykZdgQWWhEz4OkNcZL9A5O11TIfyeK1Gt6NQiQXRUkzbvBNDaGwfurrQ9IfPeKT4kkNQi/JJhUU4BHNcaTBXGsbGmGhtbmPO6HhLVfGddlDBwN7lTh5ItFeC+Mfr/ocLu91uPoutmxkgW3qafOkxmEHLnCLewraYRFmiS1EV/j5KkhXjbBDNMcFMNQUjR8Wh2caBnMzgMWAyStd9cB3cRh+RKUQei5E2Qt6wTfGSfZ8b69u0UaFqHNW/upDiuQalFEu8SBUY+aHFomEG7+QyshybM94Bo9kvgH26wRGPGW+rs6OHjWIOXGgxUEC6t8TOyKhV/0V2RMB43TviFT3VmD3xAbesYS4UkwoqF+uXWy9tStBagZBaqKrkq4xUjlYCQBP24jM7wPWQSrI9uVzdcF4y0JngP08MkWu27s21CprTFDUG9y7EurY8QrCw32Q0p8Pk5ZC/VZO29mX/TVFd/6suHMHo5SuuYtUWzb5AdWNWXimDFyyB3KDASND4j1Zq1crVsJMKmrP6g/3FUv/jC957vUSFJKk3cbyPJYnD15DJHICIeluwdPHMut7el7SDhwt4yfFSd20UFHeeV3G6HOSoeGMCQnZ6s++I2n03wx1u3G3JqnStyD6sMbohNqBOcGYdZjvUBu64UDtJnt3irICsACf+BiCJk5yj9EgB5TNnD8dtDP6QZ13IQHb4ImscLujzKYN7Lu8jvhqXA7AcvV+urDp9P2M0w9EAMojwEqXpOYZgNEOFEfkEcqj9PE2iA9EdHGwgMUvULRFimn9xJ7P1VCUaWOqDm2sOQTfTH+PjgkWy+Ypq15CwpZJkYE4VsWq8Hm5xnXpvyDSN3eIXDUfkHjv1mtQ7QC4io7rnZUOri2+Z3bNFD/SgZYdUxlEPexa4smti7cqLYRQLyhVg","webUmidToken":"TEE47092FDF85908C442C9F4C8D964EC7AEDC90DF4CC6D732FE5115B209","wyToken":"9ca17ae2e6ffcda170e2e6eeadcb4b9396a7b6f752e9a88bb2c85a839e9fabf27dab92afb0d54b9887009bcb2af0feaec3b92af4ada9d3ec5da3b09c8aee4a929b8eb7d14b8bb0a5d3d06fa39e8eb1cb6882e8ee9e"}'
    print(type(param))
    res=run.http_request('post',url,param)
    print(res)

    # #响应头 字典
    # print(response.headers)
    # #状态码
    # print(response.status_code)
    # #响应数据
    # print(response.json()) #只有当你返回的数据格式 是json 采用json去解析
    # print(response.text)  # html xml json 格式都可以解析
    # 有时间就可以去了解下装饰器












# import requests
# #封装好类 第一步  ； 第二步 做单元测试
# #如果要完成不同接口的请求，为了最高的复用性
# #我们可以封装成函数
# #升级为类
#
# #写这个类的目的： 完成接口测试
# class HttpRequest:
#     def http_request(self,method,url,request_data):
#         if method.lower()=='get':
#             try:
#                 response=requests.get(url,request_data)
#             except Exception as e:
#                 print("get报错了:{0}".format(e))
#                 raise e
#         elif method.lower()=='post':
#             try:
#                 response=requests.post(url,request_data)
#             except Exception as e:
#                 print("post报错了： {0}".format(e))
#                 raise e
#         else:
#             print("请求方式错误")
#         return response.json()#只返回结果，后面可能会改
#
#
# if __name__ == '__main__':
#     run = HttpRequest()
#     url = 'https://www.ketangpai.com/UserApi/login'
#     request_data = {"email":"17718567797","password":"123456","remember":"0"}
#     # method = 'post'
#     run.http_request(url,request_data,'Post')
#
#     # #响应头 字典
#     # print(response.headers)
#     # #状态码
#     # print(response.status_code)
#     # #响应数据
#     # print(response.json()) #只有当你返回的数据格式 是json 采用json去解析
#     # print(response.text)  # html xml json 格式都可以解析
#     # 有时间就可以去了解下装饰器
#
#
#
