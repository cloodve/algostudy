
class Node(object):
    def __init__(self, value, parentNode=None, leftNode=None, rightNode=None):
        self.leftNode = leftNode 
        self.rightNode = rightNode 
        self.parent = parentNode 
        self.value = value
    
class Tree(object):

    def __init__(self, rootValue):
        self.root = Node(rootValue)

    def _traverse_and_insert(self, parent, node, value):
        
        # Done with recursion
        if not node:
            n = Node(value, parent)
            if value < parent.value:
                parent.leftNode = n
            else:
                parent.rightNode = n 
            return node

        if value > node.value:
            return self._traverse_and_insert(node, node.rightNode, value)
        elif value < node.value:
            return self._traverse_and_insert(node, node.leftNode, value)
        elif node.value == value: # An error
            return None
        
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        elif value > self.root.value:
            return self._traverse_and_insert(self.root, self.root.rightNode, value)
        elif value < self.root.value:
            return self._traverse_and_insert(self.root, self.root.leftNode, value)
        else:
            pass # TODO: update the root 

    def max(self):
        node = self.root
        while node.rightNode:
            node = node.rightNode

        return node.value

    def min(self):
        node = self.root
        while node.leftNode:
            node = node.leftNode

        return node.value

    def _traverse(self, node, value):
        if not node:
            return None
        if value > node.value:
            return self._traverse(node.rightNode, value)
        elif value < node.value:
            return self._traverse(node.leftNode, value)
        elif value == node.value:
            return node
        
    def find(self, value):
        return self._traverse(self.root, value)

    def predecessor(self, value):
        node = self.find(value)
        if not node:
            return None 
        elif node.leftNode:
            node = node.leftNode
            while node.rightNode:
                node = node.rightNode
            return node
        elif not node.leftNode:
            node = node.parent
            # Follow parents until you find node that is less
            while node.value > value:
                node = node.parent 
            return node 

    def successor(self, value):
        node = self.find(value)
        if not node:
            return None
        elif node.rightNode:
            node = node.rightNode
            while node.leftNode:
                node = node.leftNode
            return node
        elif not node.rightNode:
            node = node.parent
            while node and node.value < value:
                node = node.parent     
            if not Node:
                return None
            return node

    def _inorder(self, node, l):
        if not node:
            return None
        self._inorder(node.leftNode, l)
        l.append(node)
        self._inorder(node.rightNode, l) 

    def _preorder(self, node, l):
        if not node:
            return None
        l.append(node)
        self._preorder(node.leftNode, l)
        self._preorder(node.rightNode, l)

    def _postorder(self, node, l):
        if not node:
            return None
        self._postorder(node.leftNode, l)
        self._postorder(node.rightNode, l)
        l.append(node) 

    def traverse(self, order='inorder'):
        ret = []
        if order == 'inorder':
            self._inorder(self.root, ret)     
        elif order == 'preorder':
            self._preorder(self.root, ret)
        elif order == 'postorder':
            self._postorder(self.root, ret)
         
        return ret        

    def delete(self, key):
        ret = True
        node = self.find(key)
        if not node.parent and not node.leftNode and not node.rightNode:
            self.root = None 
        elif not node.leftNode and not node.rightNode:
            if node.parent.value > node.value:
                node.parent.leftNode = None
            else:
                node.parent.rightNode = None
            node = None
        # Check for one child
        elif (not node.leftNode and node.rightNode): 
            tempNode = node.rightNode
            tempNode.parent = node.parent
            if tempNode.parent and tempNode.parent.value > tempNode.value:
                tempNode.parent.leftNode = tempNode
            elif tempNode.parent:
                tempNode.parent.rightNode = tempNode
            else:
                self.root = tempNode
        elif (not node.rightNode and node.leftNode):
            tempNode = node.leftNode
            tempNode.parent = node.parent
            if tempNode.parent and tempNode.parent.value > tempNode.value:
                tempNode.parent.leftNode = tempNode
            elif tempNode.parent:
                tempNode.parent.rightNode = tempNode
            else:
                self.root = tempNode
        elif (node.leftNode and node.rightNode):
            temp = self.predecessor(node.value)
            node, temp = temp, node

            node.parent, temp.parent = temp.parent, node.parent
            node.leftNode, temp.leftNode = temp.leftNode, node.leftNode
            node.rightNode, temp.rightNode = temp.rightNode, node.rightNode 

            if node.value == node.leftNode.value:
                node.leftNode = None
            elif temp.leftNode: 
                temp.parent.leftNode = temp.leftNode 
                temp.leftNode.parent = temp.parent

            temp.parent.rightNode = None
            temp.parent = None
            temp.leftNode = None
            temp.rightNode = None
            del temp

            if node.leftNode:
                node.leftNode.parent = node
            if node.rightNode:
                node.rightNode.parent = node

            if not node.parent:
                self.root = node

        else:
            ret = False
         
        return ret
        
