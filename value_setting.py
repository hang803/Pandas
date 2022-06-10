import pandas as pd
import numpy as np
dates=pd.date_range('20220419',periods=4)
df=pd.DataFrame(np.arange(16).reshape(4,4),index=dates,)
print(df)
df.iloc[2,2]=22
df.loc['20220420',2]=12
df[2][df[0]<=4]=0
df['a']=np.nan
df['b']=pd.Series(np.arange(4),index=dates)
print(df)