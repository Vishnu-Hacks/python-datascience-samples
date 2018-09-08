# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 12:15:41 2018

@author: vishn
"""

from  matplotlib import pyplot

movies=["Avatar","Avengers","Deamons & Angels","Gandhi","West Side Story"]
num_oscars=[5,11,3,8,10]


plt1 = pyplot
plt1.title("Oscars award for movies")
plt1.ylabel("Num of Oscars")
plt1.xlabel("Movie")
plt1.bar(movies,num_oscars)
plt1.show() 

""" There are different ways to align and beautify the graphs """