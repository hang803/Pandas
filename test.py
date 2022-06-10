import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
df=pd.read_csv('covid19_day_wise.csv')
array=np.array(df)
dates=pd.date_range(array[0,0],periods=array.shape[0])
data=pd.DataFrame(array[:,1:],index=dates,columns=df.columns[1:])
# 获取 2020 年 2 月 3 日的所有数据
print(data.loc['2020-02-03'])
# 2020 年 1 月 24 日之前的累积确诊病例有多少个？
print(data.loc['2020-01-24','Confirmed'])
# 2020 年 7 月 23 日的新增死亡数是多少？
print(data.loc['20200723','New deaths'])
# 从 1 月 25 日到 7 月 22 日，一共增长了多少确诊病例？
print(data.loc['20200125':'20200722','New cases'].sum())
# 每天新增确诊数和新恢复数的比例？平均比例，标准差各是多少？
zero_mask=data.loc[:,'New recovered']!=0
ratio=data.loc[zero_mask,'New cases']/data.loc[zero_mask,'New recovered']
print(ratio.mean(),ratio.std())
# 画图展示新增确诊的变化曲线
# 画图展示死亡率的变化曲线
fig,ax1=plt.subplots()
ax2=ax1.twinx()
ax1.plot(data.loc[:,'New cases'],'r')
ax2.plot(data.loc[:,'Deaths / 100 Cases'],'k')
ax1.set_ylabel('new cases')
ax2.set_ylabel('death ratio')
plt.show()