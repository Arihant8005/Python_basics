# 1. Even–Odd Separator

# Write a program that takes n numbers and prints two lists — one with even numbers and one with odd numbers.
# Concepts: loops, conditionals, list handling

numbers = [int(x) for x in input("Enter numbers: ").split()]
#int(x) for x in ...
#Converts each small string "10", "20", etc. into integers
# .split()
#  Splits that string into a list of smaller strings (based on spaces).
# Result: ["10", "20", "30", "40"]
even = []
odd = []

for val in numbers:
    if(val % 2 == 0):
        even.append(val)
    else:
        odd.append(val)

print("Even numbers:", even)
print("Odd numbers:", odd)
