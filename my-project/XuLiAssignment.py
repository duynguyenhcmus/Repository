#Xu Li Du Lieu Thong Ke - Assignment 03
#Ten: Nguyễn Đức Vũ Duy
#MSSV: 18110004
import pandas as pd
from pandas import Series,DataFrame
import numpy as np
#Tao ra mot Series co cac chi so la a, b, c va du lieu la 0, 1, 2
object = Series(range(3), index=['a', 'b', 'c'])
index = object.index
print(index)
#Print ra cac chi so tu 1 tro di 
print(index[1:])
#
index = pd.Index(np.arange(3))
obj2 = Series([1.5, -2.5, 0], index=index)
print(obj2.index is index)

