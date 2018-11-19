#方差分析时数据往往不存在相同的情况
# 1组很多时候只有1个数据，因此改造成分阶段归组

import pandas as pd
import numpy as np
from scipy.stats import f
dataframe = pd.read_excel('D:/test.xlsx')
data = np.array(dataframe)

x = 1
y = 4
#不同组之间的方差分析，暂选1 4列


maxnum = np.max(data[: ,x])
minnum = np.min(data[:, x])

if(minnum == maxnum): maxnum += 1
interval = (maxnum - minnum) / 50
#我们假设最大到最小共有50组
num = minnum
vectorx = []
vectory = []
len = len(data[:, x])
#print(data[:, x],data[: ,y])
AVG = np.mean(data[:, y])

df = 49 #自由度
while(num < maxnum):
    vecx = []
    vecy = []
    for i in range(len):
        if(data[i, x] < num + interval and data[i, x] >=num):
            vecx.append(data[i, x])
            vecy.append(data[i, y])
    if(vecx == []): df -= 1
    else:
        vectorx.append(vecx)
        vectory.append(vecy)
    num += interval
SSE = 0
SSA = 0

for vecy in vectory:
    array_y = np.array(vecy)
    arraymean = array_y.mean()
    arrayvar = 0
    for Y in array_y:
        arrayvar += (Y - arraymean) * (Y - arraymean)
        SSE += (arraymean - AVG) * (arraymean - AVG) #组间
    SSA += arrayvar #组内

SA = SSA / (298 - df)
SE = SSE / (df - 1)
F = SE / SA
print(SSE, SSA, df, SE, SA, F)

p = f.sf(F, df-1 ,298-df)
print(p)