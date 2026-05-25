#full binary tree
# each node has either 0 or 2 Child  
# no node has a single child


# conplete binary tree
#all levels except possibely the last are completely filled
#nodes in the last level are filled from left to right

# perfect binary tree 
# all internal nodes have exactly 2 nodes 
# all leaf nodes are at the same level

#why binary tree 
# it performs faster that binary tree when inserting and deleting node 

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None     
        self.rightChild = None

def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
            
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data, end=" ")
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
    
def inOrderTraversal(rootNode): 
    if not rootNode:
        return
    preOrderTraversal(rootNode.leftChild)
    print(rootNode.data, end=" ")
    preOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
    print(rootNode.data, end=" ")
    
def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.rightChild, nodeValue)
 

newBST = BSTNode(None)
insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)
print("preorder: ")
preOrderTraversal(newBST)
print()
print("inorder: ")
inOrderTraversal(newBST)
print()
print("postorder: ")
postOrderTraversal(newBST)
print()
searchNode(newBST, 100)
