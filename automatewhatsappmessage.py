# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 11:59:55 2021

@author: Sagar Goel
"""
import pywhatkit
import pyautogui
import time
print("Mobile Number of the person with country code:")
Q=input()
print("Please enter the message:")
P=input()
print('Number of times you want to share message:')
N=int(input())
N=N-1
print('There are two types of functions:')
print('1: After how many minutes you wanna share')
print('2: At which time you wanna share')
print('enter 1 or 2:')
k=int(input())
if(k==1):
    M=int(input())
    minutes=time.localtime().tm_min
    minutes=minutes+M
    hours=time.localtime().tm_hour
    hours=hours+int(minutes/60)
    minutes=minutes%60
else:
    print('enter time in hhmm format')
    M=int(input())
    hours=int(M/100)
    minutes=M%100
    print("Message will be sent at ",hours,":",minutes)
pywhatkit.sendwhatmsg(Q,P, hours, minutes)
#pywhatkit.sendwhatmsg('+919997955711', 'Hello', 14, 9)
for i in range(N):
    time.sleep(1)
    pyautogui.typewrite(P)
    pyautogui.press('enter')
    
        