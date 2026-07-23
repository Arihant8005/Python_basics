# Q16 Count How Many Times Each Number Appears 

from collections import Counter

n=[int(x) for x in input("enter the numbers:").split()]

print(Counter(n))

# or
# n = [int(x) for x in input("Enter the numbers: ").split()]

# count = {}

# for num in n:
#     if num in count:
#         count[num] += 1
#     else:
#         count[num] = 1

# print(count)