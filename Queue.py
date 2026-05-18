# 16 may

# def func(value, values): #[1, 2, 3]
#     var = 1
#     values[0] = 44
# t = 3
# v = [1, 2, 3]
# func(t, v)
# print(t, v[0])

# def f(i, values = []):
#     values.append(i)
#     print(values)
# f(1)
# f(2)
# f(3)

#Queue operations 

# def func(value,values):
#     var=1
#     values[0]=44
# t=3
# v=[1,2,3]
# func(t,v)
# print(t,v[0])

# def f(i,values=[]):
#     values.append(i)
#     print(values)
# f(1)
# f(2)
# f(3)

# import sys
# class Queue:
#     def __init__(self,size):
#         self.myQueue=[]
#         self.queuesize=size
#     def isFull(self):
#         if len(self.myQueue) == self.queuesize:
#             return True
#         else:
#             return False
#     def enqueue(self,value):      0
#         if self.isFull():
#             print("Queue is full")
#         else:
#             self.myQueue.append(value)
#             print("element added")
#     def display(self):
#         print(self.myQueue)
    
#     def isEmpty(self):
#         if self.myQueue==[]:
#             return True
#         else:
#             return False
#     def dequeue(self):
#         if self.isEmpty():
#             print("queue is empty")
#         else:
#             self.myQueue.pop(0)
#     def peek(self):
#         if self.isEmpty():
#             print("queue is empty")
#         else:
#             print(self.myQueue[0])
#     def deletequeue(self):
#         self.myQueue=None

# size= int(input("Enter the size of queue: "))
# obj=Queue(size) 
# print("Queue has created")
# while True:
#     print("1.Enqueue operation:")
#     print("2.display queue:")
#     print("3.delete operation:")
#     print("4. peek operation")
#     print("5.delete queue")
#     print("7.Exit")
#     choice=int(input("enter your choice:"))
#     if choice==1:
#         value=int(input("enter value to push in queue:"))
#         obj.enqueue(value)
       
#     elif choice==2:
#         obj.display()
#     elif choice==3:
#         obj.dequeue(3)
#     elif choice==4:
#         obj.peek()
#     elif choice==5:
#         obj.deletequeue()
#     else:
#         sys.exit()

# fruit={}
# def addOne(index):
#     if index in fruit:
#         fruit[index]+=1
#     else:
#         fruit[index]=1
# addOne("Apple")
# addOne("BANANA")
# addOne("APPLE")
# print(len(fruit))

# Write a program to access each character of string in forward and
# backward direction by using while loop?

# s = "Learning Python is very easy"

# n = len(s)
# i = 0

# print("Forward direction")
# while i < n:
#     print(s[i], end=' ')
#     i = i + 1

# print("\nBackward direction")

# i = -1
# while i >= -n:
#     print(s[i], end=' ')
#     i = i - 1

# v=['a','e','i','o','u']
# w=input("enter the word where will search the vowels:")
# found=[]
# for i in w:
#     if i in v:
#         if i not in found:
#             found.append(i)
# print('found vowels:',found)
# print('unique vowels:',len(found),'from the given word=',w)

# x,y,z=map(int,input().split())
# mylist=[]
# for i in range(x):
#     a=int(input())
#     mylist.append(a)
# for j in mylist:
#     if j>=y and j<=z:
#         print(j,end=' ')

# import datetime
# date=datetime.datetime.now()
# print("its now:{:%d%m%Y %H:%M:%S}".format(date))

#x=['A','B','C']
#y=['A','B','C']
#z=[1,2,3,4]
#print(x==y)
#print(x==z)
#print(x!=z)         

# s=[1,4,9,16,25,36,49,64,81,100]
# val=[2**i for i in range(1,6)]
# print(val)
# val2=[i for i in s if i%2==0]
# print(val2)


# squares={x:x*x for x in range(1,6)}
# print(squares)

# how to read multiple values from the keyboard in a

# doubles={x:2*x for x in range(1,6)}
# print(doubles)

# a,b,c=[float(x) for x in input("enter 3 float numbers:").split(',')]
# print("The sum is:",a+b+c)

# mycart=[10,20,800,60,70]
# for item in mycart:
#     if item>400:
#         print("this is not my budget")
#         continue
#     print(item)
# else:
#     print("you have purchased everything")

# while True:
#     username = input("Enetr username:")
#     password = input("Enter password:")
#     if username == "admin" and password == "admin":
#         print("Login")
#         break
#     else:
#         print("Invalid")




