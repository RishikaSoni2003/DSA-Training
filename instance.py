# where we can create insatnce variable it depends on the object ....creates sepreat memory for every value
# class New():
#     def __init__(self):
#         self.a = 10
# obj1 = New()
# obj2 = New()
# obj3 = New()
# obj1.a=20
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

# class New():
#     a = 10
# def __init__(self):
#     self.name = "rishika"
# obj1 = New()
# obj2 = New()
# obj3 = New()
# New.a = 50 

# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

# For every object, a separate copy of instance variables is created.
# But in case of static variables, only one copy is created
# and it is accessible by every object of the class.

# class College:

#     collegename = "Modern College"   # Static variable (1 memory shared)

#     def __init__(self):
#         self.studentname = "Aastha"   # Instance variable (separate for each object)

# # Object creation
# principal = College()
# teacher = College()
# accountant = College()

# print("principal =", principal.collegename, "....", principal.studentname)
# print("teacher =", teacher.collegename, "....", teacher.studentname)
# print("accountant =", accountant.collegename, "....", accountant.studentname)


# # Changing static variable
# College.collegename = "HBD"

# # Changing instance variable of only principal object
# principal.studentname = "Aastha Bais"

# print("\nAfter changes:\n")

# print("principal =", principal.collegename, "|", principal.studentname)
# print("teacher =", teacher.collegename, "|", teacher.studentname)
# print("accountant =", accountant.collegename, "|", accountant.studentname)

