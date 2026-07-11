#largest and smallest among three numbers

num1 = int(input("num1:"))
num2 = int(input("num2:"))
num3 = int(input("num3:"))
largest = smallest = num1
if(num2 > largest):
    largest = num2
if(num3 > largest):
    largest = num3
if(num2 < smallest):
    smallest = num2
if(num3 < smallest):
    smallest = num3

print("largest number is", largest)
print("smallest number is", smallest)