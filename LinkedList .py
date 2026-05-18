# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class linkedlist:
#     def __init__(self):
#         self.head=None
# linkedlist=linkedlist()
# linkedlist.head=Node(5)
# second=Node(10)
# third=Node(15)
# fourth=Node(20)
# linkedlist.head.next=second
# second.next=third
# third.next=fourth
# while linkedlist.head!=None:
#     print(linkedlist.head.data,"|","-->",end=' ')
#     linkedlist.head = linkedlist.head.next

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     # Add node at end
#     def addNode(self, value):

#         node = Node(value)

#         if self.head is None:
#             self.head = node
#             self.tail = node
#         else:
#             self.tail.next = node
#             self.tail = node

#     # Display linked list
#     def display(self):

#         if self.head is None:
#             print("Linked List is empty")
#         else:
#             temp = self.head

#             while temp is not None:
#                 print(temp.data, end=" -> ")
#                 temp = temp.next

#             print("None")


# if __name__ == "__main__":

#     obj = LinkedList()

#     while True:

#         print("\n1. Add node in linked list")
#         print("2. Display linked list")
#         print("3. Exit")

#         ch = int(input("Enter your choice: "))

#         if ch == 1:

#             value = int(input("Enter value for node: "))
#             obj.addNode(value)

#             print("Node added successfully")

#         elif ch == 2:

#             obj.display()

#         elif ch == 3:

#             print("Program ended")
#             break

#         else:
#             print("Invalid choice")
 
#linked list operations
import sys 
class Node:
    def __init__(self,data):
         self.data=data
         self.next=None
class linkedlist:
     def __init__(self):
        self.head=None
        self.tail=None
     def addNode(self,value):
         self.node=Node(value)
         if self.head is None:
             self.head=self.node
             self.tail=self.node
         else:
             self.tail.next=self.node
             self.tail=self.node
     def display(self):
        while self.head!=None:
            print(self.head.data,"|","-->",end=' ')
            self.head=self.head.next
     def addnodebig(self,value):
         print("Add node beginning:")
         self.node=Node(value)
         if self.head is None:
             self.head=self.node
             self.tail=self.node
         else:
             self.node.next=self.head
             self.head=self.node


if __name__=="__main__":
    object=linkedlist()
    while True:
        print('1.Add node linkedlist:')
        print('2.Add node in beginning:')
        print('3.Add node in between:')
        print('4.Add node end:')
        print('5.Display linked list:')
        print('6.Exit')
        ch=int(input('enter your choice:'))
        if ch==1:
            value=int(input('enter value for node:'))
            object.addNode(value)
            print('Node added successfully in single linkedlist')
        elif ch==2:
            value=int(input('enter value for node:'))
            object.addnodebig(value)

        elif ch==5:
            object.display()
        elif ch==6:
            sys.exit()