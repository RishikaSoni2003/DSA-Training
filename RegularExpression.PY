# import re   # module for performing all the regular expression based operations

# count = 0

# pattern = re.compile("python")   # string converts into bytecode

# matcher = pattern.finditer(
#     "A function in python is defined by a def statement. "
#     "The general syntax looks like this: "
#     "def function_name(parameter list): statements, i.e. the function body. "
#     "The parameter python list consists of none or more parameters."
# )

# for i in matcher:
#     count += 1
#     print(i.start(), "", i.end(), "", i.group())

# print("The number of occurrences:", count)

# import re
# count=0
# matcher=re.finditer("Hi","HiHiHiHi")
# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("The number of occurrences: ",count)

# import re
# a=input("Enter string to perform match operation: ")
# mtch=re.match(a,"Python is very important language")
# print(mtch)
# if mtch!=None:
#     print("Match found at Begining Level")
#     print(mtch.start()," ",mtch.end())
# else:
#     print("There is no matching at begining level")


# import re
# s=input("Enter mail id: ")
# m=re.fullmatch("\w[a-zA-Z0-9_.]@gmail.com",s)
# if m!=None:
#     print("Valid E-mail Id")
# else:
#     print("Invalid E-mial ID")

# import re
# mo=input("Enter Moblie number:")
# obj=re.fullmatch("[0-5]\d{9}",mo)
# if obj!=None:
#     print("Valid Number")
# else:
#     print("Invalid Number")

# search() function

# import re
# a = input("Enter string to perform match operation: ")

# mtch = re.search(a, "python sss dynamic lannn")

# print(mtch)

# if mtch is not None:
#     print(mtch.start(), "", mtch.end(), "", mtch.group())
# else:
#     print("There is no matching anywhere")

# import re
# mtch=re.findall('[A-Z]',"abch3hdh5bk7ZQ%&*")
# print(mtch)

# import re
# obj=re.sub('[a-z]','*','2345 ABCS hbbs deff')
# print(obj)

# import re 
# obj = re.subn('[0-7]','@','ab3gd6nkKL7' )
# print(obj)
# print("the string is=",obj[0])
# print("the number of replacement is=",obj[1])

# WAP to extract all mobile numbers from input.txt

# import re

# f1 = open("input.txt", "r")
# f2 = open("output.txt", "w")

# for line in f1:
#     numbers = re.findall(r"[6-9]\d{9}", line)
    
#     for num in numbers:
#         f2.write(num + "\n")

# print("Mobile numbers extracted successfully!")

# f1.close()
# f2.close()

# class Graph:
#     def __init__(self,vertices):
#         self.V=vertices
#         self.matrix=[[0 for _ in range(vertices)]for _ in range(vertices)]

#     def display(self):
#         for row in self.matrix:
#             print(row)
            
# g=Graph(4)     
# g.display()     

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def display(self):
        for row in self.matrix:
            print(row)

    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1


# Create graph with 4 vertices
g = Graph(4)

# Add edges
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

# Display adjacency matrix
g.display()

# hashing is a technique that is use to data into a fixed size value call a hash value or a hash code 
# and that is use to search data fast 
# convert data into fixed index


                                                                                                                                                                                                                                                