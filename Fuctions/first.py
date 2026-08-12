# def avg_three(a,b,c):
#     average=(a+b+c)/3
#     print(average)
#     return average

# avg_three(1,2,3)


#------------------------------------------------------#
#WAP to find length of a list

# cities=["Delhi","Kathmandu","Berlin"]
# heroes=["Superman","Batman","Spiderman"]
# def print_len(list):
#     print(len(list))

# print_len(cities)

# print_len(heroes)

#------------------------------------------------------#

#WAP to print elements of list in a single line

# cities=["Delhi","Kathmandu","Berlin"]

# def element(lis):
#     for item in lis:
#         print(item,end=" ")

# element(cities)

#------------------------------------------------------#

#WAP to factorial of n



# def fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)

# fact(6)    


#------------------------------------------------------#

# Convert USD to NPR
 
# def converter(usd_val):
#     inr_val=usd_val*83
#     print(usd_val,"USD=",inr_val,"INR")

# converter(1)


#------------------------------------------------------#
# a=int(input("Enter:"))

# def o_e(n):

#     if n%2==0:
#         print("Even!")
#     else:
#         print("Odd!")

# o_e(a)

#------------------------------------------------------#
# n=int(input("Enter:"))

# def show(a):
#     if (a==0):
#         return
#     print(a)
#     show(a-1)

# show(n)

#------------------------------------------------------#

# a=int(input("Enter:"))
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*fact(n-1)

# print(fact(a))
#------------------------------------------------------#

# def calc_sum(n):
#     if(n==0):
#         return 0
#     print(n)
#     return calc_sum(n-1 )+ n

# calc_sum(4)

#------------------------------------------------------#



# def print_list(list,idx=0):
#     if(idx==len(list)):
#         return
#     print(list[idx])
#     print_list(list,idx+1)
# fruits=["a","b","c","d"]

# print_list(fruits)
    
