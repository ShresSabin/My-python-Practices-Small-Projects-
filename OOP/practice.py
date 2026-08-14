class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Hi",self.name,"Your average marks is ",sum/3)


s1=Student("Sabin",[90,80,70])

print(s1.name,s1.marks)

s1.get_avg()