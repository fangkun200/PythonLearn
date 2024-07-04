#!/usr/bin/python3

counter = 100          # 整型变量
miles   = 1000.0       # 浮点型变量
name    = "runoob"     # 字符串

print (counter)
print (miles)
print (name)

# 标准数据类型 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）

# Number（数字） Python3 支持 int、float、bool、complex（复数）。
# 判断类型
a = 111
print(isinstance(a, int))
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
# 内置的 type() 函数可以用来查询变量所指的对象类型
# type()不会认为子类是一种父类类型 isinstance()会认为子类是一种父类类型
# 注意：Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，但可以通过 is 来判断类型。

print(5+4)

5 + 4  # 加法
4.3 - 2 # 减法
3 * 7  # 乘法
2 / 4  # 除法，得到一个浮点数
2 // 4 # 除法，得到一个整数
17 % 3 # 取余
2 ** 5 # 乘方








