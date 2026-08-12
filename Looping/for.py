#----------------------------------------#

# list1 = [10, 20, 30, 40, 50]

# for i in reversed(list1):
#     print(i)

#---------------------------------------------#

# nums=[1,4,9,16,25,36,49,64,81,100]
# print(nums)
# x=int(input("ENter the number on the list:"))
# idx=0
# for i in nums:
#     if i==x:
#         print("Found the number on index",idx)
#         break
#     idx+=1   
# else:
#        print("Number not found")

#------------------------------#

# str="Python"

# for i in reversed(str):
#     print(i, end="")

#------------------------------#

# n=int(input("Enter a number:"))

# for i in range(1,11):
#     print(f"{n}x{i}={n*i}")

#----------------------------------#

# for i in range(5):
#     pass
# print("some work")

#-----------------------#
#for loop natural sum
# n=int(input("Enter number:"))

# sum=0

# for i in range(1,n+1):
#     sum+=i
# print("Total sum is:",i)    
#-------------------------------------#
#for loop
# n=int(input("Enter number:"))
# i=1
# sum=0

# while i<=n:
#     sum+=i
#     i+=1
# print("Total Sum=",sum)

#--------------------------------------#

#Factorial

# n=int(input("Enter a number: "))

# fact=1

# i=1

# while i<=n:
#     fact*=i
#     i+=1
# print("Factorial",fact)

#---------------------------------------#

#for loop

n=int(input("Enter a number: "))

fact=1

for i in range(1,n+1):
    fact*=i
print("Factorial",fact)    
