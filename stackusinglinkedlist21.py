# import time

# class Node:
#     def __init__(self, value = None):
#         self.value = value
#         self.next = None
        
# class LinkedList:
#     def __init__(self):
#         self.head = None
        
# class Stack:
#     def __init__(self):
#         self.LinkedList = LinkedList()
        
#     def __str__(self):
#         values = []
#         current = self.LinkedList.head
        
#         while current:
#             values.append(str(current.value))
#             current = current.next
            
#         return '\n'.join(values)
        
#     def isEmpty(self):
#         if self.LinkedList.head == None:
#             return True
#         else:
#             return False
        
#     def push(self, value):
#         node = Node(value)
#         node.next = self.LinkedList.head
#         self.LinkedList.head = node
        
#     def pop(self):
#         if self.isEmpty():
#             return "There is no element in the stack"
#         else:
#             nodeValue = self.LinkedList.head.value
#             self.LinkedList.head = self.LinkedList.head.next
#             return nodeValue
        
#     def peek(self):
#         if self.isEmpty():
#             return "There is no element in the stack"
#         else:
#             nodeValue = self.LinkedList.head.value
#             return nodeValue
        
#     def delete(self):
#         self.LinkedList.head = None
    
# customStack = Stack()
# customStack.push(1)
# customStack.push(2)
# customStack.push(3)
# print(customStack)
# print("Display Top values: ")
# print(customStack.peek())
# print("pop top elements: ")
# print(customStack.pop())
# print("Now checck the stack again")
# print(customStack)
# print("pop top elements: ")
# print(customStack.pop())
# print("Now checck the stack again")
# print(customStack)


