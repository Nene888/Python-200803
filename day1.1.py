# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:04:24 2020

@author: USER
"""

w=input("請輸入體重(公斤):\n")
h=input("請輸入身高(公分):\n")
w = float(w)
h = float(h)/100
BMI= w//h**2

if BMI <18.5:
    print("體重不足")
elif BMI <24:
    print("體重正常")
elif BMI <27:
    print("體重過重")    
elif BMI <30:
    print("輕度肥胖")
elif BMI <38:
    print("中度肥胖")
else:
    print("重度肥胖")