# -*- coding: utf-8 -*-

import os,sys

def cdWalker(path,filename):
    export = []
    for root,dirs,files in os.walk(path):
        export.append("%s;%s;%s"%(root,dirs,files))
    open(filename,"w").write(''.join(export))

filepath = r"E:\python_project\trunk\lovely python"
cdWalker(filepath,"cdays_3_1.txt")

    
