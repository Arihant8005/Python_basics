# 2. Sum Without Using sum()

# Given a list of integers, find their sum without using the built-in sum() function.
# Concepts: loops, accumulator variables

numbers=[int(x) for x in input("enter numbers:").split()]

#print(sum(numbers))       not to use this

print(numbers)
sum = 0
for num in numbers:
    sum += num
    
print("sum = ",sum)
