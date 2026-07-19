class student:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths
    @property                             #@methodname takes only self as a argument
    def percentage(self):
       percentage = str((self.phy+self.chem+self.maths)/3 ) + "%"
       print(percentage)
    #  or  return percentage
s1=student(99,98,97)
s1.percentage
# or print(s1.percentage)

s1.phy=91
s1.percentage
#OR
# class student:
#     def __init__(self,phy,chem,maths):
#         self.phy=phy
#         self.chem=chem
#         self.maths=maths
#     @property
#     def percentage(self):
#         return str((self.phy+self.chem+self.maths)/3)+"%"

# s1=student(99,98,97)
# print(s1.percentage)

# s1.phy=91
# print(s1.percentage)
