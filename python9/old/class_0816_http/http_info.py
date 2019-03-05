#常见的http请求  get post---必须掌握的
#get post 有什么区别吗？ 关注公众号
#put dead delete option


#浏览器--browser firefox
#User-Agent:Mozilla/5.0 记录那个地方发过来的
#伪装成浏览器去发送请求？
#请求头： Mozilla/5.0 (Windows NT 6.1; rv:64.0) Gecko/20100101 Firefox/64.0
#请求头 响应头 响应报文
#请求参数 用户名 密码
#<name>'小幸福'</name> ---> xml格式
#{"name":"小幸福"} ---> json格式
#响应头 响应头字段
#响应报文  ---> 相应数据 xml json html
#<name>'小幸福'</name> ---> xml格式
#{"name":"小幸福"} ---> json格式
#<html></html> ----> html格式

#请求 是xml jsom格式 传递数据常用json
#返回 是xml json html格式
#格式和数据类型是两码事

import requests
#get post

# url='https://www.baidu.com/'#http 你访问的协议 https
# #get请求
# #def get(url位置参数, params=None默认参数, **kwargs关键字参数):
# res=requests.get(url) #发起一个http请求
# print(type(res))
# response = res.text# html xml json 用text去解析
# # response_2 = res.json() #只有当你返回的数据格式是json的，才可以用json去解析、
# print(response)
# print("状态吗",res.status_code)
# #状态码：至少要知道10个
# #200请求成功
# #401没有授权
# #404页面不见了
# #502网关错误
# #403 未更新
# #500
# #503
# #400开头 一般是请求的问题
# #500开头 一般是服务端的问题
# #200 表示我的请求成功了吗？
# #200表示你的请求被服务器接受了，并且服务器返回了结果
#


# #post请求
# #def post(url, data=None, json=None, **kwargs): 4个参数
# res=requests.post(url)
# response=res.text
# # print(response)
# print("状态码",res.status_code)


#发起一个有参数的http请求
#登录的请求地址
url = "http://119.23.241.154:8080/futureloan/mvc/api/member/login"
request_data={"mobilephone":"18688773467","pwd":"123456"}

# login_res=requests.get(url,request_data)
# print(login_res.text)#json
# print(login_res.json())
# print(type(login_res.text)) #<class'str'> 字符串
# print(type(login_res.json()))#<class'dict'> 字典 #如果返回的是json格式的数据，要用json解析，返回字典类型的数据
# print(login_res.json()['msg'])#查看msg #登录成功
# print(login_res.json()['code'])#查看code

login_res=requests.post(url,request_data)
print(login_res.text)
print(login_res.json())


#work 8-16号作业 编写HTTP单元测试作业
#编写HTTP请求类
#1.根据老师上课讲解的requests完成的get请求
#和post请求，编写一个http请求类，
#里面有一个函数：http_request()
#可以根据你们指定的方法，完成get请求
#或者是post请求

#2.请根据你们自己写的http请求类，编写一个测试类

#3.请根据你们写的测试类，完成单元测试，生成测试报告

#请求地址和请求参数
#url = "http://119.23.241.154:8080/futureloan/mvc/api/member/login"
#request_data={"mobilephone":"18688773467","pwd":"123456"}

#请利用8-2号的作业，完成参数化



