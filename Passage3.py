# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 10:37:37 2019

@author: Maxim
"""
students = ['小明', '小丽', '小熊','小王','小李']

maths_scores = [85, 90, 72,60,73]

dictionary = dict(zip(students, maths_scores))


get_value = input('请输入要查询数学成绩的学生姓名：')
if get_value in dictionary.keys():
    print(get_value+'的数学成绩是：'+str(dictionary[get_value]))
else:
    print('你要查询的'+get_value+'的数学成绩不存在')
    
"""
#查询个人的分数
dictionary['小熊']
#添加个人分数
dictionary['小溪']=100
#修改个人分数
dictionary['小溪']=35
#删除个人分数
del dictionary['小明']
"""