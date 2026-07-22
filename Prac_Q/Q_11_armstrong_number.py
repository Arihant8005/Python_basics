# Q11: Check if a Number is an Armstrong Number
# A number is an Armstrong number if the sum of its digits raised to the power of the number of digits equals the number itself.
# 👉 Example:
# 153 → 1³ + 5³ + 3³ = 153 → Armstrong number

n = int(input("Enter the number: "))

if (n < 0):
    print("Negative numbers cannot be Armstrong numbers.")
else:
    temp = n
    digits = len(str(n))
    sum = 0

    while (n != 0):
        rem = n % 10
        sum += rem ** digits
        n //= 10

    if (sum == temp):
        print("Armstrong number")
    else:
        print("Not an Armstrong number")