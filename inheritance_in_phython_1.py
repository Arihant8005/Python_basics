# it is of three types:# 1.single inheritance  2.multi level inheritance  3.multiple inheritance
# SINGLE INHERITANCE
class car:
    def start(self):
        print("starting..")
    def stop(self):
        print("stoping..")
class Toyota(car):
    def __init__(self,name):
        self.name=name

c1=Toyota("alto")
c2=Toyota("kishan")
print(c1.name)
print(c2.name)
c1.stop()
c1.start()
#OR 
# class car:
#     @staticmethod            BY USING staticmethod: i.e () iss ke andhar 'self' nahi likhna phadta
#     def start():
#         print("starting..")
#     @staticmethod
#     def stop():
#         print("stoping..")
# class Toyota(car):
#     def __init__(self,name):
#         self.name=name

# c1=Toyota("alto")
# c2=Toyota("kishan")
# print(c1.name)
# print(c2.name)
# print(c1.stop())
