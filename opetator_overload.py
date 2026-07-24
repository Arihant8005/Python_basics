#polymorphism : when the same operator is allowed to have different meaning according to context
# operators and dunder functions:
# a+b   :   a__add__b
# a-b   :   a__sub__b
# a*b   :   a__mul__b
# a/b   :   a__truediv__b
# a%b   :   a__mod__b

# adding two complex numbers
class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def show_num(self):
        print(self.real,"i+",self.img,"j")
    def __add__(self,num2):                    # here we created a dunder function
        newreal=self.real+num2.real
        newimg=self.img+num2.img
        return complex(newreal,newimg)

num1=complex(2,-8)
num1.show_num()

num2=complex(4,5)
num2.show_num()

num3=num1+num2
num3.show_num()