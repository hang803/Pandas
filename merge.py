import pandas as pd
import numpy as np
# <editor-fold desc="merge by the base on key">
# left=pd.DataFrame({'key':['k0','k1','k2','k3'],
#                    'a':['a0','a1','a2','a3'],
#                    'b':['b0','b1','b2','b3']})
# right=pd.DataFrame({'key':['k0','k1','k2','k3'],
#                    'c':['c0','c1','c2','c3'],
#                    'd':['d0','d1','d2','d3']})
# print(left,right,sep='\n')
# m1=pd.merge(left,right,on='key',)
# print('base on key\n',m1)
# </editor-fold>
# # <editor-fold desc="two key">
# left=pd.DataFrame({'key0':['k0','k1','k2','k3'],
#                    'key1':['k0','k0','k2','k3'],
#                    'a':['a0','a1','a2','a3'],
#                    'b':['b0','b1','b2','b3']})
# right=pd.DataFrame({'key0':['k0','k1','k1','k3'],
#                     'key1':['k0','k0','k0','k1'],
#                    'c':['c0','d1','c2','c3'],
#                    'd':['d0','d1','d2','d3']})
# print(left,right,sep='\n')
# m2=pd.merge(left,right,on=['key0','key1'],how='right')#how=in,out,left,right
# print('base on two keys\n',m2)
# # </editor-fold>
# # <editor-fold desc="indicator">
# df1=pd.DataFrame({'col':[0,1],
#                   'col_left':['a','b']})
# df2=pd.DataFrame({'col':[1,2,2],
#                   'col_left':[2,2,2]})
# print(df1,df2,sep='\n')
# m3=pd.merge(df1,df2,on='col',how='outer',indicator='indicator_column')#indicator=tell me data exist in where(left_only,right,both)
# print(m3)
# # </editor-fold>
# # <editor-fold desc="merge by index">
# left=pd.DataFrame({'a':['a0','a1','a2','a3'],
#                    'b':['b0','b1','b2','b3']},index=[0,1,2,3])
# right=pd.DataFrame({'c':['c0','c1','c2','c3'],
#                    'd':['d0','d1','d2','d3']},index=[2,3,4,5])
# print(left,right,sep='\n')
# m1=pd.merge(left,right,left_index=True,right_index=True,how='outer',indicator='indicator')
# print(m1)
# # </editor-fold>
# <editor-fold desc="suffixes">
boys=pd.DataFrame({'k':['zhang','yue','feng'],'age':[2,3,4]})
girls=pd.DataFrame({'k':['wen','cui','zhang'],'age':[5,6,7]})
print(boys,girls,sep='\n')
m=pd.merge(boys,girls,on='k',suffixes=['_b','_g'],how='outer')#suffixes:the explain behind the same col
print(m)
# </editor-fold>