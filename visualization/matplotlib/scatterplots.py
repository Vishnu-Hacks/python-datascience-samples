# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 13:39:18 2018

@author: vishn
"""

""" scatterplots best for paired set of data """

from matplotlib import pyplot as plt

friends=[70,65,72,63,71,64,60,64,67]
minutes=[175,170,205,120,220,130,105,145,190]
names=['adithya','noble','aswin','daisy','e','f','g','h','i']



plt.scatter(friends,minutes)

plt.title("time spend on 2 social media by people with different # of friends") 
plt.xlabel("number of friends")
plt.ylabel("# of minutes")   
           
plt.show()


""" combining two different scatter plots ex: minutes my friends spends in two different 
social medias """

plt.scatter(friends,minutes)# time spent on fb
for name,friend,minute in zip(names,friends,minutes):
      plt.annotate(name,xy=(friend,minute))
      
friends=[70,65,72,63,71,64,60,64,67]
minutes=[10,11,12,100,120,130,105,145,190]
names=['adithya','noble','aswin','daisy','e','f','g','h','i']

plt.scatter(friends,minutes) # time spent on instagram

#adding labels to the points
for name,friend,minute in zip(names,friends,minutes):
      plt.annotate(name,xy=(friend,minute))

plt.title("time spend on 2 social media by people with different # of friends") 
plt.xlabel("number of friends")
plt.ylabel("# of minutes")     
     
plt.show()

""" design can be customized in different ways """