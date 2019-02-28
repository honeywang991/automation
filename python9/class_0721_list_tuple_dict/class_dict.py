__author__ = 'zz'
#字典 dict{}
#1: 他的值 也可以是任何数据类型
#2：存储的格式不一样 key-value
#3: 取值 字典无序 字典名[key值]
#4: key值是唯一的  如果不唯一 前面的值会被覆盖掉
#key尽量做到见名知意
# dict_1={'s_1':'sunny','s_2':'sun','s_3':'sun1','s_1':'sun2'}
# dict_2={1:3}
# print(dict_1['s_1'])#同名的可被替换

dict_2={'name':'lili','age':18,'height':1.75}
#字典 可以增删改吗？
#增加 字典名[key] key不存在  如果存在的话 value就会被替换
# dict_2['sex']='girl'

#修改  字典名[key]=new_value key必须是存在的 进行替换
# dict_2['sex']='boy'

#删除 字典名.pop(key)
# dict_2.pop('age')
print(dict_2)