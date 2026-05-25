#Types Of Error

# RuntimeError
# CompileTimeError


#kyu aa rha kaise aa rha kaise handle krege


# try:
#     a=int(input("Enter First Number: "))
#     b=int(input("Enter Second Number: "))

#     print(a/b)
# except ZeroDivisionError:
#     print("can't divide by zero")
# except ValueError:
#     print("Enter only integer value: ")
# except:
#     print("Default except ")

# try:
#     a=int(input("Enter First Number: "))
#     b=int(input("Enter Second Number: "))

#     print(a/b)
# except (ZeroDivisionError,ValueError) as msg:
#     print(msg)



# try:
#     a= int(input("Enter first number: "))
#     b= int(input("Enter second number: "))
#     print(a/b)
# except ZeroDivisionError:
#     print("cant divide by zero")
# except ValueError:
#     print("Enter only integer value")
# except:
#     print("Error")
# finally:
#     print("im always executed")
# # else:
# #     print("Everything is okay")
# # except (ZeroDivisionError, ValueError) as msg:
# #     print(msg)

# import logging
# logging.basicConfig(filename="newfile.txt", level=logging.DEBUG)
# try:
#     a=int(input("enter first integer no")) 
#     b=int(input("enter second integer no")) 
#     print(a/b)
# except (ZeroDivisionError, ValueError) as message:
#     print(message)
#     logging.exception(message)
# print("Logging Level is set up. Check 'newfile.txt' for log details.")


#Why we use File Handling

# import csv
# f=open("employee.csv",'a')
# a = csv.writer(f)
# a.writerow(["EmpID","EmpName","EmpAge"])
# empid = int(input("Enter your EmpId : "))
# empname = (input("Enter your EmpName : "))
# empage  = int(input("Enter your EmpAge : "))
# a.writerow(["empid","empname","age"])
# print("File has created")

# import csv
# f = open("employee.csv", 'a', newline='')
# a = csv.writer(f)

# # Uncomment only first time to create heading
# # a.writerow(["EmpID", "EmpName", "EmpAge"])

# empid = int(input("Enter your EmpId : "))
# empname = input("Enter your EmpName : ")
# empage = int(input("Enter your EmpAge : "))

# a.writerow([empid, empname, empage])

# print("File has been created and data added successfully")

# f.close()

# Column Name = studentId, Studentname,phy,chem,math,Total,Percentage,Result   
# input: studied,studname,phy,chem,math
# calculate : total,percentage
#check condition all paper marks >= 40 pass else fail


# import csv
# f = open("student.csv", 'a', newline='')

# a = csv.writer(f)

# #Uncomment only first time
# # a.writerow(["studentId", "studentName", "phy", "chem", "math",
# #             "Total", "Percentage", "Result"])

# studentId = int(input("Enter Student ID : "))
# studentName = input("Enter Student Name : ")

# phy = int(input("Enter Physics Marks : "))
# chem = int(input("Enter Chemistry Marks : "))
# math = int(input("Enter Maths Marks : "))

# # Calculate total
# total = phy + chem + math

# # Calculate percentage
# percentage = total / 3

# # Check result
# if phy >= 40 and chem >= 40 and math >= 40:
#     result = "Pass"
# else:
#     result = "Fail"

# # Write data into CSV
# a.writerow([studentId, studentName, phy, chem, math,
#             total, percentage, result])

# print("Student record added successfully")

# f.close()