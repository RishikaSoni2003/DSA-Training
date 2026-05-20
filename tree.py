#can store tree by uing linkedlist and array
#creating tree using list

#LinkedList
# class Tree:
#     def __init__(self, data):
#         self.data= data
#         self.child =[]

#     def __str__(self, level=0):
#         ret=" "* level + str(self.data) + "\n"
#         for ch in self.child:
#             ret += ch.__str__(level+1)
#         return ret

#     def addChild(self, object):
#         self.child.append(object)
#         print("Tree Node Added")


# rootNode = Tree("Drinks")
# Hot = Tree("Payal")
# Cold= Tree("Cold")
# Tea=Tree("Tea")
# Coffee=Tree("Coffee")
# NonAlcholic=Tree("NonAlcholic")
# Alcholic=Tree("Alcholic")

# rootNode.addChild(Hot)#left
# rootNode.addChild(Cold)#right
# Hot.addChild(Tea)#left
# Hot.addChild(Coffee)#right
# Cold.addChild(NonAlcholic)#left
# Cold.addChild(Alcholic)#right

# print(rootNode)

