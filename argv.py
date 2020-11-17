# -*- coding: utf-8 -*-
# @Time : 2020/11/17 10:39
# @Author : wianwu
# @Software: PyCharm 

import sys
import argparse

def sys_argv():
    '''
    使用sys包的argv接收参数
    使用：pytong argv1 argv2 ....
    sys.argv[0] 为文件命， 从1开始是参数
    :return:
    '''
    argvlist = sys.argv  # Xianwu:接收参数
    print(argvlist)  # 展示'''put put ['argv.py', 'hello', '!', 'i', 'am', 'a', 'boy']'''

    for i in range(len(argvlist)):
        print("argv", i,':', argvlist[i])

    pass  # 主程序：


def argparse_argv():
    '''
    通过argparse包接受参数
    基本用法:
    创建解析器ArgumentParser
    向解析器添加参数格式 ： 参数前缀，参数， 参数类型，帮助信息，默认等等
    解析器解析参数 然会一个参数： args = parser.parse_args()
    使用参数： args.arg_name

    :return:
    '''
    # coding=utf-8
    import argparse

    # 创建 ArgumentParser() 对象
    parser = argparse.ArgumentParser(description="your script description")  # description参数可以用于插入描述脚本用途的信息，可以为空
    print(parser)
    # 调用 add_argument() 方法添加参数
    parser.add_argument('-a', '--arga_name', type=int, help='input aint num', default = 80)
    parser.add_argument('-b', '--argb_name', type=int, help='input aint num', default = 80)

    # 使用 parse_args() 解析添加的参数
    args = parser.parse_args()  # 将变量以标签-值的字典形式存入args字典

    print(args)
    print(args.arga_name) #使用参数
    print(args.argb_name)
if __name__ == "__main__":
    # sys_argv()
    argparse_argv()