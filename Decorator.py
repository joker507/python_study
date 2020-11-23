# -*- coding: utf-8 -*-
# @Time : 2020/11/21 0:52
# @Author : wianwu
# @Software: PyCharm 
'''
@Information: 装饰器
定义：在已有函数中增加额外功能的函数
本质：使用闭包在inner()内部函数给原函数增加新功能
作用：添加函数功能，并且没有修改源代码
特点：1.不能修改已有函数源代码。
     2. 不能修改已有函数的调用方式
     3. 给已有函数添加功能

'''

# 装饰器示例：发表评论前需要登录
#==================================================================
# 1
print("一：第一中写法（一般不用")
def comment():
    print("发表评")

#没有装饰器
print("没有装饰器：")
comment()

#2 写装饰器
def check(f):

    def inner():  # 在这里增加f函数外的新功能
        print("请登录..") #增加功能
        f()       #是一个闭包 因为使用了外部函数的变量 ：

    return inner

#3 使用装饰器来装饰他
print("有装饰器：")
comment = check(comment) #进行装饰comment()函数
comment()  # == inner()

#==================================================================

#更简便的方法：直接在被装饰函数的头部def func()加上@check #装饰器名称

print("二： 第二种写法@")

# 写装饰器
def check2(f):

    def inner2():  # 在这里增加f函数外的新功能
        print("请登录..") #增加功能
        f()       #是一个闭包 因为使用了外部函数的变量 ：

    return inner2

@check2   # == comment2 = check2(comment2)
def comment2(): #这里的comment 已经被check2修饰成 inner2函数的功能，但是调用的时候还hi用comment2()
    print("发表评")


print("使用了@装饰器：")
comment()  #已经用了@check2进行进行了装饰


