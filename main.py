import numpy as np
import pylab as pl
from matplotlib import collections  as mc
import random
import interval

intervalArray = []
for i in range(5):
# (minLow, maxLow, minSize, maxSize)
    x = interval.Interval(5,40,10,15)
    print(x)


queryLow = random.randint(10,35)
queryInterval=[queryLow, queryLow + random.randint(12,13)]
print(queryInterval)

# query_x = random.randint(1,80)
# query_interval=[[(query_x,50),(query_x,0)]]
# # 
# intervals=[]
# for i in range(40):
#     small_x=random.randint(0,80)
#     intervals.append([(small_x, i+2),(small_x+random.randint(40,60), i+2)])

# intervalCollection = mc.LineCollection(intervals, colors="Blue", linewidths=3)
# queryCollection = mc.LineCollection(query_interval, colors = "Red", linewidth=3)
# fig, ax = pl.subplots()
# ax.add_collection(intervalCollection)
# ax.add_collection(queryCollection)
# print(query_interval)
# ax.autoscale()
# ax.margins(0.1)
# pl.show()