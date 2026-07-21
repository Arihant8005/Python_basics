# 7. Fibonacci Sequence

# Print the first n Fibonacci numbers.
# Concepts: sequence generation, variable swapping, iteration

n = int(input("How many terms:"))

a = 0
b = 1

if(n == 1):
    print(a)
else:
    print(a, b,end=" ")
    for i in range(2, n):
        c = a + b
        print(c,end=" ")
        a = b
        b = c

# or
# n = int(input("Enter the number upto which you want to print the fibonachi series: "))

# a = 0
# b = 1
# if(n == 1):
#     print(a)
# else:
#     for i in range(2, n + 2):
#         print(a, end = " ")
#         c = a + b
#         a = b
#         b = c

