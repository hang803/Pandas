import pandas as pd
import numpy as np
data=pd.read_csv('data0.csv')
data1=pd.read_excel('data1.xlsx',index_col=0,)
print(data,data1,sep='\n')
data.to_pickle('data0.pickle')