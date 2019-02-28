#if 条件语句 80%
#if else 判断你语句的走向 控制流
#1：最简单的if判断语句：if
#2: 符合语句： if...else...
#3: 复杂一点点 if..elif..else
#用缩进来控制 级别
# age=18
# if age>18:
#     print("你未年了")
# else:
#     print("你成年了")

# color='red'
# if color=='red':
#     print('stop')
# elif color=='yellow':
#     print("wait")
# elif color=='green':
#     print('go')
# else:
#     print('color is wrong')


#if语句： if 后面跟的是 比较表达式  比较运算 条件
#if 后面的条件语句  运算结果是 布尔值 True 或者false
#1: if后面的条件为True 那么就执行if下面的代码块 否则不执行if下面的代码块
#2: if...else  else后面不能加任何条件 ，而且整个if语句只能有一个else结尾
#3: if elif else 其中elif可以有多个 elif后面必须加条件

# score=60
# if score>=60:
#     print("及格")
# else:
#     print("不及格")

age=18
sex='girl'
if age>=18:
    if sex=='girl':
        print("是个成年的女孩")
    elif sex=='boy':
        print("是个成年的男孩")
elif age<18:
    if sex=='girl':
        print("是个成年的女孩")
    elif sex=='boy':
        print("是个成年的男孩")