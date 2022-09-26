from graphviz import Digraph

class Node(object):
    def __init__(self, range):
        self.range = range
        self.key = None
        self.intervals = []
        self.rightChild = None
        self.leftChild = None

    def __str__(self):
            return "(" + str(self.range[0]) + ", " + str(self.range[1]) + ") " +str(self.intervals[:])


class SegmentTree(object):
    # 0 <= s < t <= max_range
    def build(self, s, t) :
        v = Node([s,t])
        if(s+1 < t):
            m = (s+t) // 2
            v.key = m
            v.leftChild = self.build(s, m)
            v.rightChild = self.build(m, t)
        return v

    # v node of tree
    # b begining of interval
    # e end of interval
    def insert(self, b, e, v):
        # if interval contains v.range
        if(b <= v.range[0] and e >= v.range[1]):
            v.intervals.append([b,e])
        else:
            if(b < v.key): 
                self.insert(b, e, v.leftChild)
            if(v.key < e): 
                self.insert(b, e, v.rightChild)

    def query(self, root, point):
        if(len(root.intervals) > 0):
            print("Found in: "+str(root.intervals))
        # if is not leaf
        if(root.leftChild or root.rightChild):
            # go left
            if(root.leftChild and (root.leftChild.range[0] <= point and point <= root.leftChild.range[1])):
                self.query(root.leftChild, point)
            # go right
            elif(root.rightChild):
                self.query(root.rightChild, point)
    
    def printTreeInPdf(self, filename,root):
        g = Digraph('G', filename=filename)
        node_list = [root]
        while(len(node_list) != 0):
            current_node = node_list[0]
            node_list.pop(0)
            if(current_node.leftChild):
                g.edge(str(current_node.key)+"\n"+str(current_node.range), str(current_node.leftChild.key)+"\n"+str(current_node.leftChild.range))
                node_list.append(current_node.leftChild)
            if(current_node.rightChild is not None):
                g.edge(str(current_node.key)+"\n"+str(current_node.range), str(current_node.rightChild.key)+"\n"+str(current_node.rightChild.range))
                node_list.append(current_node.rightChild)
        g.view()
        return
    

    def inOrder(self, root):
        if root == None:
            return
        self.inOrder(root.leftChild)
        print(root)
        self.inOrder(root.rightChild)

