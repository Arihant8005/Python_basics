n= int(input("Enter the number :"))

fact = 1
for i in range(0 , n + 1):
    if(i == 0):
        print(i,"! = 1" )
    else:
        fact = fact * i
        print(i, "! =",fact)