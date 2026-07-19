#create account class with balance and acc. no. and add method debit , credit and printing balance

class Account:
    def __init__(self,acc_num,bal):
        self.acc_num=acc_num
        self.bal=bal
    def debit(self,amount):
        self.bal-=amount
        print("Rs.",amount,"was debited")
    def credit(self,amount):
        self.bal+=amount
        print("Rs.",amount,"was credit")
    def get_balance(self):
        print("totat balance:",self.bal)

a1=Account(12345,10000)
print("acc. num:",a1.acc_num)
print("bal:",a1.bal)
a1.debit(1000)
a1.credit(500)
a1.get_balance()

#OR
# class Account:
#     def __init__(self,acc_num,bal):
#         self.acc_num=acc_num
#         self.bal=bal
#     def debit(self,amount):
#         self.bal-=amount
#         print("Rs.",amount,"was debited")
#         print("total balance:",self.get_balance())
#     def credit(self,amount):
#         self.bal+=amount
#         print("Rs.",amount,"was credit")
#         print("total balance:",self.get_balance())
#     def get_balance(self):
#         return self.bal

# a1=Account(12345,10000)
# print("acc. num:",a1.acc_num)
# print("bal:",a1.bal)
# a1.debit(1000)
# a1.debit(2000)
# a1.credit(500)