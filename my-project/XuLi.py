import pandas as pd
from pandas import Series,DataFrame
import numpy as np
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],'year': [2000, 2001, 2002, 2001, 2002],'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
#print(frame)
#print(DataFrame(data, columns=['year', 'state', 'pop']))
frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],index=['one', 'two', 'three', 'four', 'five'])
#print(frame2)
#print(frame2.columns)
#print(frame2['state'])
#print(frame2.year)
#print(frame2.loc['three'])
frame2['debt'] = 16.5
#print(frame2)	
frame2['debt'] = np.arange(5.)
#print(frame2)
val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
#print(frame2)
frame2['eastern'] = frame2.state == 'Ohio'
#print(frame2)
del frame2['eastern']
#print(frame2.columns)
pop = {'Nevada': {2001: 2.4, 2002: 2.9},'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = DataFrame(pop,index=[2001,2002,2003])
#print(frame3)
#print(frame3.T)
#DataFrame(pop, index=[2001, 2002, 2003])
pdata = {'Ohio': frame3['Ohio'][:-1],'Nevada': frame3['Nevada'][:2]}
#print(DataFrame(pdata))
frame3.index.name = 'year'; frame3.columns.name = 'state'
#print(frame3)
obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
#print(obj2)
#print(obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0))
obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 3, 5])
#print(obj3.reindex(range(6), method='ffill'))
#print(obj3.reindex(range(6), method='bfill'))
frame = DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'],columns=['Ohio', 'Texas', 'California'])
#print(frame)
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
#print(frame2)
states = ['Texas', 'Utah', 'California']
#print(frame.reindex(columns=states))
#print(frame.reindex(index=['a', 'b', 'c', 'd'], method='ffill',columns=states))
#print(frame.iloc[[1, 2, 3, 4], states])
obj = Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
new_obj = obj.drop('c')
print(new_obj)
data = DataFrame(np.arange(16).reshape((4, 4)),index=['Ohio', 'Colorado', 'Utah', 'New York'],columns=['one', 'two', 'three', 'four'])
print(data.drop(['Colorado', 'Ohio']))