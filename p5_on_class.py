#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 13:37:08 2019

@author: stanford
"""

class celebrity:
    """A class for celebrity"""
    #属于类的属性
    instanCount = 0;
    
    def __init__(self, name, age, gender, occupation, no_of_followers):
        #初始化对象的属性
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.no_of_followers = no_of_followers
        celebrity.instanCount += 1
    def speak(self, words):
        print(self.name + " speaks:" + words)
    def showSelf(self):
        print("I am {}. I am {} years old and my occupation includes {}".format(self.name, self.age, self.occupation))
    def __str__(self):
        return "a celebrity called {}".format(self.name)
        
if __name__ == "__main__":
    Jay_Chou = celebrity("Jay Chou", 40, "male", ["singer", "song writer"], 400)
    Zhou_Xun = celebrity("Zhou Xun", 45, "female", "actor", 300)    
    Cai_Xukun = celebrity("Cai Xukun", 21, "male", ["idol", "singer"], 200) 
    Jay_Chou.speak("I love you.")  
    Zhou_Xun.speak("I am a professional actor.")
    Cai_Xukun.speak("I can play basketball.")
    Jay_Chou.showSelf()
    Zhou_Xun.showSelf()
    Cai_Xukun.showSelf()
    print(Cai_Xukun)
    print(celebrity.instanCount) 
    print(celebrity.__doc__)
    print(celebrity.__name__)
    print(celebrity.__module__)
    print(celebrity.__bases__)    
    print(celebrity.__dict__) 
    
    hasattr(Jay_Chou, 'age')    # 如果存在 'age' 属性返回 True。
    getattr(Jay_Chou, 'age')    # 返回 'age' 属性的值
    setattr(Jay_Chou, 'age', 8) # 添加属性 'age' 值为 8
    delattr(Jay_Chou, 'age')    # 删除属性 'age'