import pandas as pd
import numpy as np

#concatenating
# # <editor-fold desc="Description">
# df1=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
# df2=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
# df3=pd.DataFrame(np.ones((3,4))*3,columns=['a','b','c','d'])
# print(df1,df2,df3,sep='\n')
# print('vertical\n',pd.concat((df1,df2),axis=0,ignore_index=1))#ignore_index,delete its indexes
# print('horizontal\n',pd.concat((df1,df2,df3),axis=1))
# # </editor-fold>

#join
# # <editor-fold desc="Description">
# df11=pd.DataFrame(np.ones((3,4))*1,index=[1,2,3],columns=['a','b','c','d'])
# df22=pd.DataFrame(np.ones((3,4))*2,index=[2,3,4],columns=['b','c','d','e'])
# print(df11,df22,sep='\n')
# print('concat directly\n',pd.concat((df11,df22),ignore_index=1))#initial join='outer'
# print('concat join=inner\n',pd.concat((df11,df22),join='inner'))#cut the col which is not contained together
# # </editor-fold>

#append
# <editor-fold desc="Description">
df111=pd.DataFrame(np.ones((3,4))*1,index=[1,2,3],columns=['a','b','c','d'])
df222=pd.DataFrame(np.ones((3,4))*2,index=[2,3,4],columns=['b','c','d','e'])
df333=pd.DataFrame(np.ones((3,4))*3,index=[3,4,5],columns=['b','c','d','e'])
print('append',df111.append([df222,df333],ignore_index=1,),sep='\n')
s1=pd.Series(np.arange(4),index=['a','b','c','d'])
print('append_one_series\n',df111.append(s1,ignore_index=1))
# </editor-fold>