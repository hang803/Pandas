import pandas as pd
import numpy as np
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
s=pd.Series([1,2,3,4,np.nan],index=['a','b','c','d','e'])#only float32 64 dtype,np.nan==None
print(s)
dates=pd.date_range('20220415',periods=6)
print(dates)

df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'],)#index,columns init=[0,1,2,3...]
print(df)
df1=pd.DataFrame(np.arange(12).reshape(3,4))
print(df1)
df2=pd.DataFrame({'A':1.,
                  'B':pd.Timestamp('20220417'),
                  'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                  'D':np.arange(4,dtype='int32'),
                  'E':pd.Categorical(['test','wen','yu','chan']),
                  'F':'foo'},index=['a','b','c','d'])
print(df2)

#property
print('data dtypes',df2.dtypes)
print('df2 index',df2.index)#rows_names
print('df2_columns',df2.columns)#columns_names
print('df2_value',df2.values)
print('df2_describe\n',df2.describe())#operatate nums
print('df2.transpose\n',df2.T)
print('df2_sort_index\n',df2.sort_index(axis=1,ascending=False))#axis=1,horizontal;axis=0,vertical###ascending><decend
print('df2_sort_value',df2.sort_values('D',axis=0,ascending=False),sep='\n')