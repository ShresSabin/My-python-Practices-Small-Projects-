# class Student():
#     def __init__(self):
#         print("Adding new Students")


# s1=Student()
# print(s1)

#-------------------------------------#

# class Car:
#     color="Red"
#     brand="maercedes"

# car1=Car()
# print(car1.color,car1.brand)

#-------------------------------------#
class Student():
    
       
    college_name="ABC College"
    def __init__(self,name,marks):
        print("Adding new Students")
        self.name=name
        self.marks=marks
    def welcome(self):
        print("Welcome student",self.name)


s1=Student("Sabin",80)
s1.welcome()
print(s1.college_name)
print(s1.name ,"has", s1.marks)


