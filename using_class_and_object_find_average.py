#create student class that takes name and marks of three subjects as arguments in constructor.
#Then create a method to print avg.

# # BY USING FOR LOOP
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val

        avg=sum/len(self.marks)
        print("your avg score is",avg)

s1=Student("arihant",[99,98,97])
s1.get_avg()

# # BY USINF WHILE LOOP
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def get_avg(self):
#         sum=0
#         i=0
#         while i<len(self.marks):
#             sum+=self.marks[i]
#             i+=1
#         print("your avg score is",sum/len(self.marks))

# s1=Student("arihant",[99,98,97])
# s1.get_avg()