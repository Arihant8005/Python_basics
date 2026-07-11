# input sallary from user and if salary is greater than 5000 than give 5% of his sallary as bonus otherwise give bonus = 250 rupees

num=int(input("salary:"))
if(num>=5000):
    bonus=0.05*num
else:
    bonus=250
print(bonus)