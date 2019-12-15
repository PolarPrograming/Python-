# -*- coding: utf-8 -*-

import os
import shutil

boys=[]
girls=[]
os.makedirs(r"sorted_files/boys")
os.makedirs(r"sorted_files/girls")
os.makedirs(r"sorted_files/boys/beijing")
os.makedirs(r"sorted_files/boys/shanghai")
os.makedirs(r"sorted_files/boys/guangzhou")
os.makedirs(r"sorted_files/girls/beijing")
os.makedirs(r"sorted_files/girls/shanghai")
os.makedirs(r"sorted_files/girls/guangzhou")

for dirname,folders,filenames in os.walk(r"list/files"):
    for filename in filenames:
        if filename.endswith(".boy"):
            boys.append(os.path.join(dirname,filename))
        if filename.endswith(".girl"):
           girls.append(os.path.join(dirname,filename))
            
for boy in boys:
    if open(boy).read()=="beijing":
        shutil.copy(boy,r"sorted_files/boys/beijing")
    if open(boy).read()=="shanghai":
        shutil.copy(boy,r"sorted_files/boys/shanghai")
    if open(boy).read()=="guangzhou":
        shutil.copy(boy,r"sorted_files/boys/guangzhou")

        
for girl in girls:
    if open(girl).read()=="beijing":
        shutil.copy(girl,r"sorted_files/girls/beijing")
    if open(girl).read()=="shanghai":
        shutil.copy(girl,r"sorted_files/girls/shanghai")
    if open(girl).read()=="guangzhou":
        shutil.copy(girl,r"sorted_files/girls/guangzhou")

            
        
            

         