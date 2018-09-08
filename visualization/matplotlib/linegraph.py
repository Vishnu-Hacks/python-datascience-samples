# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 11:26:21 2018

@author: vishn
"""

from matplotlib import pyplot as plt
import random as rnd


""" The graphs can be visually customized in many ways """
""" The Line graphs are the best choice for visualizing trends """

#simple graph
years=[2000,2002,2004,2006,2007,2009]
gdp=[1.2, 3.4, 2 ,9.2 ,10 ,2.9 ]

plt.plot(years,gdp,color="red",marker="x",linestyle="solid")
plt.title("GDP growth in Years")
plt.ylabel(" in Billion Dollars")
plt.xlabel("year")
plt.show() #displayes the image

""" graph created using random values """
#creating random years
years= rnd.sample([x for x in range(2000,2018) if x%3==0],6)
years.sort()
print years

#creating random gdp rates
gdp=rnd.sample([x for x in range(10,100)],6)
print gdp

plt.plot(years,gdp,"b:.") #"b:." -> blue dots
plt.title("GDP growth in Years")
plt.ylabel(" in Billion Dollars")
plt.xlabel("year")
plt.show() #displayes the image

plt.savefig("/image") #saves the image


""" combining two line or more line graphs """
years1=[2000,2002,2004,2006,2007,2009]
years1.sort()
gdp1=[1.2, .4, 2 ,9.2 ,10 ,2.9 ]

years2=[2004,2002,2000,2006,2007,2010]
years2.sort()
gdp2=[1.2, .4, 2 ,5.2 ,7 ,2.9 ]


plt.plot(years1,gdp1,"g-."); #"g-." -> green line dots
plt.plot(years2,gdp2,color="red");
plt.show()


