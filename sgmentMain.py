import interval
import matplotlib.pyplot as plt
import sgmntTree

plotResults = True
numberOfIntervals = 100
minLow = 10
maxLow = 6*numberOfIntervals
minSize = 5
maxSize = 20
intervals = []
for i in range(numberOfIntervals):
    x = interval.Interval(minLow,maxLow,minSize,maxSize)
    # print(x)
    intervals.append(x)
Tree = sgmntTree.SegmentTree()
root = None
root = Tree.build(minLow, maxLow+maxSize)
for x in intervals:
    Tree.insert(x.low, x.high, root)

# Tree.inOrder(root)
# Tree.printTreeInPdf("segment_tree.gv",root)

#get a random query point
queryPoint = interval.Interval(minLow, maxLow, 0,0)
print("Query Point: "+str(queryPoint.low))

Tree.query(root, queryPoint.low)

# plot intervals
if(plotResults):
    for x in range(len(intervals)):
        # print(intervalArray[x].high)
        plt.plot((intervals[x].low,intervals[x].high), (x+1,x+1))
    # print("Query Interval low: " + str(queryInterval[0])+" Query Interval High: " + str(queryInterval[1]))
    plt.plot((queryPoint.low, queryPoint.low), (0,numberOfIntervals+1), 'k:')
    plt.show()
