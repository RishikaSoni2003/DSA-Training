# mydict={
# 101:"prashant",
# 102:"ashish",
# "103":"mohini",
# "104":"trivani",
# 101:"ashish",
# 104:"ashish",
# 103:"mohini",}
# print(mydict)

# mydict[102]="peter"
# print(mydict)

# for x in mydict:
#     print(x)
# for x in mydict.values():
#     print(x)
# for x,y in mydict.items():
#     print(x,y)
# mydict["mobile_no"]=6786543876
# print(mydict)
# mydict.pop(101)
# print(mydict)

# a={(1,2):1,(2,3):2,(4,5):3}#we take tuple as key
# print(a[4,5])

# a={'a':1,'b':2,'c':3}
# print(a['a','b'])

# arr={}
# arr[1]=1
# arr['1']=2
# arr[1.0]=4
# print(arr)#{1: 4, '1': 2}
# sum=0
# for k in arr:
#     sum+=arr[k]
# print(sum)

# dict={}
# dict[(1,2,4)]=8
# dict[(4,2,1)]=10
# dict[(1,2)]=12
# sum=0
# for k in dict:
#     sum+=dict[k]

# print(sum)
# print(dict)

# box={}
# jars={}
# crates={}
# box['biscuit']=1
# box['cake']=3
# box['jam']=4
# crates['box']=box
# crates['jars']=jars
# print(len(crates[box]))

# dict={'c':97,'a':96,'b':98}
# for _in sorted(dict):
#     print(dict[_])

# rec={"name":"python","age":"20"}
# r=rec.copy()
# print(id(r)==id(rec))
# print(id(r))
# print(id(rec))

# rec={"name":"python","age":"20","addr":"NJ","country":"usa"}
# id1=id(rec)
# del rec
# rec={"name":"python","age":"20","addr":"NJ","country":"usa"}
# id2=id(rec)
# print(id1==id2)

# a={"A":50,"B":30,"C":70}
# max=max(a.keys())
# print(max)
# min=min(a.keys())
# print(min)

# num = 123456
# a = num%10
# num=num//10
# b= num%10
# num=num//10
# c= num%10
# num=num//10
# d= num%10
# num=num//10
# e= num%10
# f=num // 10
# rev = a*100000 + b*10000 + c*1000+d*100+e*10+f*1
# print (rev)

# amount=int(input("please enter amount for withdraw:"))
# print("100 notes=",amount//100)
# print("50 notes=",(amount%100)//50)
# print("20 notes=",((amount%100)%50)//20)
# print("10 notes=",(((amount%100)%50)%20)//10)
# print("10 notes=",(((amount%100)%50)%20)//10)
# print("10 notes=",(((amount%100)%50)%20)//10)
# print("10 notes=",(((amount%100)%50)%20)//10)
# print("5 notes=",((((amount%100)%50)%20)%10)//5)
# print("2 coin=",(((((amount%100)%50)%20)%10)%5)//2)
# print("1 coin=",((((((amount%100)%50)%20)%10)%5)%2)//1)

# 14 may
#while loop - when range is not given 

# i=1
# while i<=5:
#     print(i)
#     i+= 1

#function

# def hello():
#     print("hello world")

# hello() #calling function 
# hello()

# def arithamatic():
#     a = int(input("Enter the value of a:"))
#     b = int(input("Enter value of b:"))
#     sum = a+b
#     sub = a-b
#     div = a/b
#     mul =  sum, sub, div, mul 

#  arithamatic()

# # result =arithamatic()
# # print("Arithematic =",result)

# # Positional argument 
# def arithamatic():
#     a = int(input("Enter the value of a:"))
#     b = int(input("Enter value of b:"))
#     sum = a+b
#     sub = a-b
#     div = a/b
#     mul = a*b 
#     return sum, sub, div, mul

# # Positional argument 
# result = arithamatic(5,5)
# print("Arithematic =",result)

# keyword argumnet - paramerte name and keyword mus be same 

# def crdential(username, password):
#     if username == password:
#         print("login successfully")
#     else:
#         print("invalid credential:")

#         crdential(username ="admin", password ="admin") #calling function 

# default argument  if we are not passing any argument we can pass default argument/parmeter

