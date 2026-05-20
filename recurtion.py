# when the main problem can be divided into similar sub problem then will use recurtion 
#also uses stack memory its a less timr efficient but it is time effcient 

# def factorial(num):
#     if num <= 1:
#         return 1
#     return num*factorial(num-1)

# print(factorial(4))

# def capitalizesirst(arr): #will make the first letter capital
#     result = []
#     if len(arr) ==0:
#         return result
    
#     result.append(arr[0][0].upper() + arr[0][1:])
#     return result + capitalizesirst(arr[1:])

# print(capitalizesirst(['car', 'taco', 'banana']))

#power

# def power(base,exponent):
#     if exponent==0:
#         return 1
#     return base*power(base,exponent-1)
# print(power(2,0))
# print(power(2,2))
# print(power(2,4))

#productOfArray solution 
# def productOfArray(arr):
#     if len(arr) == 0: #if false 
#         return 1
#     return arr [0] * productOfArray(arr[1:]) # will jump here 
#                #1*2*3
#                #1*2*3*10
# print(productOfArray([1,2,3]))
# print(productOfArray([1,2,3,10]))
    
#reverseString using recurtion

# def reverse(string):
#     if len(string) <= 1:
#         return string
#     return string[len(string)-1] + reverse(string[0:len(string)-1])
    
# print((reverse('python')))
# print((reverse('appmillers')))

# recursiveRange

# def recursiveRange(num):
#     if num <= 0:
#         return 0 
#     return num + recursiveRange(num - 1)
# print(recursiveRange(6))  

#palindrome

# def isPalindrome(string):
#     if len(string) == 0:
#         return True
#     if string[0] != string[len(string)-1]:
#         return False
#     return isPalindrome(string[1:-1])

# print(isPalindrome('awesome'))
# print(isPalindrome('tacocat'))

#somerecursive solution 

# someRecursive Solution

# def someRecursive(arr, cb): # cb - isodd function
#     if len(arr) == 0:
#         return False

#     if not(cb(arr[0])):
#         return someRecursive(arr[1:], cb)

#     return True


# def isOdd(num):
#     if num % 2 == 0:
#         return False
#     else:
#         return True

# print(someRecursive([1, 2, 3, 4], isOdd))   # true
# print(someRecursive([4, 6, 8, 9], isOdd))   # true
# print(someRecursive([4, 6, 8], isOdd))      # false

