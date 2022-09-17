# Python code to insert a node in AVL tree
# Generic tree node class
import interval
from graphviz import Digraph # Print the tree in PDF

class Node(object):
    def __init__(self, range, max):
        self.range = range
        self.max = max
        self.right = None
        self.left = None
        self.height = 1

    def __str__(self):
        return "[" + str(self.range.low) + ", " + str(self.range.high) + "] " + "max = " + str(self.max) + "\n"


class Interval_Tree(object):
    def insert(self, root, x):
        
        if root == None:
            return Node(x, x.high)
        if x.low < root.range.low:
            root.left = self.insert(root.left, x)
        else:
            root.right = self.insert(root.right, x)
        if root.max < x.high:
            root.max = x.high

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balanceFactor = self.getBalance(root)   
        if balanceFactor > 1:
            if x.low < root.left.range.low:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if x.low >= root.right.range.low:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

		# Perform rotation
        y.left = z
        z.right = T2

		# Update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
		# Return the new root
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

		# Perform rotation
        y.right = z
        z.left = T3

		# Update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
		# Return the new root
        return y
    
    def getHeight(self, root):
        if root == None:
            return 0
        return root.height
    
    def getBalance(self, root):
        if root == None:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def preOrder(self, root):
        if root == None:
            return
        print("{0} ".format(root.range) + str(self.getBalance(root)))
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):
        if root == None:
            return
        self.inOrder(root.left)
        print(root, end="")
        if (self.getBalance(root)<-1 or self.getBalance(root)>1):
            print(self.getBalance(root), end="")
        self.inOrder(root.right)

    def printTreeInPdf(self, filename,root):
        g = Digraph('G', filename=filename)
        node_list = [root]
        while(len(node_list) != 0):
            current_node = node_list[0]
            node_list.pop(0)
            if(current_node.left):
                g.edge(str(current_node.max)+"\n"+str(current_node.range), str(current_node.left.max)+"\n"+str(current_node.left.range))
                node_list.append(current_node.left)
            if(current_node.right is not None):
                g.edge(str(current_node.max)+"\n"+str(current_node.range), str(current_node.right.max)+"\n"+str(current_node.right.range))
                node_list.append(current_node.right)
        g.view()
        return

if __name__ == '__main__':
    tree = Interval_Tree()
    root = None
    for i in range(100):
    # (minLow, maxLow, minSize, maxSize)
        x = interval.Interval(5,200,10,30)
        root = tree.insert(root, x)
    print("PreOrder traversal of constructed Interval Tree is")
    # tree.preOrder(root)
    print()
    # print("InOrder traversal of constructed Interval Tree is")
    # tree.inOrder(root)
    print()
    tree.printTreeInPdf("interval_tree.gv",root)
