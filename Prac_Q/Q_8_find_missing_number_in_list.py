# 8. Find Missing Number

# Given a list of consecutive numbers with one missing, find the missing one.
# Example: [1, 2, 3, 5, 6] → 4
# Concepts: math logic, sum formulas, reasoning

num=[int(x) for x in input("given series:").split()]
num.sort           #arrange the randomly arrange numbers in order
for el in range(num[0], num[-1] + 1):       #not use len(num) cannot give largest number
    if el not in num:                     #because num[-1] gives largest num in the list
        print("missing number:", el)
