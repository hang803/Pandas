import pandas as pd
import numpy as np
dates=pd.date_range('20220419',periods=4)
df=pd.DataFrame(np.arange(16).reshape(4,4),index=dates,columns=['a','b','c','d'])
df.iloc[0,1]=np.nan
df.iloc[1,2]=np.nan
print(df)
print('dropna',df.dropna(axis=0,how='any'),sep='\n')###axis=0(rows),1(cols),how='any','all'
print('fillna\n',df.fillna(0))
print('isnull\n',df.isnull())
print('check nan exist',np.any(df.isnull()))