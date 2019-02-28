__author__ = 'zz'
#列表 list 标识符[]
#特性： 1：他可以包含任何类型的数据,数据之间用逗号隔开
#2：元组取值的方式： 列表名[索引的值]
#3: 他的索引是从0开始的
#4：列表可以进行增删改
list_1 = [1,'hello',8.6,(1,2,3,4),[5,6,9,10]]

#出一个小题目：把(1,2,3,4)里面的3 替换成‘Python9’
# list_1[3][2]='python9' #不能改
# print(list_1)

# print(list_1[3][2])
list_1[3]='python9'
print(list_1)

#取[5,6,9,10]中的5
# print(list_1[4][0])

#函数 列表的函数
#新增一个值 列表名.append() 在最后名加一个元素
# list_1.append('野人')
# print(list_1)

#新增一个值 列表名.insert(i,value) 在指定位置加一个元素
# list_1.insert(0,'大人')

#删除一个元素  列表名.pop() 删除最后面一个元素
#删除指定位置的元素 列表名.pop(index)
# list_1.pop()
# list_1.pop(0)
# print(list_1)
# print(list_1.pop(0))