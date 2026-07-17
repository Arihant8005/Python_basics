#methods are function that belongs to object
class Student:
    collage_name="poornima"
    def __init__(self,name,marks,hobby):
        self.name=name
        self.marks=marks
        self.hobby=hobby
    def hello(self):
        print("my name is",self.name)
    def get_marks(self):                         # in methods we add some lines
        print("my marks is",self.marks)
    def get_hobby(self):
        print("my hobby is to play",self.hobby)
        
s1=Student("arihant",74,"chess")
print(s1.name,s1.marks,s1.hobby)
s1.hello()
s1.get_marks()
s1.get_hobby()