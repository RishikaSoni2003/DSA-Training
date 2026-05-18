# reverse string
# s = "Hello world"
# words = s.split()
# reversed_words = []

# for word in words:
#     reversed_words.append(word[::-1])

# result = " ".join(reversed_words)
# print(result)

# while True:
#     username = input("Enetr username:")
#     password = input("Enter password:")
#     if username == "admin" and password == "admin":
#         print("Login")
#         break
#     else:
#         print("Invalid")

# s = input("Enetr parentheses string:")

# stack = []

# pairs = {')' : '(',
#          ']' : '[',
#          '}' : '{'}

# valid = True

# for ch in s:
#     if ch in "({[":
#         stack.append(ch)
#     else:
#         if not stack or stack [-1] !=pairs[ch]:
#             valid = False
#             break
#         stack.pop()
#     if valid and not stack:
#         print("Valid")
#     else:
#         print("Invalid")

# def insertion(arr):
#     for i in range(1,len(arr)):
#         key=arr[i]
#         j=i-1
#         while(j>=0) and arr[j]>key:
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j+1]=key
#     return arr
# n=[5,3,8,6,2]
# sortedarr=insertion(n)
# print(sortedarr)

