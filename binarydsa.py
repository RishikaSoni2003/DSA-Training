#15 may
# important question input = aaabbbbccceee
# output = a3b4c3e5

# name = 'aaabbbbccceee'
# newname ={}
# for i in range(len(name)):
#     key = name[i]
#     count=0
#     for j in range(len(name)):
#         if key == name[j]:
#             count+=1
#     newname [key] = count
# print(newname)
# for i,j in newname.item():
#     print(i,j,sep='',end='')

# salary = int(input("Enter you salary:"))
# rating = int(input("Enter you performance appraisal rating :"))
# increment =0
# if rating >=1 and rating<=3:
#     increment = salary * 10/100
# elif rating>=3.1 and rating<=4:
#     increment = salary*30/100
# elif rating >= 4.1 and rating<=5:
#     increment = salary*40/100
# else:
#     print('Invalid rating')
# print('Increment Salary: ',increment=salary)

# basicSal = int(input("Enter basic salary :"))
# hra=basicSal *(20/100)
# ta=basicSal *(30/100)
# da=basicSal *(45/100)
# gs=(basicSal+hra+ta+da)
# print(gs)

#Binary Search 

# def binarysearch(array,target):
#     low=0
#     high=len(array)-1
#     while low<=high:
#         mid=(low+high)//2
#         if array[mid]==target:
#             return mid
#         elif array[mid]<target:
#             low=mid+1
#         else:
#             high=mid-1
#     return -1

# array=[2,4,5,9,11,13,14,15,19,20,22,23,37,40]
# target=37
# result=binarysearch(array,target)
# if result == -1:
#     print("element not found")
# else:
#     print("element found at",result)

# def bubblesort(array):
#     for i in range(len(array)-1):
#         for j in range(len(array)-i-1):
#             if array[j] > array[j+1]:
#                 temp=array[j]
#                 array[j]=array[j+1]
#                 array[j+1]=temp
#             print(array)
#         print()
# array=[64,34,25,12,22,11,90]
# bubblesort(array)            

#input: 578378923
# output:3

# mylist = [5,7,8,3,7,8,9,2,3]
# newlist = []

# for i in range(len(mylist)):
#     count=0
#     key=mylist[i]
#     j =i+1
#     while j<len(mylist):
#         if key == mylist[]:
#             newlist.append(key)
#         j = j+1
# print(len(newlist))

#Class and object 

# class name:
#     age = 38
#     def display(self):
#         print("Hello World")

# obj = name() #object is called as reference variable
# print(obj.age)
# obj.display()

# class student:
#     def __init__(self):
#         print("I am constructor")
#     def shows(self):
#         print("class program")
# obj=student()

# class studentinfo:
#     def __init__(self,name,age,rollno):
#         self.Name=name
#         self.Age=age
#         self.Rollno=rollno
#     def displaystu(self):
#         print("Name",self.Name)
#         print("Age",self.Age)
        
# studentobj=studentinfo("Prakash",34,101)
# studentobj.displaystu()

#stack operations

# import sys
# class stack:
#     def __init__(self):
#         self.mystack=[]
#     def push(self,value):
#         self.mystack.append(value)
#         print("element push")
#     def display(self):
#         print(self.mystack)
#     def isEmpty(self):
#         if self.mystack==[]:
#             return True
#         else:
#             return False
#     def pop(self):
#         if self.isEmpty():
#             print("stack is empty")
#         else:
#             print(self,self.mystack.pop())
#     def peek(self):
#         if self.isEmpty():
#             print("stack is empty")
#         else:
#             print(self.mystack[-1])
#     def delete(self):
#         self.mystack=None

# size = int(input("Enter the size of stack :"))

# obj=stack()
# print("stack has created")
# while True:
   
#     print("1.push operation:")
#     print("2.display stack:")
#     print("3.pop stack:")
#     print("4. peek ")
#     print("5.delete operation")

#     print("7.Exit")
#     choice=int(input("enter your choice:"))
#     if choice==1:
#         value=int(input("enter value to push in stack:"))
#         obj.push(value)
#     elif choice==2:
#         obj.display()
#     elif choice==3:
#         obj.pop()
#     elif choice==4:
#         obj.peek()
#     elif choice==5:
#         obj.delete()
#     else:
#         sys.exit()

#stack with limited size
# import sys
# class stack:
#     def __init__(self,size):
#         self.mystack=[]
#         self.stackSize = size

#     def isFull(self):
#         if len(self.mystack) == self.stackSize:
#             return True
#         else:
#             return False
        
#     def push(self,value):
#         if self.isFull():
#             print("Stack is full")
#         else:
#             self.mystack.append(value)
#             print("element push")
        
#     def display(self):
#         print(self.mystack)
        
#     def isEmpty(self):
#         if self.mystack==[]:
#             return True
#         else:
#             return False
            
#     def pop(self):
#         if self.isEmpty():
#             print("stack is empty")
#         else:
#             print(self,self.mystack.pop())
            
#     def peek(self):
#         if self.isEmpty():
#             print("stack is empty")
#         else:
#             print(self.mystack[-1])
            
#     def delete(self):
#         self.mystack=None
# size= int(input("Enter the size of stack: "))
# obj=stack(size)
# print("stack has created")
# while True:
   
#     print("1.push operation:")
#     print("2.display stack:")
#     print("3.pop stack:")
#     print("4. peek ")
#     print("5.delete operation")

#     print("7.Exit")
#     choice=int(input("enter your choice:"))
#     if choice==1:
#         value=int(input("enter value to push in stack:"))
#         obj.push(value)
#     elif choice==2:
#         obj.display()
#     elif choice==3:
#         obj.pop()
#     elif choice==4:
#         obj.peek()
#     elif choice==5:
#         obj.delete()
#     else:
#         sys.exit()
#         break

#Q 
def bubblesort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
            print(array)
        print()
array=[64,34,25,12,22,11,90]
bubblesort(array)

mylist=[5,7,8,3,7,8,8,9,2,3,3]
newdict={}
for i in range(len(mylist)):
    count=0
    key=mylist[i]
    j=1
    while j<len(mylist):
        if key==mylist[j]:
            count+=1
        j=j+1
    if count>1:
        newdict[key]=count
max=newdict
print(max)