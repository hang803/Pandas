import pandas as pd
import numpy as np
dates=pd.date_range('2022-04-18',periods=6)
df=pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])
print(df)
print('col_A',df['A'],df.A)
print(df[0:3],df['2022-4-18':'2022-4-20'],sep='\n')#series of rows use direct_index

#choose_by_loc
print('loc',df.loc['20220422'])#one row use loc
print(df.loc['20220419',['A','B']])

#choose_by_iloc,index_loc,is similar with numpy
print('index_loc',df.iloc[-2:,[0,3]])

#choss_by_conditions
print('condition',df[df>5])
