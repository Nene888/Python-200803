# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 16:13:42 2020

@author: USER
"""

m=int(input("請輸入數學分數:\n"))
e=int(input("請輸入英文分數:\n"))

if m >=90 and e >=90:
    print("gift")
elif m<60 and e<60:
    print("處罰")
elif m<60 or e<60 :
    print("再加油")
