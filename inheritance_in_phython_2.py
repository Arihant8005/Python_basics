#multi level inhetrance
class car:
    def start(self):
        print("starting..")
    def stop(self):
        print("stoping..")
class Toyota(car):
    def __init__(self,name):
        self.name=name
class Alto(Toyota):
    def __init__(self,brand):
        self.brand=brand

c1=Alto("Mahendra")
c2=Toyota("kishan")
print(c2.name)
print(c1.brand)
c1.start()