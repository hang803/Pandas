import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# <editor-fold desc="series">
data=pd.Series(np.random.randn(1000))
data=np.cumsum(data)
data.plot()
plt.show()
# </editor-fold>
# <editor-fold desc="DataFrame">
data1=pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list('abcd'))
data1=data1.cumsum()
fig=data1.plot.scatter('a','b',label='c1')
data1.plot.scatter('a','c',c='r',ax=fig,label='c2')
plt.show()
# </editor-fold>