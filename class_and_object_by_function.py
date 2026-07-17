class Student:                               #creating class
    def __init__(self,name,marks,hobby):       #creating function  #__init__ is a constructor 
       self.name= name                        # name,marks,hobby are attributes
       self.marks= marks                    #self refers to the current object.
       self.hobby= hobby                         #Without __init__, you would have to assign values manually.
s1=Student("arihant",92.17,"chess")             #creating object
print(s1.name,s1.marks,s1.hobby)
s2=Student("gopi",92.8,"cricket")
print(s2.name,s2.marks,s2.hobby)
s3=Student("kishan",87.9,"chess")
print(s3.name,s3.marks,s3.hobby)

# AND
class Student:                                       #creating class
    collage_name="poornima university"               #same for all students
    def __init__(self,name,marks,hobby):             #creating function
       self.name= name
       self.marks=marks
       self.hobby=hobby
s1=Student("arihant",92.17,"chess")             #creating object
print(s1.name,s1.marks,s1.hobby)
s2=Student("gopi",92.8,"cricket")
print(s2.name,s2.marks,s2.hobby)
s3=Student("kishan",87.9,"chess")
print(s3.name,s3.marks,s3.hobby)

print(Student.collage_name)
