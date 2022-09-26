import interval
import intervalTree
import matplotlib.pyplot as plt

plotResults = True
numberOfIntervals = 100
minLow = 10
maxLow = 6*numberOfIntervals
minSize = 5
maxSize = 20
intervalArray = []
tree = intervalTree.Interval_Tree()
root = None
for i in range(numberOfIntervals):
    x = interval.Interval(minLow,maxLow,minSize,maxSize)
    root = tree.insert(root, x)
    if(plotResults):
        intervalArray.append(x)
# print("PreOrder traversal of constructed Interval Tree is")
# tree.preOrder(root)
# print("InOrder traversal of constructed Interval Tree is")
# tree.inOrder(root)
queryInterval = interval.Interval(minLow, maxLow, minSize,maxSize)
print("Query Interval: "+str(queryInterval))
print("First overlap with: "+str(tree.searchInterval(root, queryInterval)))
print("All overlaps: ")
tree.searchAllOvelaps(root, queryInterval)
print("Ran for " + str(numberOfIntervals) + " intervals")
# tree.printTreeInPdf("interval_tree.gv",root)

# plot intervals
if(plotResults):
    for x in range(len(intervalArray)):
        # print(intervalArray[x].high)
        plt.plot((intervalArray[x].low,intervalArray[x].high), (x+1,x+1))
    # print("Query Interval low: " + str(queryInterval[0])+" Query Interval High: " + str(queryInterval[1]))
    plt.plot((queryInterval.low, queryInterval.high), (0,0))
    plt.plot((queryInterval.low, queryInterval.low), (0,numberOfIntervals+1), 'k:')
    plt.plot((queryInterval.high, queryInterval.high), (0,numberOfIntervals+1), 'k:')
    plt.show()