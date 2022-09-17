import random
import interval
import matplotlib.pyplot as plt


numberOfIntervals = 80
intervalArray = []
for i in range(numberOfIntervals):
# (minLow, maxLow, minSize, maxSize)
    x = interval.Interval(5,80,10,15)
    # print(x)
    intervalArray.append(x)


# plot intervals
for x in range(len(intervalArray)):
    # print(intervalArray[x].high)
    plt.plot((intervalArray[x].low,intervalArray[x].high), (x+1,x+1))

queryLow = random.randint(10,35)
queryInterval=[queryLow, queryLow + random.randint(12,13)]
print("Query Interval: "+str(queryInterval))
# print("Query Interval low: " + str(queryInterval[0])+" Query Interval High: " + str(queryInterval[1]))
plt.plot((queryInterval[0], queryInterval[1]), (0,0))
plt.plot((queryInterval[0], queryInterval[0]), (0,numberOfIntervals+1), 'k:')
plt.plot((queryInterval[1], queryInterval[1]), (0,numberOfIntervals+1), 'k:')
plt.show()