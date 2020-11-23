# -*- coding: utf-8 -*-
# @Time : 2020/11/21 0:14
# @Author : wianwu
# @Software: PyCharm
'''
闭包 ：调用函数返回一个函数
作用：保存外部函数的变量
'''

#定义外部函数
def func_out(p1):
    print("func_out:")

    #定义内部函数：第一次执行func_out的时候不执行func_inner
    def func_inner(p2):
        result = p1 + p2
        print("保存外部函数变量：",p1)
        print("result:",result)
        return result

    return func_inner #返回闭包函数

isFunction = func_out(55) #func_inner(p2)

print("return func_out:",isFunction)

result = isFunction(77)

print("return func_inner result:",result)




