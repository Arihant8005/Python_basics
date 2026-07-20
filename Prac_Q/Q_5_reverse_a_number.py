# 5. Reverse a Number

# Input: 12345 → Output: 54321
# (Don’t use string slicing)
# Concepts: arithmetic, while loops, modulo operator

num = int(input("Enter the number: "))

rev_num = 0
while(num != 0):
    rem = num % 10
    rev_num = rev_num * 10 + rem
    num //= 10

print(rev_num)