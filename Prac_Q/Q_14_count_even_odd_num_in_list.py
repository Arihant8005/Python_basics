# Q14 Count Even and Odd Numbers in a List

numbers = (int(x) for x in input("Enter numbers: ").split())
even = 0
odd = 0

for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)