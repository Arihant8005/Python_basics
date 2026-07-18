class person:
    name="vinod"
    @classmethod
    def change_name(self,name):
        self.name=name

p1=person()
p1.change_name("arihant")
print(p1.name)
