# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:29:15 2020

@author: USER
"""

r=input("請輸入分數:\n")
r = int(r)
if r >=0 and r<=100:
    if r >=90:
        print("分數:A ")
    elif r >=80:
        print("分數:B ")
    elif r >=70:
        print("分數:C ")    
    elif r >=60:
        print("分數:D ")
    else:
        print("分數:E ")            
elif r >100:
    print("您輸入過多")
elif r <0:
    print("您輸入過少")            