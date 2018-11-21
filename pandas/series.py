"""
Series Data Structure in Pandas
"""

import pandas as pd;
from pandas import Series,DataFrame;

series1=Series([1,'a',4,True])
series2=Series([1,2,3,4,5], index=['a','b','c','d','e'])

print series1
print series2

sampleDic = {"key1":"value1","key2":"value2"}

series3 = Series(sampleDic)

print series3

#set
sampleSet = (1,2,3,4,5)

series4=Series(sampleSet)

print series4

sampleArr= [1,2,3,4,5,6]

series5=Series(sampleArr)

print series5


series6 =  Series(sampleDic,index=["key1","key4"])
print series6

#return true for null value keys
#same as py.isnull(series6)
print series6.isnull()

#same series6.notnull()
print pd.notnull(series6)


series6.name="test series"
series6.index.name="test keys"

print series6

#altering the index of series
series6.index=["key-a","key-b"]
print series6