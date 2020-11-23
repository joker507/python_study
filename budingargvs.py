'''
python不定参数的使用
在函数传参数的时候，有时我们不知道要传多少个
这时候在定义的时候就可以用不定参数
格式：def function(*argv,**kwargv):

*表示传入一个元组
**表示传入键值也就是字典

使用 function(1,2,3,4,name='xiaoming',age=16)
此时参数 argv = (1,2,3,4)
        kwargv = {'name':'xiaoming','age':16}

注意传参的时候： key值（key = )没有''他不是一个字符窜

'''

#示例
#统计学生的得分情况以及基本信息
def count_core(*core,**info):
    #打印成绩
    print('core:',core)
    print('info:',info)

    for i in range(len(core)):
        print("第{}科成绩为{}".format(i,core[i]))

    # itemss = info.items()
    # print('info.items:',itemss)
    #字典(不属于迭代器)的迭代需要转换成一个迭代器:dict.items()
    for key,word in info.items():
        print('学生的{}是{}'.format(key,word)) 

#实例化
count_core(89,79,93,95,69, name = 'xiaoming', 专业='物联666', 老师 ='显武')

