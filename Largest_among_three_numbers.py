Num1 = int(input("Enter NUM 1 : "))
Num2 = int(input("Enter NUM 2 : "))
Num3 = int(input("Enter NUM 3 : "))

Largest = Num1
if(Num2 > Largest):
    Largest = Num2
if(Num3 > Largest):
    Largest = Num3

print("Largest = ", Largest)