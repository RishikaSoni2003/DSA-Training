# age = 33
# pi = 3.14
# name = "rish"
# result = True 
# print(type(age))
# print(type(pi))
# print(type(name))
# print(type(result))

# age = 33
# pi = 3.14
# name = "rish"
# result = True 
# print(id(age))
# print(id(pi))
# print(id(name))
# print(id(result))

# math = 50 
# chem = 50
# phy =  50
# print(id(math))
# print(id(chem))
# print(id(phy))

# print(2+2)
# print("2"+"2")
# a = int(input("Enter first Number :"))
# b = int(input("eneyr second Number :"))
# print(a+b)

# typecast

# print(int(1.14))
# #pritnint (it(10+5j)) 
# print(int(True)) #=1
# print(int(False)) #=0
# #print(int("4.22"))
# print(int("4"))

#cannot type cast complex no

# flot() used to conver 
# print(float(3))
# #print(float(50+2j))
# print(float(True))
# print(float(False))
# print(float("3.14"))
# print(float("4"))

# complex() used to convert 

# print(complex(3))
# print(complex(12.5))
# print(complex(True))
# print(complex(False))
# print(complex("5"))
# print(complex("5.6"))
# # print(complex(name ))
# print(complex(5, -3))
# print(complex(True,False))

# if we pass the zero it will conver it into false 

# print(bool(0))
# print(bool(15))
# print(bool(3.14))
# print(bool(0.0))
# print(bool(1+2j))
# print(bool(0+0j))
# print(bool(-1))
# print(bool(False))
# print(bool(True))
# print(bool(""))
# print(bool("rishika"))

#simple if 

# a  = int (input ("Enter any single digit :"))
# if a >0:
#     print("positive number")
# if a< 0:
#     print("Negitive number")
#     if a ==0:
#         print("Zero")

# if else - it decide flow of execution

# day = input(" Enter day :")
# if day == "SATURDAY" or day == "saturday" or day == "SUNDAY" or day == "sunday" 
#      print("weekend")
# else:
#     print("working day")

#if elif

# per =65
# if per > 65:
#     print("grade A")
# elif per <=65 and per >=50:
#     print("Grade B")
# else:
#     print("fail")


# chr = ord(input("Enter any one chararacter :"))#b
# #ord function is use to convert ascii code 
# if chr >=65 and chr<=90:
#     print("upper case")
# elif chr >=97 and chr <=122:
#     print("lower case")
# elif chr >=48 and chr <=57:
#     print("digit")
# else:
#     print("special")

# in or not in 

# name = "helpcenter" 
# print('z' in name ) # there or not 

#identity operator - use for address comparison 

# math = 50
# chem = 50
# print(math is chem) # will return coz have same value will have same address 

# for loop - will increment internally sequentaly 

# for i in range (5):
#     print(i) 

# for i in range (2, 11,): # 
#     print(i) 

# for i in range (2, 11,2): # will increment by 2
#     print(i) 

# for i in range (5, 0, -1): # will decrement -1 
#     print(i) 

# for i in range (1, 11,): 
#     print(i*2, " ",i*3," ",i*4, " ",i*5," ",i*6," ",i*7," ",i*8," ",i*9," ",i*10) 
# print()
# for i in range (1, 11,): 
#     print(i*11, " ",i*12," ",i*13," ",i*14," ",i*15," ",i*16, " ",i*17, " ",i*18," ",i*19, " ",i*20) 


# a = input("Enter marks of math): ")
# b =  input("Enter marks sub phy : ")
# c =  input("Enter marks sub chem : ")
# total = math+phy+chem
# percentage = total/3.0
# print("total = ",total)
# if phy >=40 and chem >=40 and phy >=40:
#     print("pass")
# else:
#     print("fail")
#  gender = input("Enter your gender M/F :")
# if percent >=65 and gender == "M":
#     print("Elegible for placement")
# else:
#     print("Not Elegible for placement ")

# for i in range  (1,6):
#     if i ==3:
#         continue 
#     print (i)

# zip() we can take multiple range function inside zip()

# for i,j in zip(range(1,6),range(5,0,-1)): #
#     if i ==3 and j ==3:
#         continue 
#     print (i, "   ",j)

#List

# mylist = ["rishika" , "aastha" , "janvi" , "Aarya" , "riya" , 77, "sandip" , 60.52, "rishika"]
# print(mylist)
# print(type(mylist))#<list>
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[ :5])
# print(mylist[1: ])

# mylist[2] = "aastha"
# print(mylist)

# if "rishika" in mylist:
#     print("yes rishika in avaiable")
# else:
#     print('not avilable')

# mylist.append('harsh')  #add alwasys at the top only  
# mylist.append('laxman')
# print(mylist)  #append() and extend() works same    

# mylist.insert(3,"sanket")
# print(mylist)

# mylist.remove("sandip")
# print(mylist)

# newlist = mylist.copy() #cloning   copy everything objests an all
# print(newlist)

# mylist = [['prashant', 'jga'],['85,56'],[440022,"yyy"]]
# print("example of multidimentional list : ")
# print(mylist)
# #print(mylist[row][col])
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])

# list2 =[50,25.50,'prashant']
# del list2

# list2 = [50,25.50,'prashant']
# list2.clear()
# print(list2)

# name= "prashant"
# print(name)
# myname=list(name)
# print(myname)   #we have used list constructor

# mylist =[44,22,77,0,9,88]
# #mylist.sort()
# mylist.sort(reverse=True)
# print(mylist)

# mylist=[44,22,77,0,9,88] #alising means assigning one variable reference to another 
# newlist = mylist 
# print(id(mylist))
# print(id(newlist))

# mylist=[44,22,77,0,9,88]
# for i in mylist:
#     print(i)

# list1=[0,1,4,0,2,5]
# for i in list1:
#     if i ==0:
#         list1.remove(i)
#         list1.append(i)
# print(list1)

# mylist=[7,3,9,2,8]
# mylist.sort(reverse=True)
# print(mylist [1])

# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)

# a=[1,2,3,4,5]
# print(a[3:0:-1])

# arr = [[1, 2, 3, 4]
#        [4, 5, 6, 7]
#        [8, 9, 10, 11]
#        [12, 13, 14, 15]]
# for i in range(0, 4): #only focus on outer loop i.e rows
#     print(arr[i].pop())

# arr = [1, 2, 3, 4, 5, 6]
# for i in range(1, 6):
#     arr[i - 1] = arr[i]

# for i in range(0, 6):
#     print(arr[i], end = " ")

#advance question

# fruit_list1 = ['Apple', 'Berry', 'Cherry', 'pappya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
# fruit_list2[0] = 'Guava'
# fruit_list1[1] = 'kiwi'

# sum = 0 
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Guava' :
#         sum += 1
#         if ls[1] == 'kiwi' :
#             sum += 20
# print(sum)

# A = [1, 2, 3]
# B = [2, 3, 4]
# C = [3, 4, 5]

# for i in A:
#     if i in B and i in C:
#         print(i)