# def cityname(city="Pune"):
#     print(city)

# cityname("Nagpur")
# cityname("Mumbai")
# cityname()

# variable length argument/variable no. of argument  * will print all the arguments in the function

# def cityname(*name):
#     print(name)

# cityname("Nagpur", "Mumbai", "pune")

#modularity approach in function 
# import sys
# def add():
#     a = int(input("Enter value of A:"))
#     b = int(input("Enbetr the value of B:"))
#     print(a+b)

# def sub():
#     a = int(input("Enter value of A:"))
#     b = int(input("Enbetr the value of B:"))
#     print(a-b)

# def div():
#     a = int(input("Enter value of A:"))
#     b = int(input("Enbetr the value of B:"))
#     print(a/b)

# def mul():
#     a = int(input("Enter value of A:"))
#     b = int(input("Enbetr the value of B:"))
#     print(a*b)

# while True:
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Division")
#     print("4. Multiplication")
#     print("5. Exit")
#     choice = int(input("Enter your choice :"))
#     if choice == 1:
#         add()
#     elif choice == 2:
#         sub()
#     elif choice == 3:
#         div()
#     elif choice == 4:
#         mul()
#     elif choice == 5:
#         sys.exit()

# def findingBiggestNumber(sampleArray):
#     biggestNumber = sampleArray[0]                   #O(1)
#     for index in range (1, len(sampleArray)):        #O(N)
#         if sampleArray[index] > biggestNumber:       #O(1)
#             biggestNumber = sampleArray[index]       #O(1)
#     print(biggestNumber)                             #O(1)

# sampleArray =[5,7,9,2,3,4]                           #O(1)
# findingBiggestNumber(sampleArray)

# def linearsearch(array,target):
#     for i in range(0,len(array)):
#         if array[i]==target:
#             return i

# array=[1,2,3,4,5,8,7,9]
# target=7
# result=linearsearch(array,target)
# if result == -1:
#     print("target value not found")
# else:
#     print(" found at:",result )

# city=input("enter your city name:")
# scity=city.strip()
# if scity=='hydrabad':
#     print("hello hydrabad")
# elif scity=='chennai':
#     print("hello chennai")
# elif scity=='Bengalore':
#     print("hello Bengalore")
# else:
#     print("innvalid city")

# Q Row wise max value 
# [[100, 198, 333, 323]
#  [122, 232, 221, 111]
#  [223, 565, 245, 764]]

# mylist=[[100, 198, 333, 323], [122, 232, 221, 111], [223, 565, 245, 764]]
# newlist=[]
# for i in range(3):
#     j=0
#     max = mylist[i][j]
#     for j in range(4):
#         c_max = mylist[1][j]
#         if max < c_max:
#             max = c_max
#     newlist.append(max)

# print(newlist)

# s="Rishika*is*a*good*programmer"
# new_s=""
# val=''
# for i in s:
#     if i!='*':
#         new_s+=i
#     else:
#         val+=i
# print(new_s)
# print(str(val+new_s))   

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

import sys
class stack:
    def __init__(self,size):
        self.mystack=[]
        self.stackSize = size

    def isFull(self):
        if len(self.mystack) == self.stackSize:
            return True
        else:
            return False
        
    def push(self,value):
        if self.isFull():
            print("Stack is full")
        else:
            self.mystack.append(value)
            print("element push")
        
    def display(self):
        print(self.mystack)
        
    def isEmpty(self):
        if self.mystack==[]:
            return True
        else:
            return False
            
    def pop(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            print(self,self.mystack.pop())
            
    def peek(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            print(self.mystack[-1])
            
    def delete(self):
        self.mystack=None
size= int(input("Enter the size of stack: "))
obj=stack(size)
print("stack has created")
while True:
   
    print("1.push operation:")
    print("2.display stack:")
    print("3.pop stack:")
    print("4. peek ")
    print("5.delete operation")

    print("7.Exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        value=int(input("enter value to push in stack:"))
        obj.push(value)
    elif choice==2:
        obj.display()
    elif choice==3:
        obj.pop()
    elif choice==4:
        obj.peek()
    elif choice==5:
        obj.delete()
    else:
        sys.exit()
        break
     
