class BSTNode:

    def __init__(self, k):
        self.key = k
        self.parent = None
        self.left = None
        self.right = None


    def find(self, key):
        if self.key == key:
            return self
        elif self.key < key:
            if self.right is not None:
                return self.right.find(key)
            else:
                return None
        else:
            if self.left is not None:
                return self.left.find(key)
            else:
                return None


    def  insert(self, node):
        if node is None:
            return

        if node.key > self.key:
            if self.right is not None:
                self.right.insert(node)
            else:
                self.right = node
                node.parent = self
        else:
            if self.left is not None:
                self.left.insert(node)
            else:
                node.parent = self
                self.left = node

    """
    Returns minimum element located at subtree with current node as root
    """
    def find_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current


    """
    Returns node with the largest key located at subtree with current node as root
    """
    def find_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current


    def next_smaller(self):
        if self.left is not None:
            return self.left.find_max()
        current = self
        while current.parent is not None and current is current.parent.left:
            current = current.parent
        return current.parent

    def next_larger(self):
        if self.right is not None:
            return self.right.find_min()
        current = self
        while current.parent is not None and current is current.parent.right:
            current = current.parent
        return current

    def delete(self):
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            self.parent = None
            return self
        else:
            successor = self.next_larger()
            self.key, successor.key = successor.key, self.key
            return successor.delete()

    def in_order_traversal(self):
        if self.left is not None:
            self.left.in_order_traversal()
        print "-%s- "%(self.key)
        if self.right is not None:
            self.right.in_order_traversal()



class BST:
    def __init__(self):
        self.root = None

    def find(self,key):
        # print "in BST Find Found %s" %(self.root.find(key))
        return self.root and self.root.find(key)

    def find_min(self):
        return self.root and self.root.find_min()

    def find_max(self):
        return self.root and self.root.find_max()

    def insert(self, key):
        newNode = BSTNode(key)
        if self.root == None:
            self.root = newNode
            return
        else:
            self.root.insert(newNode)


    def delete(self, key):
        # print "%s found" %(self.find(key))
        delNode = self.find(key)
        if delNode is None:
            print "Node Not Found"
            return None
        if delNode is self.root:
            pseudoRoot = BSTNode(0)
            self.root.parent = pseudoRoot
            pseudoRoot.left = self.root
            deleted = self.root.delete()
            self.root = pseudoRoot.left
            if self.root is not None:
                self.root.parent = None
            return deleted
        else:
            return delNode.delete()

    def next_larger(self, key):
        nextNode = self.root.find(key)
        return nextNode and nextNode.next_larger()

    def next_smaller(self,key):
        nextNode = self.root.find(key)
        return nextNode and nextNode.next_smaller()

    def in_order_traversal(self):
        if self.root is None:
            print "Empty BST"
        else:
            self.root.in_order_traversal()



newBST = BST()
newBST.in_order_traversal()
newBST.insert(30)
newBST.insert(25)
newBST.insert(35)
newBST.insert(42)
newBST.insert(15)
newBST.insert(2)
newBST.insert(5)
newBST.insert(37)
newBST.insert(12)
print "BST min element is %s " %(newBST.find_min().key)
print "BST max element is %s " %(newBST.find_max().key)
newBST.in_order_traversal()
# print "BST Root key %s" %(newBST.root.key)
# print newBST.delete(30)
# print "New root %s" %(newBST.root.key)
# print newBST.delete(35)
# print "New root %s" %(newBST.root.key)
# print newBST.delete(37)
# print "New root %s" %(newBST.root.key)
# print newBST.delete(42)
# print "New root %s" %(newBST.root.key)
# print newBST.delete(25)
# print "New root %s" %(newBST.root.key)
# print newBST.delete(15)
# print "New root %s" %(newBST.root.key)
# print newBST.delete(12)
# print "New root %s" %(newBST.root.key)
# print newBST.delete(5)
# print "New root %s" %(newBST.root.key)
# print newBST.delete(2)
#
# newBST.in_order_traversal()
