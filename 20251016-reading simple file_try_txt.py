# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 15:43:13 2025

@author: joeyj
"""

#I am opening the try file and running each line in the files into loops:
trying=open('try.txt')
count=0


for yy in trying:
    count=count+1
    print(count,':',yy)
    
#once an operation is done, I need to reopen the file to execute a second function
    
trying=open('try.txt')
    
tp=trying.read()
print(tp)

#check again if I never open the file
for ta in trying:
    print('?', ta)
#see this line never get printed out
    
#now I reopen the files and operate the read line by line again:
trying=open('try.txt')
for zz in trying:
    print('ok',':',zz)
    
