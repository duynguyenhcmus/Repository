#Xu Li Du Lieu Thong Ke - Assignment 03
#Ten: Nguyễn Đức Vũ Duy
#MSSV: 18110004
import pandas as pd
from pandas import Series,DataFrame
import numpy as np
#Index Object
#Tao ra mot Series co cac chi so la a, b, c va du lieu la 0, 1, 2
object = Series(range(3), index=['a', 'b', 'c'])
index = object.index
print(index)
#Print ra cac chi so tu 1 tro di 
print(index[1:])
#Phan tu chi so la thuoc Immutable data (khong thay doi duoc boi user) va co the chia se cho nhieu loai cau truc du lieu khac nhau
index = pd.Index(np.arange(3))
obj2 = Series([1.5, -2.5, 0], index=index)
print(obj2.index is index)
#Them index vao cuoi
index2=pd.Index([3,4,5])
index3=index.append(index2) 
print(index3)
#Arithmetic and Data Alignment
#Khoi tao 2 series
s1 = Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
#tinh tong 2 series trong do phan tu khong co se de la NaN
print(s1+s2)
#Tuong tu cho DataFrame, phan tu khong co se de NaN
df1 = DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),index=['Ohio', 'Texas', 'Colorado'])
df2 = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(df1+df2)
#Tinh tong df1 va df2 nhung phan tu khong co se de phan tu cua df2
df1 = DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
print(df1.add(df2, fill_value=0))
#index lay cua df2 nhung data cua df1, nhung phan tu df1 khong co ma df2 co thi de la 0
print(df1.reindex(columns=df2.columns, fill_value=0))
#in mot mang co kich thuoc 3x4 trong do phan tu tung dong bang phan tu dong do tru phan tu dong dau tien tuong ung
arr = np.arange(12.).reshape((3, 4))
print(arr-arr[0])
#Tuong tu nhu voi series, ta cung co cau lenh tuong tu voi DataFrame
frame = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),index=['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.iloc[0]
print(frame-series)
#Neu nhu co index ma series2 va frame khong giao nhau thi se de la NaN
series2 = Series(range(3), index=['b', 'e', 'f'])
print(frame + series2)
#Tuong tu nhu tren, ta broadcast voi phep tinh tru.
series3 = frame['d']
print(frame.sub(series3, axis=0))
#in ra ket qua cua hieu so lon nhat voi so be nhat theo tung cot
frame = DataFrame(np.random.randn(4, 3), columns=list('bde'),index=['Utah', 'Ohio', 'Texas', 'Oregon'])
f = lambda x: x.max() - x.min()
print(frame.apply(f))
#Tuong tu in ra ket qua cua hieu so lon nhat voi so be nhat theo tung dong
print(frame.apply(f, axis=1))
#In ra frame duoi dang so thap nhan lay 2 chu so sau dau phay
format = lambda x: '%.2f' % x
print(frame.applymap(format))
#Lam tron den 2 chu so thap phan cho index e cua frame
print(frame['e'].map(format))
#Sap xep index theo thu tu tang dan cua bang chu cai
obj = Series(range(4), index=['d', 'a', 'b', 'c'])
print(obj.sort_index())
#Sap xep index cua DataFrame theo thu tu tang dan
frame1 = DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'],columns=['d', 'a', 'b', 'c'])
print(frame1.sort_index())
#Tuong tu nhu tren nhung la sap xep columns theo thu tu tang dan
print(frame1.sort_index(axis=1))
#Sap xep columns theo thu tu giam dan
print(frame1.sort_index(axis=1, ascending=False))
#Sap xep gia tri cac phan tu cua Series theo thu tu tang dan
obj1 = Series([4, 7, -3, 2])
print(obj1.sort_values())
#Sap xep gia tri cac phan tu cua dataframe theo thu tu tang dan va uu tien phan tu cua cot a truoc
frame2 = DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
print(frame2.sort_values(by=['a', 'b']))
#Xuat ra mot Series co values tuong ung la so thu tu cua values khi sap xep tang dan va de them .5 neu co 2 phan tu bang nhau
obj3 = Series([7, -5, 7, 4, 2, 0, 4])
print(obj3.rank())
#Tuong tu nhu tren nhung khi co 2 phan tu bang nhau thi sap xep theo phan tu nao xuat hien truoc thi nho hon
print(obj3.rank(method='first'))
#Tuong tu nhu tren nhung sap xep theo thu tu giam dan va phan tu bang nhau thi co value bang max vi tri cua chung
print(obj3.rank(ascending=False, method='max'))
#Xuat ra rank theo tung hang
frame4 = DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1],'c': [-2, 5, 8, -2.5]})
print(frame4.rank(axis=1))
#Kiem tra xem index co khac nhau tung doi mot khong
obj2 = Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
print(obj2.index.is_unique)
#Khi co index bi trung thi khi truy xuat, ket qua tra ve se la mot vecto
print(obj2['a'])
#Tuong tu voi dataframe thi ket qua tra ve so co dang mot ma tran
df_a = DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
print(df_a.loc['b'])
#Using DataFrame's Columns
#Tao ra mot dataframe moi su dung c, d lam index
frame5 = DataFrame({'a': range(7), 'b': range(7, 0, -1),'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],'d': [0, 1, 2, 0, 1, 2, 3]})
frame6 = frame5.set_index(['c', 'd'])
print(frame6)
#Giu nguyen cot c,d thay vi chi xuong 1 dong lam index moi
print(frame5.set_index(['c', 'd'], drop=False))
#reset index, cho cac index lam thanh 1 dong
print(frame6.reset_index())
#Handling Missing Data
#Kiem tra co phan tu null hay khong 
string_data = Series(['aardvark', 'artichoke', np.nan, 'avocado'])
print(string_data.isnull())
#Tuong tu nhu tren nhung phan tu cua Series co the thay doi duoc boi user
string_data[0] = None
print(string_data.isnull())
#Tra ve Series khong co cac phan tu khong co gia tri (nan) nhung series khong thay doi
data = Series([1, np.nan, 3.5, np.nan, 7])
print(data.dropna())
#Tuong tu nhu tren, ta co the dung truy xuat index co value khong phai null
print(data[data.notnull()])
#Tao ra mot Dataframe bo di cac dong co phan tu NaN.
data = DataFrame([[1., 6.5, 3.], [1., np.nan, np.nan],[np.nan, np.nan, np.nan], [np.nan, 6.5, 3.]])
cleaned = data.dropna()
print(cleaned)
#Xuat ra DataFrame ma chi bo dong co tat ca phan tu la NaN
print(data.dropna(how='all'))
#Bo di cot ma co tat ca phan tu la NaN
data[4] = np.NaN
print(data.dropna(axis=1, how='all'))
#Chon ra nhung dong ma co it nhat thresh phan tu khac NaN
df = DataFrame(np.random.randn(7, 3))
df.iloc[:4, 1] = np.nan
df.iloc[:2, 2] = np.nan
print(df.dropna(thresh=2))
#Nhung phan tu la NaN thay bang 0
print(df.fillna(0))
#Thay nhung phan tu la NaN o cac cot bang phan tu da dinh
print(df.fillna({1: 0.5, 2: -1}))
#Thay doi dataframe co san trong do cac phan tu NaN thay bang 0
df.fillna(0, inplace=True)
print(df)
#Thay cac phan tu NaN trong Series bang trung binh cua cac phan tu co san
data = Series([1., np.nan, 3.5, np.nan, 7])
print(data.fillna(data.mean()))